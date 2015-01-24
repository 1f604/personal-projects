#created on 24th January 2015
#You need to have pygame and python 2.7 to run this
import string
import math
import pygame
import random
import time
import copy
from pygame.locals import *
from random import randint

lst = []

WINDOWWIDTH = 800  # size of window's width in pixels
WINDOWHEIGHT = 600  # size of windows' height in pixels
FPS = 30  # frames per second, the general speed of the program
BOX_WIDTH = 60  # size of box width in pixels
BOX_HEIGHT = 80 # size of box height in pixels
GAPSIZE = 20  # size of gap between boxes in pixels
lose_flag = False

BLACK = (0, 0, 0)
GRAY = (170, 170, 170)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

BACK_GROUND_COLOR = NAVYBLUE

colors = (RED, GREEN, BLUE, YELLOW)

FONTSIZE = 36
FONTSPACE = 4

def add_to_list(str):
    global lst
    lst.append(str)

def printhelp():
    add_to_list("Help (h):")
    add_to_list("Stats in green text are consumable stats (i.e used up by doing things)")
    add_to_list("Do [Task] (d [Task]): Does the task specified by number. Example usage: Do 0")
    add_to_list("Play (p): Play a video game")
    add_to_list("Surf (s): Surf the internet or surf TV channels") #regenerates stamina
    add_to_list("Walk (w): Go out for a walk") #have a walk
    add_to_list("Go (g): Go out to make new connections (and possibly get a girlfriend)")
    add_to_list("Roll (r): Do something random and hope something good happens")
    add_to_list("Meditate (m): Meditate for up to 1 hour") #reduces impulsivity
    add_to_list("Practice (pr): Practice solving problems for up to 1 hour") #practice maths, increases intelligence and skill
    add_to_list("Exercise (ex): Exercise for up to 1 hour") #increases intelligence, constitution and stamina
    add_to_list("Concepts (c): Display concepts")
    add_to_list("Learn [concept] (l [concept]): Try to learn a concept for up to 1 hour. Example usage: Learn parity") #increases stats massively during learning
    add_to_list("Sleep (sl): Makes you sleep.")
    add_to_list("nd: Skips to the next day.")
    add_to_list("Stats (st): Shows stats")
    add_to_list("Exit (e): Exits the game without saving")
    add_to_list("Once your luck or skill reaches a certain level, you will unlock a special power that will enable you to win the game")

def showWork():
    if tasks != []:
        add_to_list("Tasks to do:")
        for i in range(len(tasks)):
            add_to_list(str(i) + ". " + tasks[i][2] + str(". Amount remaining: " + str(tasks[i][0]) + ". Time remaining: "+ str(tasks[i][1]) + " days"))
    else:
        add_to_list("There are no tasks to do.")

def minus (max, i):
    result = max - i
    if result >= 0:
        return result
    else:
        return 0

def rollstat(type):
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
        add_to_list("You rolled " + str(i[0]) + "/100 in " + str(i[1]))


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
    list = ["finite state machine", "memoization", "shors algorithm", "linear programming", "convex optimization","denotational semantics", "recursion", "parity", "regular expression", "boolean algebra", "lexing", "parsing", "string matching", "caching", "iteration", "pointers", "hashtables", "sorting", "context free grammar", "context sensitive grammar", "turing machines","computability", "sets", "infinite state machine", "trees", "graphs", "computational complexity", "databases", "compilers", "operating systems", "propositional logic", "predicate logic", "2nd order logic", "cellular automata", "finite state machines", "searching", "dimensions", "probability", "induction", "pigeonhole principle", "bayes law", "benfords law"] #list of random shit
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
time1 = [5]; #wake up at 5am, there are 24 hours in a day
cap = 365;
ondrugs = False;
sleepdeprived = False;
sleepdeprivationthreshold = 16; #How many hours without sleep before you go sleep deprived
hourswithoutsleep = 0; #start with a sleep debt of 0. As sleep debt increases your other stats go down. When your stats drop to a certain level you will die. when sleep debt exceeds some amount you will start to automatically fall asleep unless you take drugs.
canfallasleep = True #Can he fall sleep? Insomnia, drugs, stress and other conditions prevent this.
sleeptime = 8; #How long the person will sleep for the next time he falls asleep.
ill = False;
attention = [0]; #How much attention you can currently spare. Depleted by doing tasks and replenished by rest. If attention goes to 0 you fall asleep until it reaches 50%. Attention is normally at 60%. Increased by exercise and stress to 80%. Drugs can raise your attention to 100%.
attentionmax = [0]; #How much attentional capacity you have. Cannot be improved by anything, but illnesses, injury, drugs etc will decrease it.
constitution = [0]; #How good your body is. Reduced by lack of exercise, illness, injuries, overwork, and lots of other factors. Can raise constitution to max by using steroids.
constitutionmax = [0]; #How good your body could be, based on genetics. Serious illnesses and injuries will reduce this. Also affected by age.
willpower = [0]; #How much willpower you have. Can be reduced by brain damage, drugs, and other factors. Cannot be increased.
impulsivity = [100]; #How impulsive you are. Can be increased by brain damage, drugs and other factors. Can be decreased by drugs and surgery as well.
stamina = [0]; #How much more physical energy you have. Physical tasks drain more stamina than things like video games. Replenished to 70% max by resting for enough time. Deep sleep can restore it to 100%.
staminamax = [0]; #How much max stamina you can have. Affected by constitution, illnesses and various other factors.
attractiveness = [0]; #How attractive you are. Affected by constitution, injuries, plastic surgery, makeup, age and many other factors.
intelligence = [0]; #how fast you gain knowledge and skills. The higher your intelligence, the more knowledge and skill you gain from doing a task. Can be increased by education.
intelligencemax = [0]; #The cap on your intelligence. You cannot gain more intelligence than the cap, which is genetic and can be reduced by many factors but cannot be increased in any way.
skill = [0]; #How skilled you are. Has no cap but gain is based on intelligence.
#99% of the comments above were not implemented in the game, lol.
stats = [[impulsivity, "Impulsivity"], [willpower, "Willpower"], [attentionmax, "Maximum attention"], [constitutionmax, "Maximum constitution"], [staminamax, "Maximum stamina"], [intelligencemax, "Maximum intelligence"], [attractiveness, "Attractiveness"]]
currentstats = [[skill, "Skill"], [impulsivity, "Impulsivity"], [willpower, "Willpower"],  [attention, "Attention"],[attentionmax, "Maximum attention"], [constitution, "Constitution"], [constitutionmax, "Maximum constitution"], [stamina, "Stamina"],[staminamax, "Maximum stamina"], [attractiveness, "Attractiveness"], [intelligence, "Intelligence"]]
lives = [3]
girlfriend = [False]
happiness = [0]

