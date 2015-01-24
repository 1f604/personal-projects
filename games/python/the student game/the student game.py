#created on 22nd January 2015
#runs on python 2.7
import string
import math
from random import randint

def printhelp():
    print "Help (h):"
    print "Do [Task] (d [Task]): Does the task specified by number. Example usage: Do 0"
    print "Play (p): Play a video game" #play games
    print "Surf (s): Surf the internet or surf TV channels" #regenerates stamina
    print "Walk (w): Go out for a walk" #have a walk
    print "Go (g): Go out to make new connections (and possibly get a girlfriend)"
    print "Roll (r): Do something random and hope something good happens"
    print "Meditate (m): Meditate for up to 1 hour" #reduces impulsivity
    print "Practice (pr): Practice solving problems for up to 1 hour" #practice maths, increases intelligence and skill
    print "Exercise (ex): Exercise for up to 1 hour" #increases intelligence, constitution and stamina
    print "Concepts (c): Display concepts"
    print "Learn [concept] (l [concept]): Try to learn a concept for up to 1 hour. Example usage: Learn parity" #increases stats massively during learning
    print "Sleep (sl): Makes you sleep."
    print "nd: Skips to the next day."
    print "Stats (st): Shows stats"
    print "Exit (e): Exits the game without saving"
    print "Once your luck or skill reaches a certain level, you will unlock a special power that will enable you to win the game."

def showWork():
    if tasks != []:
        print "Tasks to do:"
        for i in range(len(tasks)):
            print str(i) + ". " + tasks[i][2] + str(". Amount remaining: " + str(tasks[i][0]) + ". Time remaining: "+ str(tasks[i][1]) + " days")
    else:
        print "There are no tasks to do."

def minus (max, i):
    result = max - i
    if result >= 0:
        return result
    else:
        return 0

def rollstat(type):
    statboost = [["Maximum intelligence",14],["Willpower",12],["Attractiveness",12],["Maximum attention",25],["Maximum stamina",15],["Constitution",20]]
    boost = 45
    incre = 1
    w = 0
    if type == "Impulsivity":
        w = 100
        boost = 17
        incre = -1
    elif type in [x[0] for x in statboost]:
        boost = [x for x in statboost if x[0] == type][0][1] #A shitty and inefficient way to use a nested list as a dictionary
    for i in xrange(100):
        k = minus(boost,i) #Gives the player a free chance boost
        p = randint(0, 3 + k)
        if(p == 0):
            break
        else:
            w += incre
    return w

def rollimpulse():

    return w

def rollstats():
    global attention
    global attentionmax
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    global intelligence
    global intelligencemax
    for i in stats:
        i[0][0] = rollstat(i[1])
    attention[0] = 0
    stamina[0] = 0
    constitution[0] = constitutionmax[0] * 0.2
    intelligence[0] = intelligencemax[0] * 0.4
    #total = sum([i[0] for i in stats])

def printstats():
    for i in stats:
        print "You rolled " + str(i[0]) + "/100 in " + str(i[1])


#initialize variables
def rand():
    w= 5
    for i in xrange(10000):
        p = randint(0, 200)
        if(p == 0):
            break
        else:
            w += 1
    return w

def generateconcepts():
    result = {}
    list = ["Finite state machine", "Memoization", "Shor's Algorithm", "Linear Programming", "Convex Optimization","Denotational Semantics", "Recursion", "Parity", "Regular expression", "boolean algebra", "lexing", "regex", "parsing", "string matching", "caching", "iteration", "pointers", "hashtables", "sorting", "context free grammar", "turing machines","computability", "sets", "trees", "graphs", "computational complexity", "databases", "compilers", "operating systems", "propositional logic", "predicate logic", "2nd order logic", "cellular automata", "finite state machines", "search", "dimensions", "lines", "points", "planes", "waves", "probability", "induction", "pigeonhole principle", "Bayes' law", "Benford's law"] #bunch of random shit
    for i in list:
        result[i] = rand()
    return result

