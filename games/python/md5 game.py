#Created on 4th of November 2014
import hashlib
import string
import random
rndstr = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(500))
m = hashlib.md5()
m.update(rndstr)
result = 0
print "Welcome to my game!"
print "In order to win the game, you need to score at least 70"
for i in xrange(5):
    newstr = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(50))
    m.update(newstr)
    print "Current game status: " + m.hexdigest()
    print "Your current score is: " + str(result)
    userinput = raw_input("please enter a string")
    m.update(userinput)
    a = m.hexdigest()[-1]
    result+= int(a,16)
print "Your final score is: " + str(result)
if (result >= 70):
    print "You win!"
else:
    print "You lose!"
input("Press enter to exit")