def showStats():
    for i in currentstats:
        if i[1] != "Skill":
            add_to_list(i[1] + ": " + str(round(i[0][0], 1))+"/100")
        else:
            add_to_list(i[1] + ": " + str(round(i[0][0], 1)))

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
        add_to_list("It is currently termtime. Holiday begins at day " + str(getnextdate(day[0],termtime)))
    else:
        add_to_list("It is currently holidays. Term begins at " + str(getnextdate(day[0],termtime)))

def showTime():
    global termtime
    add_to_list("Current status: Year "+ str(year[0]) + " Day "+ str(day[0])+" "+ days[day[0]%7] + ". Time: "+str(time1))


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
    roll = randint(0,10) #Decide whether to return a regular number or something weird
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
    timeleft = int(rolltimeleft(effort)*6 / 1.2 ** hardness + 2) #time decreases exponentially with your age.
    tasks.append([round(effort,2),timeleft,generatetaskname()])


def generatetasks():
    global tasks
    global termtime
    global day
    add_to_list("It's a new day!")
    if day[0]%7 in [6,7] or day[0] not in termtime:
        add_to_list("It is a free day. You did not go to school today.")
    else:
        add_to_list("You went to school today.")
        numtasks = rolltasks()
        add_to_list("Number of tasks assigned: "+ str(numtasks))
        for i in xrange(numtasks):
            generatetask()

def start():
    add_to_list("Welcome to the student game!")
    add_to_list("To do well in this game, you need both luck and good judgment!")
    add_to_list("Type 'Help' for help")
    rollstats()
    printstats()

def regen(stat, stat_max, regen_rate, statname, method, printstat = True):
    if stat[0] < stat_max:
        oldstat = stat[0]
        if stat[0] < stat_max - regen_rate:
            stat[0] += regen_rate
        else:
            stat[0] = stat_max
        if printstat: add_to_list(statname + ": " + str(round(oldstat,2)) + " -> " + str(round(stat[0],2)))
    else:
        if printstat: add_to_list(statname + " was unchanged because it was already at the highest level achievable by " + method +".")