concepts = generateconcepts()
age = [15]
tasks = []
tasksgenerated = 0
year = [1];
day = [1];
luck = [0];
power = [0];
weekday = 1; #1 is monday, 2 is tuesday, etc, 7 is sunday
termtime = range(76) + range(116,180) + range(270,350)
time = [5]; #wake up at 5am, there are 24 hours in a day
cap = 365;
ondrugs = False;
sleepdeprived = False;
sleepdeprivationthreshold = 16; #How many hours without sleep before you go sleep deprived
hourswithoutsleep = 0; #start with a sleep debt of 0. As sleep debt increases your other stats go down. Not implemented.
canfallasleep = True #Can he fall sleep? Insomnia, drugs, stress and other conditions prevent this. Not implemented.
sleeptime = 8; #How long the person will sleep for the next time he falls asleep.
attention = [0]; #How much attention you can currently spare. Depleted by doing tasks and replenished by rest.
attentionmax = [0]; #How much attentional capacity you have.
constitution = [0]; #How good your body is. Reduced by lack of exercise.
constitutionmax = [0]; #How good your body could be.
willpower = [0]; #How much willpower you have.
impulsivity = [100]; #How impulsive you are.
stamina = [0]; #How much more physical energy you have. Physical tasks drain more stamina than things like video games.
staminamax = [0]; #How much max stamina you can have.
attractiveness = [0]; #How attractive you are.
intelligence = [0]; #how fast you gain knowledge and skills. The higher your intelligence, the more skill you gain from doing a task.
intelligencemax = [0]; #The cap on your intelligence.
skill = [0]; #How skilled you are. Has no cap but gain is based on intelligence.
stats = [[impulsivity, "Impulsivity"], [willpower, "Willpower"], [attentionmax, "Maximum attention"], [constitutionmax, "Maximum constitution"], [staminamax, "Maximum stamina"], [intelligencemax, "Maximum intelligence"], [attractiveness, "Attractiveness"]]
currentstats = [[skill, "Skill"], [impulsivity, "Impulsivity"], [willpower, "Willpower"],  [attention, "Attention"],[attentionmax, "Maximum attention"], [constitution, "Constitution"], [constitutionmax, "Maximum constitution"], [stamina, "Stamina"],[staminamax, "Maximum stamina"], [attractiveness, "Attractiveness"], [intelligence, "Intelligence"], [intelligencemax, "Maximum intelligence"]]
lives = [3]
girlfriend = [False]
happiness = [0]

def showStats():
    for i in currentstats:
        if i[1] != "Skill":
            print i[1] + ": " + str(round(i[0][0], 1))+"/100"
        else:
            print i[1] + ": " + str(round(i[0][0], 1))

def getnextdate(date,termtime): #done
    counter = date+1
    for i in termtime:
        if i == counter:
            counter+=1
        elif i > date:
            return i

def showInfo(): #done
    global day
    global termtime
    if day[0] in termtime:
        print "It is currently termtime. Holiday begins at day " + str(getnextdate(day[0],termtime))
    else:
        print "It is currently holidays. Term begins at " + str(getnextdate(day[0],termtime))

def showTime():
    global termtime
    print "Current status: Year "+ str(year[0]) + " Day "+ str(day[0])+" "+ days[day[0]%7] + ". Time: "+str(time)


def rolltasks():
    w = 0
    for i in xrange(8):
        p = randint(0, 2)
        if(p == 0):
            break
        else:
            w += 1
    return w

def rolleffort():
    w = 1
    roll = randint(0,10) #Decide whether to return a multiple of 7 or what
    if roll < 2:
        numbers = [1,2,3,4,5,6]
        k = randint(0,len(numbers)-1)
        return numbers[k]
    elif roll <= 8:
        numbers = [7,7,7,7,14,14,14,14,21,21,30]
        k = randint(0,len(numbers)-1)
        return numbers[k]
    elif roll == 9:
        numbers = [60,90,120]
        k = randint(0,len(numbers)-1)
        return numbers[k]
    else:
        return randint(0,365)

def rolltimeleft(effort):
    w = 0 #random number from 0 to 100, higher being less likely
    for i in xrange(100):
        p = randint(0, 2)
        if(p == 0):
            break
        else:
            w += 1
    w = 1 + w/10.0
    return int(effort / w)+1

def generatetaskname():
    nameslist = ["Math coursework", "Project report", "Group project", "Math essay", "Individual project", "Individual essay", "Lab writeup", "Take-home exam", "Exam revision", "Individual report", "Group report", "Presentation", "Individual presentation", "Group presentation", "Individual research", "Group research", "Elevator pitch", "Client report", "Project evaluation", "Project plan", "Requirements analysis", "System design", "Problem-based learning"]
    k = randint(0, len(nameslist)-1)
    return nameslist[k]

