#pixiv downloader finished on 21st 07/2015
#NO EXTERNAL MODULES REQUIRED! :DDDDDD
#basic outline of what this program does:
# 1. Find out how many pages there are : numpages(url)
# 2. Get medium links ON each page (at the time of this writing each "gallery" page has 20 medium links, but this is not relevant as my functions will automatically calculate the number each time) : geturlsfrompage(url)
# 3. Go to each medium link and find the download links that contain the actual art (could be picture, manga or animation) : downloadi(url) (3 different download functions plus another one for manga links)
# 4. Download each url : fetch(url)

username = raw_input("enter your username here")
password = raw_input("enter your password here")
id = input("enter the id of the user whose work you wish to download")


import urllib, urllib2, cookielib, httplib, re, time, os, sys, contextlib
from collections import deque
from threading import Thread
from socket import timeout

mediumillusts = deque([])
mediummangas = deque([])
mediumugoiras = deque([])
idowns = deque([]) #image urls, direct link
udowns = deque([]) #animation urls, direct link
mdowns = deque([]) #manga urls, links to a manga page containing the manga images
midowns = deque([]) #manga image urls, direct link


httplib.HTTPConnection._http_vsn = 10 #need this to avoid "incomplete read" problems
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

def ceildiv(a, b):
    return -(-a / b)

def numpages(address,p=1): #this is the new version. runs in constant time. takes the base address and the page number as arguments, then visits the url made by appending the page number to the base address, then looks at the "results" field in the html (so requires server cooperation) and divides by the number of images per page which it calculates by looking at the html again (assumes constant number of images per page which is reasonable)
        s = fetch(address+str(p))
        results = re.findall(r'<span class="count-badge">([0-9]*) results', s)
        sectionurls = re.findall(r'<a.*?href="([^"]*/member_illust.php\?mode=medium\&amp;illust_id=[0-9]*)"', s)
        nums = re.findall(r'&amp;type=[a-z]*&amp;p=([0-9]*)', s)
        if nums == []: #base case: there is only 1 page: solve by returning 1, trivial.
            return p
        r = int(results[0]) #inductive step: there is more than 1 page.
        st = set(sectionurls)
        return ceildiv(r,len(st)) #ceiling division because the last page may not contain a full page's worth of elements

def geturlsfrompage(address, urls): #print isn't thread-safe until python 3, using print in multiple threads will cause a RuntimeError. This function gets the medium url from each picture page.
    #try:
        start = time.clock()
        s = fetch(address)
        sectionurls = re.findall(r'<a.*?href="([^"]*/member_illust.php\?mode=medium\&amp;illust_id=[0-9]*)"', s)
        st = set(sectionurls)
        urls.extend(["http://www.pixiv.net"+url.replace("&amp;", "&") for url in st]) #because the links are relative URLs
        elapsed = (time.clock() - start)


def downloadi(url): #illustration
        s = fetch(url)
        imageurl = re.findall(r'data-src="(http://[^"]*)" class="original-image"', s)
        filename = os.path.basename(imageurl[0]).rsplit('?',1)[0] #windows can't create files with question marks in their names nd sometimes pixiv gives us these URLs
        aa = fetch(imageurl[0])
        FILE = open(filename, "wb")
        FILE.write(aa)
        FILE.close()
        return


def downloadm(url): #manga
        s = fetch(url.replace("medium", "manga"))
        murls = re.findall(r'data-src="(http://[^"]*)"', s)
        folder = os.path.basename(murls[0])[:-7]
        if not os.path.exists(folder):
            os.makedirs(folder)
        threads = []
        for murl in murls:
            t = Thread(target=downloadmi, args=(murl, folder))
            t.start()
            threads.append(t)
        for p in threads:
            p.join()
        return

def downloadmi(url, folder): #manga images
        filename = os.path.basename(url).rsplit('?',1)[0]
        aa = fetch(url)
        FILE = open(folder+"/"+filename, "wb")
        FILE.write(aa)
        FILE.close()
        return