def decay(stat, limit, decay_rate, statname, method, printstat = True):
    if stat[0] > limit:
        oldstat = stat[0]
        if stat[0] > limit + decay_rate:
            stat[0] -= decay_rate
        else:
            stat[0] = limit
        if printstat: add_to_list(statname + ": " + str(round(oldstat,2)) + " -> " + str(round(stat[0],2)))
    else:
        if printstat: add_to_list(statname + " was unchanged because it was already at the lowest level achievable by " + method +".")

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
    add_to_list("Tried to meditate for 1 hour")
    if (rolltempted(0.3, attention[0], attentionmax[0]) == False and attention[0] > 0):
        if attention[0] > 60 and willpower[0] > impulsivity[0]:
            add_to_list("You were able to meditate for the entire hour")
            add_to_list("Stat changes:")
            #Attention regen at 12 per hour up to 60% of max
            decay(attention, 0, 60, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*willpower[0], "Impulsivity", "meditation")
        elif willpower[0] > impulsivity[0]:
            add_to_list("You only had enough attention to meditate for " +str(duration) + " hours")
            add_to_list("Stat changes:")
            duration = 60 - attention[0]
            decay(attention, 0, 60, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*(duration/60.0)*willpower[0], "Impulsivity", "meditation")
            add_to_list("You then went off to do another activity:")
            temptedactivity(60-duration)
        else:
            length = rolltime(0.1) #0.1 is a good value
            duration = min([attention[0], length])
            add_to_list("You meditated for " +str(duration) + " minutes before you got bored/ran out of attention.")
            add_to_list("Stat changes:")
            #Attention regen at 12 per hour up to 60% of max
            decay(attention, 0, duration, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*(duration/60.0)*willpower[0], "Impulsivity", "meditation")
            chance = randint(0,5)
            if chance == 5:
                regen(luck,100,1,"Luck","Meditation")
            add_to_list("You then went off to do another activity:")
            temptedactivity(60-duration)
    else:
        add_to_list("You were either tempted to not meditate or you had 0 attention.")
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
    add_to_list("Tried to meditate for 1 hour")
    if (rolltempted(0.3, attention[0], attentionmax[0]) == False and attention[0] > 0):
        if attention[0] > 60 and willpower[0] > impulsivity[0]:
            add_to_list("You were able to meditate for the entire hour")
            add_to_list("Stat changes:")
            #Attention regen at 12 per hour up to 60% of max
            decay(attention, 0, 60, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*willpower[0], "Impulsivity", "meditation")
        elif willpower[0] > impulsivity[0]:
            add_to_list("You only had enough attention to meditate for " +str(duration) + " hours")
            add_to_list("Stat changes:")
            duration = 60 - attention[0]
            decay(attention, 0, 60, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*(duration/60.0)*willpower[0], "Impulsivity", "meditation")
            add_to_list("You then went off to do another activity:")
            temptedactivity(60-duration)
        else:
            length = rolltime(0.1) #0.1 is a good value
            duration = min([attention[0], length])
            add_to_list("You meditated for " +str(duration) + " minutes before you got bored/ran out of attention.")
            add_to_list("Stat changes:")
            #Attention regen at 12 per hour up to 60% of max
            decay(attention, 0, duration, "Attention", "meditation")
            #Intelligence loss at 0.01 per hour down to 0
            decay(impulsivity, 10, 0.001*(duration/60.0)*willpower[0], "Impulsivity", "meditation")
            add_to_list("You then went off to do another activity:")
            temptedactivity(60-duration)
    else:
        add_to_list("You were either tempted to not meditate or you had 0 attention.")
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
    add_to_list("Tried to exercise for 1 hour")
    if (rolltempted(0.2, stamina[0], staminamax[0]) == False and attention[0] > 0):
        duration = stamina[0]
        add_to_list("You had enough stamina to exercise for " +str(duration) + " minutes")
        add_to_list("Stat changes:")
        decay(stamina, 0, 60, "Stamina", "exercise")
        #Intelligence loss at 0.01 per hour down to 0
        regen(staminamax, 100, 0.1*(duration/60.0), "Max stamina", "exercise")
        regen(constitution, 100, 2*(duration/60.0), "Constitution", "exercise")
        regen(constitutionmax, 100, 0.1*(duration/60.0), "Max constitution", "exercise")
        if (duration < 60):
            add_to_list("You then went off to do another activity:")
            temptedactivity(60-duration)
    else:
        add_to_list("You were either tempted to not exercise or you had 0 stamina.")
        temptedactivity()

def cleanup(minutes):
    add_to_list("You ran out of attention and dozed off for " +str(minutes) + " minutes.")
        #Attention regen at 0.15 per minute up to 60% of max
    regen(attention, 0.6*attentionmax[0], 0.15*minutes, "Attention", "dozing off")
    #Stamina regen at 0.05 per minute per hour up to 100% of max
    regen(stamina, staminamax[0], 0.05*minutes, "Stamina", "dozing off")

