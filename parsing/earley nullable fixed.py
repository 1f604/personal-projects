#requires nltk installed for drawing parse trees
#Nullable fix from Practical Earley Parsing by Aycock & Horspool
#edit tokens and grammar to change the tokens being parsed and the grammar used
#Created on 18 September 2014
import itertools
from nltk.tree import *
from nltk.draw import tree
dp1 = Tree('dp', [Tree('d', ['the', 'cool']), Tree('np', ['dog'])])
dp2 = Tree('dp', [Tree('d', ['the']), Tree('np', ['cat'])])
vp = Tree('vp', [Tree('v', ['chased']), dp2])
sentence = Tree('s', [dp1, vp, dp1])
#print sentence
#sentence.draw()


def isterminal(item, grammar):
    for (key,value) in grammar:
        if key == item:
            return False
    return True

def containsterminals(rule, grammar):
    for item in rule:
        if isterminal(item, grammar):
            return True
    return False

def is_start(state, grammar):
    (x, ab, cd, j, bp, id) = state
    return (x, ab) == grammar[0] and cd == [] and j == 0

def flatten(dic):
    dic2 = {}
    for key in dic:
        for state in dic[key]:
            dic2[state[5]] = state
    return dic2

def isterminal(item, grammar):
    for (key,value) in grammar:
        if key == item:
            return False
    return True

def allterminals(lst, grammar):
    for item in lst:
        if not isterminal(item, grammar):
            return False
    return True

def expand(state, grammar, chart, nullable): #assume cd is empty
    res = []
    (x, ab, cd, j, bp, n) = state
##    print state
    if allterminals(ab, grammar):
##        print "allterminals"
##        print ab
        return [Tree(x, ab)]
    else:
        children = []
        count = 0
        for item in ab:
            if isterminal(item, grammar):
                children.append([item])
            else:
                if bp[count] != "NULL":
                    children.append(expand(chart[bp[count]], grammar, chart, nullable))
                else:
                    paths = nullpath(item, grammar, nullable, [])
                    children.append(paths)
                count += 1
        childlist = list(itertools.product(*children)) #each list in lst2 is a set of children of rule[1]
        for child in childlist:
            res.append(Tree(x, child))
        return res


count = 0

def is_not_in(state,lst): #compares a 5-tuple to a list of 6-tuples
    for (x,ab,cd,j,bp,n) in lst:
##        print "nnowtesting:"
##        print (x,ab,cd,j,bp)
##        print state
        if (x,ab,cd,j,bp) == state:
            return False
    return True

def addtochart(chart,queue,index,states): #adds a list of parsing states to chart
    global count
##    print queue
##    print states
    for state in states:
        print "state to be tested:"
        print state
        if is_not_in(state,chart[index]):
            count += 1
            chart[index] = chart[index] + [state+(count,)]
            print queue
            print "just appended something"
            queue.append(state+(count,))
            print queue

def scan(tokens, i, state):
    global count
    (x, ab, cd, j, bp, n) = state
    if (cd != [] and tokens[i] == cd[0]):
        if len(cd) > 1:
            count +=1
            return (x, ab+[cd[0]], cd[1:], j, bp, count)
        else:
            count +=1
            return (x, ab+[cd[0]], [], j,bp, count)
    return False

def predict(grammar,index, state, nullable): #returns a list of parsing states without ids. NEW PREDICTED STATES DO NOT HAVE BACK POINTERS!
    (x, ab, cd, j, bp, n) = state
    result = []
##    print "predicting"
##    print cd[0]
    for (key, value) in grammar:
        if key == cd[0] and value != []:
            result.append((key, [], value, index, []))
    if not isterminal(cd[0], grammar) and nullable[cd[0]]:
        result.append((x, ab+[cd[0]], cd[1:], j, bp+["NULL"]))
    return result

def complete(chart, i, state): #returns a list of parsing states
    (x, ab, cd, j, bp, n) = state
    answers = []
    for (sx, sab, scd, sj, sbp, sid) in chart[j]:
        if scd !=[] and scd[0] == x:
            if len(scd) > 1:
                answers.append((sx,sab+[x],scd[1:],sj, sbp + [n]))
            else:
                answers.append((sx,sab+[x],[],sj, sbp + [n]))
    return answers

def parse(tokens,grammar, nullable):
  tokens = tokens + ["end of input marker"]
  chart = {}
  for i in range(len(tokens)):  #initializing the chart with empty lists
    chart[i] = [ ]
  start_state = (grammar[0][0], [], grammar[0][1], 0, [], 0)
  chart[0] = [ start_state ] #seeding the chart with the start rule
  print chart

  for i in range(len(tokens)):
    queue = chart[i][:]