def downloadu(url): #ugoira
        s = fetch(url)
        imageurl = re.findall(r'"src":"([^"]*ugoira1920x1080.zip)"', s)
        imageurl[0] = urllib.unquote(imageurl[0]).replace("\\", "")
        filename = os.path.basename(imageurl[0]).rsplit('?',1)[0]
        aa = fetch(imageurl[0], 20.0) #increase  the value here if downloading particularly large zip files
        FILE = open(filename, "wb")
        FILE.write(aa)
        FILE.close()
        return


def fetch(url, tout = 20.0):  #no need to declare opener global since we are not going to modify it, may need to increase timeouts for larger files. Longer timeout = fewer restarts = fewer requests = nicer on the server.
    req= urllib2.Request(url)
    try:
        with contextlib.closing(opener.open(req, timeout=tout)) as conn: #the timeout is pretty important, without it threads will hang forever, files will not be downloaded and the program will never terminate
            s = conn.read()
            conn.close()
            return s
    except timeout:
        print "timed out trying to fetch " + url + ", trying again"
        return fetch(url)

def login():
        global opener

        opener = urllib2.build_opener(urllib2.HTTPDefaultErrorHandler,
                urllib2.HTTPErrorProcessor, urllib2.HTTPSHandler,
                urllib2.HTTPCookieProcessor(cookielib.LWPCookieJar()), #Need a correct cookie and login to obtain the html - but do not need cookie or login to download the images
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0)) #change debuglevel to 1 to see request headers and response codes

        opener.addheaders = [('Referer', 'http://www.pixiv.net/')] #Need correct referer to download images otherwise server returns 403 forbidden - but the html do not need a referer.
        forms = {
                'mode': 'login',
                'skip': '1'
        	    }
        forms["return_to"]= "google.com"
        forms["pixiv_id"]= username
        forms["pass"] = password
        data = urllib.urlencode(forms)
        req = urllib2.Request('http://www.pixiv.net/login.php',data)
        res = opener.open(req)
        s = res.read()
        if s.find("pixiv.user.loggedIn = true") == -1:
            return "Login failed"
        return "Logged in"


address = "http://www.pixiv.net/member_illust.php?type="
iaddr=address+"illust"+"&id="+str(id) + "&amp;p="
maddr=address+"manga"+"&id="+str(id) + "&amp;p="
uaddr=address+"ugoira"+"&id="+str(id) + "&amp;p="
print login()


start = time.clock()
numillusts = numpages(iaddr)
nummangas = numpages(maddr)
numugoiras = numpages(uaddr)
elapsed = (time.clock() - start)
print "time taken to get number of pages:"
print elapsed

start = time.clock()
threads = [] #start threads that go to each illustration, manga and animation page and grab all the links from each page into their respective deques
for i in range(1,numillusts+1):
    t = Thread(target=geturlsfrompage, args=(iaddr+str(i), idowns))
    t.start()
    threads.append(t)
for i in range(1,nummangas+1):
    t = Thread(target=geturlsfrompage, args=(maddr+str(i), mdowns))
    t.start()
    threads.append(t)
for i in range(1,numugoiras+1):
    t = Thread(target=geturlsfrompage, args=(uaddr+str(i), udowns))
    t.start()
    threads.append(t)
for t in threads:
    t.join()

print "finished gathering URLs"
elapsed = (time.clock() - start)
print "time taken to get URLS:"
print elapsed
if len(idowns) != len(set(idowns)): #sanity checks
    sys.exit("urls list contains duplicate")
if len(mdowns) != len(set(mdowns)):
    sys.exit("urls list contains duplicate")
if len(udowns) != len(set(udowns)):
    sys.exit("urls list contains duplicate")

#Now that we have the medium urls, we get the download pages from these urls



start = time.clock()
threads = []
for url in idowns:
    t = Thread(target=downloadi, args=(url,))
    t.start()
    threads.append(t)
for url in mdowns: #should not have any race conditions to do with creating directories because the URLS should have no duplicates
    t = Thread(target=downloadm, args=(url,))
    t.start()
    threads.append(t)
for url in udowns:
    t = Thread(target=downloadu, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()


elapsed = (time.clock() - start)
print "time taken to download all URLs:"
print elapsed

raw_input("All done.")