def decayvidya(minutes, printstat = True):
    global stamina
    global staminamax
    global constitution
    global constitutionmax, lose_flag
    k = minutes / 60.0
    if stamina[0] < k:
        diff = k - stamina[0]
        decay(stamina, 0, 100, "Stamina", "playing", printstat)
        if (constitution[0] < diff/2.0):
            add_to_list("You died")
            lose_flag = True
            add_to_list("Press enter to exit")
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
    global time1
    duration = minutes
    #Impulsivity regen at 0.5 per h
    # our of playing
    if printstat == True:
        add_to_list("You played video games for " + str(duration) + " minutes.")
        add_to_list("Stat changes:")
    regen(impulsivity, 100, 0.5*(duration/60.0), "Impulsivity", "playing", printstat)
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
        add_to_list("Stat changes:")
        add_to_list("You surfed the internet for " + str(duration) + " minutes.")
    regen(impulsivity, 100, 0.12*(duration/60.0), "Impulsivity", "surfing", printstat)
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
    add_to_list("You ran out of stamina while surfing the internet, so you dozed off for "+str(minutes)+" minutes.")
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
    add_to_list("Trying to walk")
    if rolltempted(0.1, stamina[0], staminamax[0]) == False:
        if (stamina[0]*constitution[0] < 30):
            add_to_list("Not enough stamina")
            return False
        else:
            add_to_list("You were able to walk for 60 minutes.")
            add_to_list("Stat changes:")
            #Intelligence loss at 0.01 per hour down to 0
            regen(intelligence, 0.4*intelligencemax[0], 0.001, "Intelligence", "walking")
            regen(constitution, .25*constitutionmax[0], 0.005, "Constitution", "walking")
            decay(impulsivity, 20, 0.01, "Impulsivity", "walking")
            decay(stamina, 0, 30.0/constitution[0], "Stamina", "walking")
            return True
    else:
        add_to_list("You were tempted and so did not walk")
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
    if girlfriend[0] == False: add_to_list("Trying to go out")
    else: add_to_list("You went out with your girlfriend")
    if rolltempted(0.1, attention[0], attentionmax[0]) == False:
        if (attention[0]*attractiveness[0] < 30):
            add_to_list("Not enough attention")
            return False
        else:
            add_to_list("You were able to go out to try to make new connections.")
            ran = randint(30,100)
            if ran <= attractiveness[0]:
                add_to_list("You were able to make new connections. Your skill increased by 10% as a result.")
                regen(skill, 999999999, skill[0]*0.1, "Skill", "going out")
                decay(attention, 0, 30.0/attractiveness[0], "Attention", "going out")
                win = randint(1,7)
                if win == 7:
                    add_to_list("You asked a girl out")
                    x = 0
                    for i in range(minus(99,luck[0])):
                        x = randint(0,2)
                        if x == 0:
                            add_to_list("She rejected you")
                            return True
                    add_to_list("She accepted")
                    girlfriend[0] = True
            else:
                add_to_list("Due to low attractiveness, you were unable to make new connections")
                decay(attention, 0, 30.0/attractiveness[0], "Attention", "going out")
                regen(luck,100,1,"Luck","Getting rejected")
                if ran > willpower[0]:
                    add_to_list("As a result of not being able to make new connections, you became sad and harmed yourself")
                    decay(constitution, 0, 30.0/attractiveness[0], "Constitution", "going out")
            return True
    else:
        add_to_list("You were tempted and so did not go out")
        temptedactivity()
        passtime()


def showconcepts(): #need to edit this
    global concepts
    add_to_list("Concepts available to learn:")
    for i in concepts:
        add_to_list("Concept: " + i + ". Amount left to learn: " + str(round(concepts[i],2)))

def temptedactivity(minutes=60, printstat=True):
    global impulsivity
    global willpower
    w = 1
    k = impulsivity[0] - willpower[0]
    if k <= 0:
        play(minutes, printstat)
    else:
        for i in xrange(100):
            p = randint(0, int(abs(k)))
            if(p == 0):
                break
            else:
                w += 1
        if w <= 3:
            surf(minutes, printstat)
        else:
            play(minutes, printstat)


def passtime(damages = 1):
    global time1
    global day
    global hourswithoutsleep
    global sleepdeprived
    global sleepdeprivationthreshold
    if (time1[0] + damages) >= 24:
        time1[0] = (time1[0]+damages) % 24
        newday()
    else:
        time1[0] += damages
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
    global time1
    global day
    if time1[0] < 9:
        sleeptime = 9 - time1[0]
    elif time1[0] > 16:
        sleeptime = 24 - time1[0] + 8
    if time1[0] > 16 or time1[0] < 9:
        add_to_list("You were able to fall asleep and slept for " + str(sleeptime))
        if (time1[0] > 20 or time1[0] < 1):
            add_to_list("You slept at the right stage in your circadian cycle, therefore optimal sleep effects were achieved.")
            sleepmodifier = 1
        else:
            add_to_list("You slept at the wrong stage in your circadian cycle, therefore optimal sleep effects were not achieved.")
            sleepmodifier = 0.3
        flag = False
        while(time1[0] + sleeptime >= 24):
            time1[0] = (time1[0] + sleeptime) % 24
            newday()
            flag = True
        if flag == False:
            time1[0] += sleeptime
        add_to_list("Stat changes:")
        #Attention regen at 30 per hour up to 60% of max
        regen(attention, attentionmax[0], 30*sleeptime*sleepmodifier, "Attention", "sleeping")
        #Stamina regen at 12 per hour up to 100% of max
        regen(stamina, staminamax[0], 12*sleeptime*sleepmodifier, "Stamina", "sleeping")
        #Constitution regen at 0.3 per hour up to 25% of max
        regen(constitution, constitutionmax[0], 5*sleeptime*sleepmodifier, "Constitution", "sleeping")
    else:
        add_to_list("You were unable to fall asleep")

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
    add_to_list("Tried to practice for 1 hour")
    if attention[0] == 0:
        add_to_list("You have 0 attention, you can't practice")
        return
    if rolltempted(0.2,attention[0], attentionmax[0]):
        add_to_list("You were tempted to not practice")
        temptedactivity()
    else:
        workminutes = 0
        for i in xrange(60):
            if attention[0] == 0:
                add_to_list("You ran out of attention")
                break
            else:
                decay(attention,0,5.0/(1+(1+skill[0])*(1.1**intelligence[0])),"Attention", "practicing", False)
                x = randint(0,int(minus(impulsivity[0], willpower[0]) / (1+intelligence[0] *(1 + skill[0]))))
                if x == 0:
                    workminutes += 1
        playminutes = 60-workminutes
        add_to_list("You spent " + str(workminutes) + " minutes on work and " + str(playminutes) + " on play.")
        amount = workminutes*(1.2**min([(skill[0]%100),30]))*(1.5**min([(minus(intelligence[0],50)),30]))/60.0
        regen(skill,999,amount,"Skill","practicing")
        if playminutes > 0: temptedactivity(playminutes)
    passtime()