def generatetask():
    global age
    global tasks
    hardness = year[0] #How hard the homework is, depends on year.
    effort = rolleffort() #rolls the basic amount of effort needed.
    effort = effort * (hardness * 1.09 ** hardness * 0.05) #hardness scales with your age.
    timeleft = int(rolltimeleft(effort)*6 / 1.2 ** hardness) + 2 #time decreases exponentially with your age.
    tasks.append([round(effort,2),timeleft,generatetaskname()])


def generatetasks():
    global tasks
    global termtime
    global day
    print "It's a new day!"
    if day[0]%7 in [6,7] or day[0] not in termtime:
        print "It is a free day. You did not go to school today."
    else:
        print "You went to school today."
        numtasks = rolltasks()
        print "Number of tasks assigned: "+ str(numtasks)
        for i in xrange(numtasks):
            generatetask()

def start():
    print "Welcome to the student game!"
    print "To do well in this game, you need both luck and good judgment!"
    print "Start by rolling your character's stats. Press enter to begin."
    print "Type 'Help' for help"
    raw_input()
    rollstats()
    printstats()
    main()

def regen(stat, stat_max, regen_rate, statname, method, printstat = True):
    if stat[0] < stat_max:
        oldstat = stat[0]
        if stat[0] < stat_max - regen_rate:
            stat[0] += regen_rate
        else:
            stat[0] = stat_max
        if printstat: print statname + ": " + str(round(oldstat,2)) + " -> " + str(round(stat[0],2))
    else:
        if printstat: print statname + " was unchanged because it was already at the highest level achievable by " + method +"."

def decay(stat, limit, decay_rate, statname, method, printstat = True):
    if stat[0] > limit:
        oldstat = stat[0]
        if stat[0] > limit + decay_rate:
            stat[0] -= decay_rate
        else:
            stat[0] = limit
        if printstat: print statname + ": " + str(round(oldstat,2)) + " -> " + str(round(stat[0],2))
    else:
        if printstat: print statname + " was unchanged because it was already at the lowest level achievable by " + method +"."

def rolltempted(hardness, secondarystat, secondarystatmax): #Done
    global impulsivity
    global willpower
    if willpower[0] > impulsivity[0]:
        return False
    else:
        p = randint(0,int(impulsivity[0]*hardness))
        return p+1.5*willpower[0]*(1-(float(secondarystat) / (secondarystatmax+1))) > willpower[0]

def rolltime(hardness): #Hardness value should normally be >0.01
    global impulsivity
    global willpower
    k = int(impulsivity[0] - willpower[0])
    w=0
    if hardness <= 1:
        for i in range(60):
            l = randint(0,k)
            if l >= k*hardness:
                w+=1
            else:
                break
    else:
        for i in range(60):
            l = randint(0,k*hardness)
            if l == 0:
                w+=1
            else:
                break
    return w

def meditate(): #Impulsivity reduction = duration * willpower
    global attention
    global attentionmax
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    global impulsivity
    global willpower
    print "Tried to meditate for 1 hour"
    if (rolltempted(0.3, attention[0], attentionmax[0]) == False and attention[0] > 0):
        if attention[0] > 60 and willpower[0] > impulsivity[0]:
            print "You were able to meditate for the entire hour"
            print "Stat changes:"
            #Attention regen at 12 per hour up to 60% of max
            decay(attention, 0, 60, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*willpower[0], "Impulsivity", "meditation")
        elif willpower[0] > impulsivity[0]:
            print "You only had enough attention to meditate for " +str(duration) + " hours"
            print "Stat changes:"
            duration = 60 - attention[0]
            decay(attention, 0, 60, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*(duration/60.0)*willpower[0], "Impulsivity", "meditation")
            print "You then went off to do another activity:"
            temptedactivity(60-duration)
        else:
            length = rolltime(0.1) #0.1 is a good value
            duration = min(attention[0], length)
            print "You meditated for " +str(duration) + " minutes before you got bored/ran out of attention."
            print "Stat changes:"
            #Attention regen at 12 per hour up to 60% of max
            decay(attention, 0, duration, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*(duration/60.0)*willpower[0], "Impulsivity", "meditation")
            chance = randint(0,5)
            if chance == 5:
                regen(luck,100,1,"Luck","Meditation")
            print "You then went off to do another activity:"
            temptedactivity(60-duration)
    else:
        print "You were either tempted to not meditate or you had 0 attention."
        temptedactivity()

