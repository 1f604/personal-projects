#to do: create a hash data structure with file name, date modified and file hash as tuple (perhaps line-break delimited), so that we can track duplicates more easily.
#also perhaps more bugs to be ironed out? it works fine so far.
#created on 9th May 2015
#!/usr/bin/python
import time
import os
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import errno
import hashlib
#import sys



foldername = "dropbox"
namelen = None
dirname = None
hasher = None

def copy(src, dest):
    global hasher
    try:
        if not os.path.exists(dest):
            print "src is"+src
            print "dest is"+dest
            print src
            if not os.path.exists(os.path.dirname(dest)):
                os.makedirs(os.path.dirname(dest))
            shutil.copy(src, dest)
        else: #if file already exists, create a new file
            print "src2 is"+src
            print "dest2 is"+dest
            with open(src, 'rb') as afile:
                buf = afile.read()
            digest1 = hashlib.sha224(buf).hexdigest()
            print(digest1)
            afile.close()

            # with open(dest, 'rb') as afile:
            #     buf = afile.read()
            # hasher.update(buf)
            # digest2 = hashlib.sha224(buf).hexdigest()
            # print(digest2)
            # if digest1==digest2:
            #     print "STRING COMPARISON SUCCESSFUL"
            # else:
            #     print "NOT EQUAL!"
            desti = dest+"["+digest1+"]"
            print desti
            if not os.path.exists(desti):
                print "src1:"
                print src
                print "yeah!"
                try:
                    shutil.copy(src, desti)
                except Exception,e: print str(e)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
            global dirname
            global namelen
            print event.src_path
            print type(event)
            if type(event) is watchdog.events.FileCreatedEvent or type(event) is watchdog.events.FileModifiedEvent:
                print "YES! a"
                # print event.src_path
                copy(event.src_path,dirname+"_backup"+event.src_path[2+namelen:])

            # if(event.is_directory):
            #     files_in_dir = []
            #     for f in os.listdir(event.src_path):
            #         if f != ".DS_Store":
            #             files_in_dir.append(event.src_path+"/"+f)
            #     print files_in_dir
            #     mod_file_path = max(files_in_dir, key=os.path.getmtime)
            #     print mod_file_path
            #     dirname, filename = os.path.split(mod_file_path)
            #     print dirname
            #     print "filename is:" + filename

if __name__ == "__main__":
    #create hashing object
    hasher = hashlib.md5()
    #make backup folder if it doesn't already exist
    #dirname, filename = os.path.split(os.path.abspath(__file__))
    dirname = "./"+ foldername
    namelen = len(foldername)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    if not os.path.exists(dirname+"_backup"):
        shutil.copytree(dirname,dirname+"_backup")
    #start the file system watcher
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=dirname, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()