def dotask(tasknum):
    global tasks
    task = tasks[tasknum]
    #print task
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
    add_to_list("Tried to do the task for 1 hour")
    if attention[0] == 0:
        add_to_list("You have 0 attention, you can't do the task")
        return
    if rolltemptedtask(task[1]):
        add_to_list("Since there were still " + str(task[1]) + " days until the deadline, you put off doing the task.")
        temptedactivity()
    else:
        workminutes = 0
        playminutes = 0
        for i in xrange(60):
            if attention[0] == 0:
                add_to_list("You ran out of attention")
                break
            else:
                decay(attention,0,5.0/(1+(1+skill[0])*(1.1**min([intelligence[0],30]))),"Attention", "doing tasks", False)
                x = randint(0,int(minus(impulsivity[0], willpower[0]) / (1+intelligence[0] *(1 + skill[0]))))
                if x == 0:
                    amount = (1.2**min([skill[0],30]))*(1.5**min([(minus(intelligence[0],50)),30]))/60.0
                    if (progresstask(tasknum, amount)):
                        add_to_list("Task " + task[2] + " finished.")
                        break
                    workminutes += 1
                else:
                    temptedactivity(1, False)
                    playminutes += 1
        add_to_list("You spent " + str(workminutes) + " minutes on work and " + str(playminutes) + " on play.")
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
    global lives,lose_flag
    punishment = randint(0,9)
    if punishment < 9:
        add_to_list("Because you failed to complete a task, you were punished.")
        damage = randint(0,25)
        decay(constitution,0,damage,"Constitution","punishment")
        if constitution[0] == 0:
            add_to_list("You died as a result of punishment")
            add_to_list("Press enter to exit")
            lose_flag = True
    else:
        roll = randint(0,2)
        if roll < 2:
            add_to_list("Lucky, you got away scot free!")
        else:
            if lives[0] == 0:
                add_to_list("This time you were not able to get away with it")
                add_to_list("You died")
                add_to_list("Press enter to exit")
                lose_flag = True
            else:
                add_to_list("This time you avoided punishment, but next time you may not be so lucky...")
                lives[0] -= 1

def newday(): #done
    global day
    global year
    day[0] += 1
    if day[0] == 365:
        day[0] = 1
        year[0] += 1
        add_to_list("It is a new year!")
    decrementtasks()
    checktasks()
    generatetasks()
    showInfo()
    if girlfriend[0] == True:
        add_to_list("You spent some time with your girlfriend")
        regen(happiness,9999999999,1,"Happiness","spending time")
        passtime()

def rolldeath():
    global year, lose_flag
    k = 300
    if year > 50:
        k = randint(150,300)
        if k < year*3:
            add_to_list("Unlucky, you died of old age")
            add_to_list("Press enter to exit")
            lose_flag = True
        else:
            add_to_list("Lucky. You are not old enough to die yet.")

def roll():#done
    add_to_list("rollin...")
    k = randint(0,100)
    if k == 100:
        add_to_list("Boom! Jackpot")
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
        add_to_list("You found someone who taught you some cool stuff. Intelligence increased by 10.")
        regen(intelligence,100,10,"Intelligence", "Good luck")
        regen(intelligencemax,100,10,"Max intelligence","Good luck")
    elif k < 80:
        add_to_list("Bad luck.")
        decay(attention, 0, randint(0,10), "Attention", "Bad luck")
        decay(stamina, 0, randint(0,10), "Stamina", "Bad luck")
        decay(constitution, 0, randint(0,10), "Constitution", "Bad luck")
        regen(impulsivity, 100, randint(0,10), "Impulsivity", "Bad luck")
        regen(luck,100,1,"Luck","Bad luck, lol.")
    else:
        add_to_list("Nothing good or bad happened.")

def usepower():
    if(constitution[0] > 1):
        c = (constitution[0]-1)*luck[0]
        decay(constitution,1,c,"Constitution","Power")
        regen(willpower,100,c/2,"Willpower","Power")
        regen(skill,999999999,c/2,"Skill","Power")
        regen(power,9999,c,"Power","Power")
    else:
        add_to_list("Not enough constitution")