def meditate(): #Impulsivity reduction = duration * willpower
    global attention
    global attentionmax
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    global impulsivity
    global willpower
    print "Tried to meditate for 1 hour"
    if (rolltempted(0.3, attention[0], attentionmax[0]) == False and attention[0] > 0):
        if attention[0] > 60 and willpower[0] > impulsivity[0]:
            print "You were able to meditate for the entire hour"
            print "Stat changes:"
            #Attention regen at 12 per hour up to 60% of max
            decay(attention, 0, 60, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*willpower[0], "Impulsivity", "meditation")
        elif willpower[0] > impulsivity[0]:
            print "You only had enough attention to meditate for " +str(duration) + " hours"
            print "Stat changes:"
            duration = 60 - attention[0]
            decay(attention, 0, 60, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*(duration/60.0)*willpower[0], "Impulsivity", "meditation")
            print "You then went off to do another activity:"
            temptedactivity(60-duration)
        else:
            length = rolltime(0.1) #0.1 is a good value
            duration = min(attention[0], length)
            print "You meditated for " +str(duration) + " minutes before you got bored/ran out of attention."
            print "Stat changes:"
            #Attention regen at 12 per hour up to 60% of max
            decay(attention, 0, duration, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*(duration/60.0)*willpower[0], "Impulsivity", "meditation")
            print "You then went off to do another activity:"
            temptedactivity(60-duration)
    else:
        print "You were either tempted to not meditate or you had 0 attention."
        temptedactivity()

def exercise(): #Increase max constitution and max stamina, done
    global attention
    global attentionmax
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    global impulsivity
    global willpower
    print "Tried to exercise for 1 hour"
    if (rolltempted(0.2, stamina[0], staminamax[0]) == False and attention[0] > 0):
        duration = stamina[0]
        print "You had enough stamina to exercise for " +str(duration) + " minutes"
        print "Stat changes:"
        decay(stamina, 0, 60, "Stamina", "exercise")
        #Intelligence loss at 0.01 per hour down to 0
        regen(staminamax, 100, 0.1*(duration/60.0), "Max stamina", "exercise")
        regen(constitution, 100, 2*(duration/60.0), "Constitution", "exercise")
        regen(constitutionmax, 100, 0.1*(duration/60.0), "Max constitution", "exercise")
        if (duration < 60):
            print "You then went off to do another activity:"
            temptedactivity(60-duration)
    else:
        print "You were either tempted to not exercise or you had 0 stamina."
        temptedactivity()

def cleanup(minutes):
    print "You ran out of attention and dozed off for " +str(minutes) + " minutes."
        #Attention regen at 0.15 per minute up to 60% of max
    regen(attention, 0.6*attentionmax[0], 0.15*minutes, "Attention", "dozing off")
    #Stamina regen at 0.05 per minute per hour up to 100% of max
    regen(stamina, staminamax[0], 0.05*minutes, "Stamina", "dozing off")

def decayvidya(minutes, printstat = True):
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    k = minutes / 60.0
    if stamina[0] < k:
        diff = k - stamina[0]
        decay(stamina, 0, 100, "Stamina", "playing", printstat)
        if (constitution[0] < diff/2.0):
            print "You died"
            exit(6)
        else:
            decay(constitution, 0, (diff/2.0)+(minutes/6000.0), "Constitution", "playing", printstat)
    else:
        decay(stamina, 0, k, "Stamina", "playing", printstat)
        decay(constitution, 0, minutes/6000.0, "Constitution", "playing", printstat)


def play(minutes=60, printstat=True): #Done
    global attention
    global attentionmax
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    global impulsivity
    global time
    duration = minutes
    #Impulsivity regen at 0.5 per hour of playing
    if printstat == True:
        print "You played video games for " + str(duration) + " minutes."
        print "Stat changes:"
    regen(impulsivity, 300, 0.5*(duration/60.0), "Impulsivity", "playing", printstat)
    #Attention regen at 12 per hour up to 60% of max
    decayvidya(duration, printstat)
    #Intelligence loss at 0.02 per hour down to 0
    decay(intelligence, 0, 0.01*(duration/60.0), "Intelligence", "playing", printstat)