##    print "queue is:"
##    print queue
    while queue:
      current_state = queue.pop(0)
      if current_state[2] == []:
        addtochart(chart, queue, i, complete(chart,i,current_state))
      else:
        addtochart(chart, queue, i, predict(grammar,i,current_state, nullable))
##      print "queue is"
##      print queue
##      print "chart is"
##      print chart
    for state in chart[i]:
        outcome = scan(tokens, i, state)
        if outcome != False:
            chart[i+1].append(outcome)
##        print chart
  return chart


##grammar = [
##  ("TOP", ["S" ]) ,
##  ("S", ["NP", "VP" ]) ,
##  ("PP", ["P" , "NP" ]),
##  ("VP", ["V", "NP"]),
##  ("VP", ["VP", "PP"]),
##  ("P", ["with"]),
##  ("V", ["saw"]),
##  ("NP", ["NP", "PP"]),
##  ("NP", ["N"]),
##  ("N", ["astronomers"]),
##  ("N", ["ears"]),
##  ("N", ["stars"]),
##  ("N", ["telescopes"]),
###  ("P", ["(" , "S"]),
##]
##grammar = [
##  ("TOP", ["S" ]) ,
##  ("S", ["(", "S", ")" ]) ,
##  ("S", []),
###  ("P", ["(" , "S"]),
##]
grammar = [
  ("START", ["S" ]) ,
  ("S", ["A","A", "A", "A"]) ,
  ("A", ["a"]),
  ("A", ["E" ]) ,
##  ("A", [ ]) ,
  ("E", []),
#  ("P", ["(" , "S"]),
]
##grammar = [
##  ("START", ["S" ]) ,
##  ("S", ["S","+", "M"]) ,
##  ("S", ["M"]) ,
##  ("M", ["M","*","T"]) ,
##  ("M", ["T"]) ,
##  ("T", ["1"]) ,
##  ("T", ["2"]) ,
##  ("T", ["3"]) ,
##  ("T", ["4"]) ,
##]

nullable = {}
work = 0

def isnullable(item, grammar, nullable, visited):
    if item in nullable:
        return nullable[item]
    for rule in grammar:
        if rule[0] == item and rule not in visited:
            visited.append(rule)
            if isnull(rule, grammar, nullable, visited):
                nullable[item] = True
                return True
    nullable[item] = False
    return False

def isnull(rule, grammar, nullable, visited):
    global work
    work += 1
    if rule[1] == []:
        return True
    for item in rule[1]:
        if isnullable(item, grammar, nullable, visited) == False:
            return False
    return True

def buildnullable(nullable, grammar):
    for rule in grammar:
        if rule[0] not in nullable:
            isnullable(rule[0], grammar, nullable, [])

def allnull(tokens, nullable):
    for token in tokens:
        if token not in nullable or nullable[token] != True:
            return False
    return True

def nullpath(item, grammar, nullable, visited):
    results = []
    lst = []
    for rule in grammar:
        if rule[0] == item and rule not in visited:
            visited2 = visited[:]
            visited2.append(rule)
            if rule[1] == []:
                results.append(Tree(item, ["epsilon"]))
            elif allnull(rule[1], nullable):
                for token in rule[1]:
                    lst.append(nullpath(token, grammar, nullable, visited2))
                lst2 = product(lst,len(lst),[]) #each list in lst2 is a set of children of rule[1]
                if lst2:
                    for children in lst2:
                        results.append(Tree(item, children))
    return results


def product(lst, count, answers):
    if count == 0:
        answers.append(lst)
    else:
        for i in lst[count-1]:
            product(lst[:count-1]+[i]+lst[count:], count-1, answers)
    return answers

buildnullable(nullable,grammar)



print "nullables are:"
print nullable

##tokens = ["astronomers", "saw", "stars", "with","ears"]
##tokens = ["(", "(", ")", ")"]
tokens = ["a"]
##tokens = ["2", "+", "3", "*", "4"]

results = []
endchart = parse(tokens,grammar, nullable)
chart= flatten(endchart)
for state in endchart[len(tokens)]:
    if is_start(state, grammar):
        result= expand(state, grammar, chart, nullable)
        print result
        results.extend(result)
##        result.draw()


noduplicates = []

for i in results:
    if i not in noduplicates:
        noduplicates.append(i)

print "the number of parse trees is:" + str(len(noduplicates))

for j in noduplicates:
    j.draw()