def printscore():
    score = power[0] * skill[0] * luck[0]
    if girlfriend[0] != True:
        add_to_list("You ended the game without a girlfriend, which lowered your score.")
        score = math.log10(score)
    add_to_list("Your final score was: " + str(score))
    add_to_list("Press enter to exit")
    return "lose"

def progressconcept(concept,amount):
    if concepts[concept] <= amount:
        add_to_list("Finished learning " + concept)
        result = 60*(1 - concepts[concept]/amount)
        concepts.pop(concept)
        regen(luck,100,5,"Luck","learning")
    else:
        add_to_list("Learned some things about "+concept)
        add_to_list("Concept " + concept + ": " + str(concepts[concept]) + " -> " + str(concepts[concept] - amount))
        concepts[concept] -= amount
        result = 0
    regen(skill,999999999,amount/10.0,"Skill","learning")
    regen(intelligence,100,amount/30.0,"Intelligence","learning")
    return result


def learn(concept): #Increases skill and intelligence during learning, gives luck at end
    add_to_list("Trying to learn "+concept)
    if rolltempted(0.2,attention[0], attentionmax[0]):
        add_to_list("You were tempted to not learn")
        temptedactivity()
    else:
        if (attention[0] == 0):
            add_to_list("You cannot learn when attention is 0")
        else:
            amount = min([attention[0],60])*(1.2**min([(minus(intelligence[0],30)),30]))*(1.1**min([(minus(skill[0],10)),30]))/60.0
            result = progressconcept(concept,amount)
            if result>0:
                temptedactivity(result)
    passtime()

hasflag = False
winflag = False

def main(userinput):
    global time1, day, days, year ,tasks,concepts,willpower,skill,constitution,luck,hasflag,winflag,lose_flag
    add_to_list("You entered: " + userinput)
    add_to_list("==========================================================================")
    if (constitution[0] == 0 ):
        add_to_list("You died")
        add_to_list("Press enter to exit")
        lose_flag= True
    if (time1[0] == 24):
        time1[0] = 0
        newday()
        # add_to_list("It's a new day!"
        # add_to_list("Today is "+ days[weekday]
    if ((luck[0] >= 50 or skill[0] >= 500) and hasflag == False):
        hasflag = True
        add_to_list("Power enabled. Type 'Use' or 'u' to use power.")
    if (power[0] > 500 and winflag == False):
        winflag = True
        add_to_list("You have gained enough power to enter higher dimensions.")
        add_to_list("Type 'win' to win the game.")
    if userinput[0:2] in ['Do', 'do'] or userinput[0:1] == 'd': #Done
        if userinput[0:2] in ['Do', 'do']:
            num = userinput[2:]
        elif userinput[0:1] == 'd':
            num = userinput[1:]
        try:
            kek = int(num)
            #print kek
            if kek < len(tasks):
                dotask(kek)
            else:
                add_to_list("No such task exists")
        except Exception, e:
            add_to_list("You did not enter a number (" + str(e) + ")")
    elif userinput[0:6] in ["Learn ", "learn "] or userinput[0:2] == "l ":
        if userinput[0:6] in ["Learn ", "learn "]:
            concept = userinput[6:]
        elif userinput[0:2] == "l ":
            concept = userinput[2:]
        if concept in concepts:
            learn(concept)
        else:
            add_to_list("No such concept exists")
    elif (userinput in ["Sleep", "sleep", "sl"]): #Functional
        sleep()
    elif (userinput in ["Help", "help", "h"]): #Functional
        printhelp()
    elif (userinput in ["Exit", "exit", "e"]): #Functional
        return "lose"
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
    elif (userinput in ["Exercise", "exercise", "ex"]): #done
        exercise()
        passtime()
    elif (userinput in ["Concepts", "concepts", "c"]): #Functional
        showconcepts()
    elif (userinput in ["Stats", "stats", "st"]): #Functional
        showStats()
    elif (userinput == "nd"): #done
        newday()
    elif (userinput == "ny"): #done
        year[0]+=1
    elif (userinput == "cheat"): #done
        intelligence[0] = 30
        attention[0] = 30
        attentionmax[0] = 30
        constitution[0] = 30
        willpower[0] = 30
        attractiveness[0] = 30
        staminamax[0] = 30
        constitutionmax[0] = 30
    elif (userinput == "suicide"): #done
        add_to_list("Harsh, dude!")
        exit(6)
    elif userinput in ["Roll", "roll", "r"]: #done
        roll()
    elif (hasflag == True and userinput in ["Use", "use", "u"]):
        usepower() #Do work at cost of losing some constitution, one point of constitution does skill points of work.
    elif (winflag and userinput == "win"):
        add_to_list("You win the game!")
        printscore()
        lose_flag = True
    else:
        add_to_list("Invalid command.")
    showTime()
    showWork()