def surf(minutes=60, printstat = True): #done
    global attention
    global attentionmax
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    global impulsivity
    k = minutes
    duration = k
    flag = False
    if stamina[0]*100.0 < k:
        duration = stamina[0]*100
        flag = True
    #Impulsivity regen at 0.4 per hour of playing
    if printstat == True:
        print "Stat changes:"
        print "You surfed the internet for " + str(duration) + " minutes."
    regen(impulsivity, 130, 0.12*(duration/60.0), "Impulsivity", "surfing", printstat)
    #Attention regen at 12 per hour up to 60% of max
    decay(stamina, 0, (duration/100.0), "Stamina", "surfing", printstat)
    #Constitution regen at 0.1 per hour up to 80% of max
    decay(constitution, 0, (duration/6000.0), "Constitution", "surfing", printstat)
    #Intelligence loss at 0.02 per hour down to 0
    decay(intelligence, 0, 0.012*(duration/60.0), "Intelligence", "surfing", printstat)
    if flag:
        m = k - duration
        doze(m) #Done

def doze(minutes): #done
    print "You ran out of stamina while surfing the internet, so you dozed off for "+str(minutes)+" minutes."
    regen(stamina, staminamax[0], 7*(minutes/60.0), "Stamina", "dozing off")
    #Constitution regen at 0.1 per hour up to 80% of max
    regen(constitution, constitutionmax[0], 3*(minutes/60.0), "Constitution", "dozing off")



def remainder(stat, value):
    if stat > value:
        return value
    else:
        return value-stat

def walk(): #done
    global attention
    global attentionmax
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    global intelligencemax
    print "Trying to walk"
    if rolltempted(0.1, stamina[0], staminamax[0]) == False:
        if (stamina[0]*constitution[0] < 30):
            print "Not enough stamina"
            return False
        else:
            print "You were able to walk for 60 minutes."
            print "Stat changes:"
            #Intelligence loss at 0.01 per hour down to 0
            regen(intelligence, 0.4*intelligencemax[0], 0.001, "Intelligence", "walking")
            regen(constitution, .25*constitutionmax[0], 0.005, "Constitution", "walking")
            decay(impulsivity, 20, 0.01, "Impulsivity", "walking")
            decay(stamina, 0, 30.0/constitution[0], "Stamina", "walking")
            return True
    else:
        print "You were tempted and so did not walk"
        temptedactivity()

def go(): #done
    global attention
    global attentionmax
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    global intelligencemax
    global attractiveness,luck
    print "Trying to go out"
    if rolltempted(0.1, attention[0], attentionmax[0]) == False:
        if (attention[0]*attractiveness[0] < 30):
            print "Not enough attention"
            return False
        else:
            print "You were able to go out to try to make new connections."
            ran = randint(30,100)
            if ran <= attractiveness[0]:
                print "You were able to make new connections. Your skill increased by 10% as a result."
                regen(skill, 999999999, skill[0]*0.1, "Skill", "going out")
                decay(attention, 0, 30.0/attractiveness[0], "Attention", "going out")
                win = randint(1,7)
                if win == 7:
                    print "You asked a girl out"
                    x = 0
                    for i in range(minus(99,luck[0])):
                        x = randint(0,9)
                        if x == 0:
                            print "She rejected"
                            return True
                    print "She accepted"
                    girlfriend[0] = True
            else:
                print "Due to low attractiveness, you were unable to make new connections"
                decay(attention, 0, 30.0/attractiveness[0], "Attention", "going out")
                regen(luck,100,1,"Luck","Getting rejected")
                if ran > willpower[0]:
                    print "As a result of not being able to make new connections, you became sad and harmed yourself"
                    decay(constitution, 0, 30.0/attractiveness[0], "Constitution", "going out")
            return True
    else:
        print "You were tempted and so did not go out"
        temptedactivity()


def showconcepts(): #need to edit this
    global concepts
    print "Concepts available to learn:"
    for i in concepts:
        print "Concept: " + i + ". Amount left to learn: " + str(round(concepts[i],2))

def temptedactivity(minutes=60, printstat=True):
    global impulsivity
    global willpower
    w = 1
    k = impulsivity[0] - willpower[0]
    for i in xrange(100):
        p = randint(0, int(k))
        if(p == 0):
            break
        else:
            w += 1
    if w <= 3:
        surf(minutes, printstat)
    else:
        play(minutes, printstat)

def passtime(damages = 1):
    global time
    global day
    global hourswithoutsleep
    global sleepdeprived
    global sleepdeprivationthreshold
    if (time[0] + damages) >= 24:
        time[0] = (time[0]+damages) % 24
        newday()
    else:
        time[0] += damages
    hourswithoutsleep += damages
    sleepdeprived = hourswithoutsleep > sleepdeprivationthreshold