class MenuItem(pygame.font.Font):
    selected = False

    def __init__(self, text, position, fontSize=FONTSIZE, anti_aliasing=True, color=WHITE):
        pygame.font.Font.__init__(self, None, fontSize)
        self.text = text
        self.anti_aliasing = anti_aliasing
        self.color = color
        self.surface = self.render(self.text, self.anti_aliasing, self.color)
        self.position = self.surface.get_rect(centerx=position[0], centery=position[1])

    def get_text(self):
        return self.text

    def get_position(self):
        return self.position

    def get_surface(self):
        return self.surface

    def set_color(self, color):
        self.color = color
        self.surface = self.render(self.text, self.anti_aliasing, self.color)

    def is_selected(self, (pos_x, pos_y)):
        position = self.position
        if position.left < pos_x < position.right and position.top < pos_y < position.bottom:
            return True
        return False


class Menu:
    def __init__(self, screen, menu_items):
        self.screen = screen

        # Calculate the height and start point of the menu
        # leave a space between each menu entry
        menu_height = (FONTSIZE + FONTSPACE) * len(menu_items)
        start_y = self.screen.get_height() / 2 - menu_height / 2

        self.menu_items = list()
        for menuItem in menu_items:
            center_x = self.screen.get_width() / 2
            center_y = start_y + FONTSIZE + FONTSPACE
            new_item = MenuItem(menuItem, (center_x, center_y), FONTSIZE)
            self.menu_items.append(new_item)
            start_y = start_y + FONTSIZE + FONTSPACE
            self.screen.blit(new_item.get_surface(), new_item.get_position())

    def draw_menu(self, background):
        self.screen.fill(background)
        for menu_item in self.menu_items:
            if menu_item.is_selected(pygame.mouse.get_pos()):
                menu_item.set_color(RED)
            else:
                menu_item.set_color(WHITE)
            self.screen.blit(menu_item.get_surface(), menu_item.get_position())

    def handle_event(self, event):
        if event.type == MOUSEBUTTONUP:
            for menu_item in self.menu_items:
                if menu_item.is_selected(pygame.mouse.get_pos()):
                    #Create customized event and post to pygame
                    menu_event = pygame.event.Event(USEREVENT, text=menu_item.get_text())
                    pygame.event.post(menu_event)

LINES_MAX = 21

def refreshbox():
  scrnwdth = screen.get_width()
  scrnheit = screen.get_height()
  pygame.draw.rect(screen, (0,0,0),
                   (50,
                    (scrnheit / 2) - 8,
                    scrnwdth-100,scrnheit/2 -26), 0)
  pygame.draw.rect(screen, (255,255,255),
                   (48,
                    (scrnheit / 2) - 10,
                    scrnwdth-98,scrnheit/2 -24), 1)
  #add_to_list("refreshed the screen"

def drawstatbars():
  scrnwdth = screen.get_width()
  scrnheit = screen.get_height()
  fontobject = pygame.font.Font(None,24)
  #add_to_list(fontobject.size(msg)
  list1 = ["Skill","Impulsivity", "Willpower","Attention","Max attention","Constitution","Max constitution","Stamina","Max stamina","Attractiveness","Intelligence"]
  list2 = ["Stamina","Attention"]
  list3 = ["Constitution"]
  ypos = 24
  for i in list1:
      if i in list2:
          screen.blit(fontobject.render(i, 1, GREEN),
                    (50, ypos))
      elif i in list3:
          screen.blit(fontobject.render(i, 1, RED),
                    (50, ypos))
      else:
          screen.blit(fontobject.render(i, 1, WHITE),
                    (50, ypos))
      ypos += 24
  ypos = 22
  for i in list1:
      pygame.draw.rect(screen, (255,255,255),
                       (208,
                        ypos,
                        scrnwdth-258,22), 1)
      ypos += 24
  #add_to_list("refreshed the screen"

def updatebars():
  global currentstats
  scrnwdth = screen.get_width()
  ypos = 24
  for i in xrange(11):
      pygame.draw.rect(screen, NAVYBLUE,
                       (210,
                        ypos,
                        scrnwdth-262,18), 0)
      ypos += 24
  ypos = 24
  list1 = ["Constitution"]
  list2 = ["Stamina", "Attention"]
  for i in currentstats:
      if i[1] in list1:
          pygame.draw.rect(screen, RED,
                           (210,
                            ypos,
                            (i[0][0] / 100.0) * (scrnwdth-262),18), 0)
      elif i[1] in list2:
          pygame.draw.rect(screen, GREEN,
                           (210,
                            ypos,
                            (i[0][0] / 100.0) * (scrnwdth-262),18), 0)
      else:
          pygame.draw.rect(screen, WHITE,
                           (210,
                            ypos,
                            (i[0][0] / 100.0) * (scrnwdth-262),18), 0)
      ypos += 24


def refreshtextbox():
  scrnwdth = screen.get_width()
  scrnheit = screen.get_height()
  pygame.draw.rect(screen, (0,0,0),
                   (50,
                    scrnheit - 28,
                    scrnwdth-100,17), 0)
  pygame.draw.rect(screen, (255,255,255),
                   (48,
                    scrnheit - 30,
                    scrnwdth-98,19), 1)
  #add_to_list("refreshed the screen"

def println(msg, cursor):
  fontobject = pygame.font.Font(None,18)
  #add_to_list(fontobject.size(msg)
  if len(msg) != 0:
    screen.blit(fontobject.render(msg, 1, (255,255,255)),
                (50, cursor))

def printtext(List,position):
    cursor = 553
    counter = LINES_MAX
    size = len(List)-1-position
    while(counter > 0 and size >= 0):
        println(List[size],cursor)
        cursor -= 13
        size-=1
        counter-=1
    #if size < 0:
    #    size = 0
    #    println(List[size],cursor)


def printletter(a,p):
    fontobject = pygame.font.Font(None,18)
  #add_to_list(fontobject.size(msg)
    if len(a) != 0:
        screen.blit(fontobject.render(a, 1, (255,255,255)),
                (52+p, 573))

class MemoryPuzzle():
    def __init__(self, screen):
        #pygame.mixer.music.load("Background.mid")
        #self.click_sound = pygame.mixer.Sound("Click.ogg")
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.screen.fill(BACK_GROUND_COLOR)




    def run(self):
#        pygame.mixer.music.play()
#        self.start_game_animation()


        has_won = False

        refreshbox()
        refreshtextbox()
        position = 0
        global lst
        flag = False
        upflag = False
        counter = 0
        p = 0
        userinput = ""
        start()
        printtext(lst,position)
        drawstatbars()
        updatebars()
        while not has_won:  # main game loop
            #Event handling loop
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    exit(0)
                #elif event.type == MOUSEBUTTONUP:
#                    self.click_sound.play()
                      #refreshbox()
                elif event.type == KEYDOWN and event.key == K_UP:
                    upflag = True
                elif event.type == KEYDOWN and event.key == K_DOWN:
                    flag = True
                elif event.type == KEYDOWN and event.key in range(48,58) + range(97,123)+[K_SPACE]:
                    fontobject = pygame.font.Font(None,18)
                    q = fontobject.size(chr(event.key))[0]
                    if p+q < 700:
                        printletter(chr(event.key),p)
                        p+=q
                        userinput += chr(event.key)
                elif event.type == KEYDOWN and event.key == K_BACKSPACE:
                    refreshtextbox()
                    userinput = ""
                    p = 0
                elif event.type == KEYDOWN and event.key == K_RETURN:
                    if (lose_flag):
                        exit(9)
                    if(main(userinput)=="lose"):
                        exit(99)
                    position = 0
                    p = 0
                    refreshbox()
                    refreshtextbox()
                    userinput = ""
                    printtext(lst,position)
                    updatebars()
                elif event.type == KEYUP:
                    flag = False
                    upflag = False
                    counter = 0

            if flag == True:
                if position > 0 and (counter > 10 or counter == 0):
                    position-=6
                    if(position<0):
                        position=0
                    refreshbox()
                    printtext(lst,position)
                time.sleep(1/100.0)
                counter += 1

            elif upflag == True:
                if position < len(lst) - LINES_MAX and (counter > 10 or counter == 0):
                    position+=6
                    if(position>len(lst) - LINES_MAX):
                        position=len(lst) - LINES_MAX
                    refreshbox()
                    printtext(lst,position)
                time.sleep(1/100.0)
                counter += 1


#            if not pygame.mixer.music.get_busy():
#                pygame.mixer.music.play()

            # Redraw the screen and wait a clock tick.
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    # pygame initialization
    global statboost
    pygame.init()
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('The Student Game')
    clock = pygame.time.Clock()

    menu_items = ("Easy Game", "Normal Game", "Quit")
    myMenu = Menu(screen, menu_items)
    #background = BLACK
    background = NAVYBLUE

    myMenu.draw_menu(background)

    while True:
        is_game_active = False
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                exit(0)
            elif event.type is USEREVENT:
                if event.text is menu_items[2]:
                    pygame.quit()
                    exit(0)
                elif event.text is menu_items[0]:
                    statboost = [["Maximum intelligence",45],["Willpower",45],["Attractiveness",45],["Maximum attention",45],["Maximum stamina",45],["Constitution",45]]
                    is_game_active = True
                elif event.text is menu_items[1]:
                    statboost = [["Maximum intelligence",14],["Willpower",12],["Attractiveness",12],["Maximum attention",25],["Maximum stamina",15],["Constitution",20]]
                    is_game_active = True
            else:
                myMenu.handle_event(event)

        if is_game_active:
            memoryPuzzle = MemoryPuzzle(screen)
            #Enter Game Loop
            memoryPuzzle.run()
            lose_flag = False

        myMenu.draw_menu(background)
        pygame.display.update()
        clock.tick(FPS)



start()