def sleep(): #done
    global canfallasleep
    global attention
    global attentionmax
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    global time
    global day
    if time[0] < 9:
        sleeptime = 9 - time[0]
    elif time[0] > 16:
        sleeptime = 24 - time[0] + 8
    if time[0] > 16 or time[0] < 9:
        print "You were able to fall asleep and slept for " + str(sleeptime)
        if (time[0] > 20 or time[0] < 1):
            print "You slept at the right stage in your circadian cycle, therefore optimal sleep effects were achieved."
            sleepmodifier = 1
        else:
            print "You slept at the wrong stage in your circadian cycle, therefore optimal sleep effects were not achieved."
            sleepmodifier = 0.3
        flag = False
        while(time[0] + sleeptime >= 24):
            time[0] = (time[0] + sleeptime) % 24
            newday()
            flag = True
        if flag == False:
            time[0] += sleeptime
        print "Stat changes:"
        #Attention regen at 30 per hour up to 60% of max
        regen(attention, attentionmax[0], 30*sleeptime*sleepmodifier, "Attention", "sleeping")
        #Stamina regen at 12 per hour up to 100% of max
        regen(stamina, staminamax[0], 12*sleeptime*sleepmodifier, "Stamina", "sleeping")
        #Constitution regen at 0.3 per hour up to 25% of max
        regen(constitution, constitutionmax[0], 0.3*sleeptime*sleepmodifier, "Constitution", "sleeping")
    else:
        print "You were unable to fall asleep"

def progresstask(tasknum, amount):
    global tasks
    if tasks[tasknum][0] < amount:
        tasks.pop(tasknum)
        return True
    else:
        tasks[tasknum][0] = tasks[tasknum][0] - amount
        return False

def rolltemptedtask(day):
    global willpower
    p = randint(0,99)
    k = 100/day
    return k < (p / (1+minus(willpower[0],40)))

def practice():
    global attention
    global attentionmax
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    global impulsivity
    global skill
    global intelligence
    global willpower
    print "Tried to practice for 1 hour"
    if attention[0] == 0:
        print "You have 0 attention, you can't practice"
        return
    if rolltempted(0.2,attention[0], attentionmax[0]):
        print "You were tempted to not practice"
        temptedactivity()
    else:
        workminutes = 0
        for i in xrange(60):
            if attention[0] == 0:
                print "You ran out of attention"
                break
            else:
                decay(attention,0,5.0/(1+(1+skill[0])*(1.1**intelligence[0])),"Attention", "practicing", False)
                x = randint(0,int(minus(impulsivity[0], willpower[0]) / (1+intelligence[0] *(1 + skill[0]))))
                if x == 0:
                    workminutes += 1
        playminutes = 60-workminutes
        print "You spent " + str(workminutes) + " minutes on work and " + str(playminutes) + " on play."
        amount = workminutes*(1.2**(skill[0]%100))*(1.5**(minus(intelligence[0],50)))/60.0
        regen(skill,999,amount,"Skill","practicing")
        if playminutes > 0: temptedactivity(playminutes)

def dotask(tasknum):
    global tasks
    task = tasks[tasknum]
    global attention
    global attentionmax
    global stamina
    global staminamax
    global constitution
    global constitutionmax
    global impulsivity
    global skill
    global intelligence
    global willpower
    print "Tried to do the task for 1 hour"
    if attention[0] == 0:
        print "You have 0 attention, you can't do the task"
        return
    if rolltemptedtask(task[1]):
        print "Since there were still " + str(task[1]) + " days until the deadline, you put off doing the task."
        temptedactivity()
    else:
        workminutes = 0
        playminutes = 0
        for i in xrange(60):
            if attention[0] == 0:
                print "You ran out of attention"
                break
            else:
                decay(attention,0,5.0/(1+(1+skill[0])*(1.1**intelligence[0])),"Attention", "doing tasks", False)
                x = randint(0,int(minus(impulsivity[0], willpower[0]) / (1+intelligence[0] *(1 + skill[0]))))
                if x == 0:
                    amount = (1.2**skill[0])*(1.5**(minus(intelligence[0],50)))/60.0
                    if (progresstask(tasknum, amount)):
                        print "Task " + task[2] + " finished."
                        break
                    workminutes += 1
                else:
                    temptedactivity(1, False)
                    playminutes += 1
        print "You spent " + str(workminutes) + " minutes on work and " + str(playminutes) + " on play."
        minutesleft = 60 - workminutes - playminutes
        if minutesleft > 0: temptedactivity(minutesleft)
    passtime()

days = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def decrementtasks(): #done
    global tasks
    for task in tasks:
        task[1] -= 1


def checktasks(): #done
    global tasks
    newtasks = []
    for task in tasks:
        if task[1] > 0:
            newtasks.append(task)
        else:
            punish()
    tasks = newtasks

def punish(): #done
    global constitution
    global lives
    punishment = randint(0,9)
    if punishment < 9:
        print "Because you failed to complete a task, you were punished."
        damage = randint(0,25)
        decay(constitution,0,damage,"Constitution","punishment")
        if constitution[0] == 0:
            print "You died as a result of punishment"
            exit(1)
    else:
        roll = randint(0,2)
        if roll < 2:
            print "Lucky, you got away scot free!"
        else:
            if lives[0] == 0:
                print "This time you were not able to get away with it"
                print "You died"
                exit(1)
            else:
                print "This time you avoided punishment, but next time you may not be so lucky..."
                lives[0] -= 1

def newday(): #done
    global day
    global year
    day[0] += 1
    if day[0] == 365:
        day[0] = 1
        year[0] += 1
        print "It is a new year!"
    decrementtasks()
    checktasks()
    generatetasks()
    showInfo()
    if girlfriend[0] == True:
        print "You spent some time with your girlfriend"
        regen(happiness,9999999999,1,"Happiness","spending time")
        passtime()

def rolldeath():
    global year
    k = 300
    if year > 50:
        k = randint(150,300)
        if k < year*3:
            print "Unlucky, you died of old age"
            exit(1)
        else:
            print "Lucky. You are not old enough to die yet."

def roll():#done
    print "rollin..."
    k = randint(0,100)
    if k == 100:
        print "Boom! Jackpot"
        m = randint(0,4)
        if m == 0:
            regen(intelligencemax, 100, 100, "Max intelligence", "Godly Luck")
            regen(intelligence, 100, 50, "Intelligence", "Godly Luck")
        elif m == 1:
            regen(willpower, 100, 90, "Willpower", "Godly Luck")
        elif m == 2:
            regen(skill, 10, 10, "Skill", "Godly Luck")
        elif m == 3:
            decay(impulsivity, 0, 300, "Impulsivity", "Godly Luck")
        elif m == 4:
            regen(staminamax, 100, 100, "Max stamina", "Godly Luck")
            regen(stamina, 100, 50, "Stamina", "Godly Luck")
            regen(constitutionmax, 100, 100, "Max constitution", "Godly Luck")
            regen(constitution, 100, 50, "Constitution", "Godly Luck")
            regen(attentionmax, 100, 100, "Max attention", "Godly Luck")
            regen(attention, 100, 50, "Attention", "Godly Luck")
    elif k >= 80:
        print "You found someone who taught you some cool stuff. Intelligence increased by 10."
        regen(intelligence,100,10,"Intelligence", "Good luck")
        regen(intelligencemax,100,10,"Max intelligence","Good luck")
    elif k < 80:
        print "Bad luck."
        decay(attention, 0, randint(0,10), "Attention", "Bad luck")
        decay(stamina, 0, randint(0,10), "Stamina", "Bad luck")
        decay(constitution, 0, randint(0,10), "Constitution", "Bad luck")
        regen(impulsivity, 500, randint(0,10), "Impulsivity", "Bad luck")
        regen(luck,100,1,"Luck","Getting rejected")
    else:
        print "Nothing good or bad happened."

def usepower():
    if(constitution[0] > 1):
        c = (constitution[0]-1)*luck[0]
        decay(constitution,1,c,"Constitution","Power")
        regen(willpower,100,c/2,"Willpower","Power")
        regen(skill,999999999,c/2,"Skill","Power")
        regen(power,9999,c,"Power","Power")
    else:
        print "Not enough constitution"

def printscore():
    score = power[0] * skill[0] * luck[0]
    if girlfriend[0] == True:
        score = score
    else:
        print "You ended the game without a girlfriend, which lowered your score."
        score = math.log10(score)
    print "Your final score was: " + str(score)

def progressconcept(concept,amount):
    if concepts[concept] <= amount:
        print "Finished learning " + concept
        result = 60*(1 - concepts[concept]/amount)
        concepts.pop(concept)
        regen(luck,100,5,"Luck","learning")
    else:
        print "Learned some things about "+concept
        print "Concept " + concept + ": " + str(concepts[concept]) + " -> " + str(concepts[concept] - amount)
        concepts[concept] -= amount
        result = 0
    regen(skill,999999999,amount/10.0,"Skill","learning")
    regen(intelligence,100,amount/30.0,"Intelligence","learning")
    return result


def learn(concept): #Increases skill and intelligence during learning, gives luck at end
    print "Trying to learn "+concept
    if rolltempted(0.2,attention[0], attentionmax[0]):
        print "You were tempted to not learn"
        temptedactivity()
    else:
        if (attention[0] == 0):
            print "You cannot learn when attention is 0"
        else:
            amount = min(attention[0],60)*(1.2**(minus(intelligence[0],30)))*(1.1**(minus(skill[0],10)))/60.0
            result = progressconcept(concept,amount)
            if result>0:
                temptedactivity(result)
    passtime()

def main():
    global time, day, days, year ,tasks,concepts,willpower,skill,constitution,luck
    hasflag = False
    winflag = False
    showInfo()
    while True:
        showTime()
        showWork()
        if (constitution[0] == 0 ):
            print "You died"
            exit(1)
        if (time[0] == 24):
            time[0] = 0
            newday()
            # print "It's a new day!"
            # print "Today is "+ days[weekday]
        if ((luck[0] >= 50 or skill[0] >= 500) and hasflag == False):
            hasflag = True
            print "Power enabled. Type 'Use' or 'u' to use power."
        if (power[0] > 500 and winflag == False):
            winflag = True
            print "You have gained enough power to enter higher dimensions."
            print "Type 'win' to win the game."
        userinput = raw_input("Please enter your command")
        if userinput[0:2] in ['Do', 'do'] or userinput[0:1] == 'd': #Done
            if userinput[0:2] in ['Do', 'do']:
                num = userinput[2:]
            elif userinput[0:1] == 'd':
                num = userinput[1:]
            try:
                kek = int(num)
                if kek < len(tasks):
                    dotask(kek)
                else:
                    print "No such task exists"
            except Exception, e:
                print "You did not enter a number" + str(e)
        elif userinput[0:6] in ["Learn ", "learn "] or userinput[0:2] == "l ":
            if userinput[0:6] in ["Learn ", "learn "]:
                concept = userinput[6:]
            elif userinput[0:2] == "l ":
                concept = userinput[2:]
            if concept in concepts:
                learn(concept)
            else:
                print "No such concept exists"
        elif (userinput in ["Sleep", "sleep", "sl"]): #Functional
            sleep()
        elif (userinput in ["Help", "help", "h"]): #Functional
            printhelp()
        elif (userinput in ["Exit", "exit", "e"]): #Functional
            break
        elif (userinput in ["Play", "play", "p"]): #done
            play()
            passtime()
        elif (userinput in ["Surf", "surf", "s"]): #done
            surf()
            passtime()
        elif (userinput in ["Walk", "walk", "w"]): #done
            if (walk()):
                passtime()
        elif (userinput in ["Go", "go", "g"]): #done
            if (go()):
                passtime()
        elif (userinput in ["Meditate", "meditate", "m"]): #done
            meditate()
            passtime()
        elif (userinput in ["Practice", "practice", "pr"]): #done
            practice()
            passtime()
        elif (userinput in ["Exercise", "exercise", "ex"]): #done
            exercise()
            passtime()
        elif (userinput in ["Concepts", "concepts", "c"]): #Functional
            showconcepts()
        elif (userinput in ["Stats", "stats", "st"]): #Functional
            showStats()
        elif (userinput == "nd"): #done
            newday()
        elif (userinput == "cheat"): #done
            intelligence[0] = 30
            attention[0] = 30
            attentionmax[0] = 30
            willpower[0] = 30
            attractiveness[0] = 30
        elif (userinput == "suicide"): #done
            print "Harsh, dude!"
            exit(1)
        elif userinput in ["Roll", "roll", "r"]: #done
            roll()
        elif (hasflag == True and userinput in ["Use", "use", "u"]):
            usepower() #Do work at cost of losing some constitution, one point of constitution does skill points of work.
        elif (winflag and userinput == "win"):
            print "You win the game!"
            printscore()
        else:
            print "Invalid command."
    printScore()

start()