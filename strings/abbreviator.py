#abbreviator version 0.01
#finished on 1st November 2015
#This is the naive version - extremely slow for any realistic input - takes ages to process more than a few thousand words
#Likely worse than O(n^3) performance
#Does not handle the case where a phrase ends with a punctuation like a comma or full stop.
#Rough sketch of future O(n^2) algorithm:
#1. Get longest repeated substring by constructing (O(n) if using Ukkonen's) and searching through a suffix tree - worst case O(n).
#2. Run searchandreplace on the resulting substring to abbreviate it out. Complexity for searchandreplace should be O(n) if using Boyer-Moore with Galil rule. Steps 1+2 together is O(n).
#2. Actually the searchandreplace step can be merged into #1 since we can just do the search on the suffix tree itself. This results in a lower time complexity for this step but since we have to rebuild the suffix tree after every modification to the string, the time complexity is unchanged.
#3. Repeat step 1-2 until there are no repeated substrings. Time-complexity: O(n*r) where r is the number of longest repeated substrings (each after previous one has been deleted from text). Worst case O(n^2)
#
#Alternative algorithm sketch (not sure if possible or faster):
#1. Same as above but instead of rebuilding the suffix tree after each deletion, simply modify the suffix tree to fit the new string
#2. Same as above but instead of rebuilding the suffix tree after each deletion, simply keep a list of indices to avoid so that the next search will not visit those nodes that are already deleted. Then delete/replace all the LRPs to be deleted at once once all have been found.
#
#Another alternative O(n^2) or worse algorithm (not sure if possible):
#1. Again, construct suffix tree in O(n)
#2. Search through suffix tree for ALL repeating substrings. This is O(n^2) already
#3. Cull those substrings which are already in previous substrings (unsure of time complexity of this), then run searchandreplace on the remaining substrings. This step would be at least O(n^2) because searchandreplace is O(n)
LONGEST_ABBREV = 20 #abbreviate phrases of no longer than 20 words
SHORTEST_ABBREV = 2 #abbreviate phrases of no shorter than 2 words


import cProfile
from datetime import datetime

def printRepeatingPhrases(src, sequenceLength): #O(n) time complexity
                i=0
                j=i+sequenceLength
                tempSet = []
                repeatingSequences = []
                while (j <= len(src)):
                    if (src[i:j] not in tempSet):
                        tempSet.append(src[i:j]);
                    else:
                        repeatingSequences.append(src[i:j]);
                    i+=1
                    j = i + sequenceLength;
                return repeatingSequences


test="AB FG A B C BA BBZE A B C D Z E D BBZE AB FG"
test2 = """A consequence of the approach just outlined is that the systematic use of complex symbols may remedy and, at the same time, eliminate irrelevant intervening contexts in selectional rules. With this clarification, the notion of level of grammaticalness suffices to account for an important distinction in language use. From C1, it follows that any associated supporting element does not affect the structure of the strong generative capacity of the theory. So far, this selectionally introduced contextual feature is, apparently, determined by nondistinctness in the sense of distinctive feature theory. Presumably, the natural general principle that will subsume this case is not subject to an abstract underlying order.
It appears that the fundamental error of regarding functional notions as categorial appears to correlate rather closely with the ultimate standard that determines the accuracy of any proposed grammar. Conversely, an important property of these three types of EC is, apparently, determined by an important distinction in language use. Clearly, a case of semigrammaticalness of a different sort is unspecified with respect to the levels of acceptability from fairly high (eg (99a)) to virtual gibberish (eg (98d)). A consequence of the approach just outlined is that most of the methodological work in modern linguistics delimits the strong generative capacity of the theory. However, this assumption is not correct, since relational information can be defined in such a way as to impose an abstract underlying order.
This suggests that the notion of level of grammaticalness can be defined in such a way as to impose an abstract underlying order. Comparing these examples with their parasitic gap counterparts in (96) and (97), we see that the appearance of parasitic gaps in domains relatively inaccessible to ordinary extraction is to be regarded as the traditional practice of grammarians. For one thing, this analysis of a formative as a pair of sets of features is rather different from problems of phonemic and morphological analysis. We have already seen that the theory of syntactic features developed earlier cannot be arbitrary in irrelevant intervening contexts in selectional rules. On the other hand, this selectionally introduced contextual feature suffices to account for nondistinctness in the sense of distinctive feature theory.
For one thing, the notion of level of grammaticalness does not readily tolerate the ultimate standard that determines the accuracy of any proposed grammar. A consequence of the approach just outlined is that the speaker-hearer's linguistic intuition is necessary to impose an interpretation on a descriptive fact. If the position of the trace in (99c) were only relatively inaccessible to movement, the fundamental error of regarding functional notions as categorial is unspecified with respect to the extended c-command discussed in connection with (34). Presumably, most of the methodological work in modern linguistics suffices to account for a general convention regarding the forms of the grammar. Conversely, a descriptively adequate grammar cannot be arbitrary in the requirement that branching is not tolerated within the dominance scope of a complex symbol.
It must be emphasized, once again, that the systematic use of complex symbols is not subject to a corpus of utterance tokens upon which conformity has been defined by the paired utterance test. On our assumptions, most of the methodological work in modern linguistics is not to be considered in determining the levels of acceptability from fairly high (eg (99a)) to virtual gibberish (eg (98d)). However, this assumption is not correct, since the appearance of parasitic gaps in domains relatively inaccessible to ordinary extraction cannot be arbitrary in an abstract underlying order. A consequence of the approach just outlined is that the notion of level of grammaticalness is rather different from a descriptive fact. Conversely, the natural general principle that will subsume this case is not quite equivalent to the ultimate standard that determines the accuracy of any proposed grammar.
Presumably, the theory of syntactic features developed earlier is not subject to the ultimate standard that determines the accuracy of any proposed grammar. Furthermore, the natural general principle that will subsume this case suffices to account for a corpus of utterance tokens upon which conformity has been defined by the paired utterance test. With this clarification, this analysis of a formative as a pair of sets of features does not readily tolerate problems of phonemic and morphological analysis. In the discussion of resumptive pronouns following (81), the appearance of parasitic gaps in domains relatively inaccessible to ordinary extraction may remedy and, at the same time, eliminate a descriptive fact. So far, the fundamental error of regarding functional notions as categorial does not affect the structure of an important distinction in language use.
Summarizing, then, we assume that the theory of syntactic features developed earlier cannot be arbitrary in a corpus of utterance tokens upon which conformity has been defined by the paired utterance test. Presumably, this selectionally introduced contextual feature delimits the levels of acceptability from fairly high (eg (99a)) to virtual gibberish (eg (98d)). Thus the natural general principle that will subsume this case appears to correlate rather closely with irrelevant intervening contexts in selectional rules. On our assumptions, the systematic use of complex symbols is not subject to an abstract underlying order. Analogously, relational information is, apparently, determined by a parasitic gap construction.
Note that the earlier discussion of deviance is, apparently, determined by a stipulation to place the constructions into these various categories. Thus the theory of syntactic features developed earlier can be defined in such a way as to impose an abstract underlying order. Comparing these examples with their parasitic gap counterparts in (96) and (97), we see that the descriptive power of the base component is not quite equivalent to irrelevant intervening contexts in selectional rules. Conversely, the appearance of parasitic gaps in domains relatively inaccessible to ordinary extraction may remedy and, at the same time, eliminate a parasitic gap construction. Summarizing, then, we assume that this analysis of a formative as a pair of sets of features is not subject to the ultimate standard that determines the accuracy of any proposed grammar.
For any transformation which is sufficiently diversified in application to be of any interest, a case of semigrammaticalness of a different sort raises serious doubts about nondistinctness in the sense of distinctive feature theory. By combining adjunctions and certain deformations, the systematic use of complex symbols suffices to account for the strong generative capacity of the theory. On our assumptions, the appearance of parasitic gaps in domains relatively inaccessible to ordinary extraction cannot be arbitrary in the traditional practice of grammarians. With this clarification, the fundamental error of regarding functional notions as categorial is, apparently, determined by a parasitic gap construction. Clearly, an important property of these three types of EC is rather different from problems of phonemic and morphological analysis.
Conversely, most of the methodological work in modern linguistics does not readily tolerate a corpus of utterance tokens upon which conformity has been defined by the paired utterance test. Note that the natural general principle that will subsume this case delimits the ultimate standard that determines the accuracy of any proposed grammar. So far, the appearance of parasitic gaps in domains relatively inaccessible to ordinary extraction cannot be arbitrary in a stipulation to place the constructions into these various categories. Clearly, the speaker-hearer's linguistic intuition is not quite equivalent to the levels of acceptability from fairly high (eg (99a)) to virtual gibberish (eg (98d)). From C1, it follows that an important property of these three types of EC may remedy and, at the same time, eliminate the extended c-command discussed in connection with (34).
Presumably, a descriptively adequate grammar suffices to account for the traditional practice of grammarians. Clearly, the systematic use of complex symbols can be defined in such a way as to impose nondistinctness in the sense of distinctive feature theory. By combining adjunctions and certain deformations, relational information is unspecified with respect to irrelevant intervening contexts in selectional rules. So far, the appearance of parasitic gaps in domains relatively inaccessible to ordinary extraction does not readily tolerate an abstract underlying order. Summarizing, then, we assume that the natural general principle that will subsume this case is not to be considered in determining a general convention regarding the forms of the grammar.
"""
def abbreviate(phrase):
    result = []
    for word in phrase:
        if isinstance(word,str):
            result.append(word[0].upper())
        else:
            result.append(str(word))
    return ''.join(result)

def indexof(sl,l): #This is O(n*m)
    sll=len(sl)-1
    for i in range(len(l)-sll+1):
        counter = i
        for j in range(sll):
            if(l[counter]!=sl[j]):
                break
            if (j+1==sll):
                return i
            counter += 1

def searchandreplace(phrase, abbreviation, src): #This is O(n*m*number of times the phrase repeats in the text)
    start=indexof(phrase,src)
    sll=len(phrase)-1
    while(start!=None):
        src[start] = abbreviation
        del src[start+1:start+sll]
        start=indexof(phrase,src)


def iterate(inputString):
    src = inputString.split()
    abbreviations = {}
    for sequenceLength in range(min(LONGEST_ABBREV,len(src)/2),SHORTEST_ABBREV-1,-1): #this loop runs O(n) times
        out = printRepeatingPhrases(src, sequenceLength) #this function runs in O(n), so already this algorithm is O(n^2)
        if (out):
            for phrase in out: #this loop runs at most n times therefore is at least O(n^2).
                brk = False
                phrase.append(0)
                while(abbreviate(phrase) in abbreviations): #simply check if phrase is already in dictionary
                    if abbreviations[abbreviate(phrase)] == phrase:
                        brk = True
                    phrase[-1]+=1
                if (brk):
                    continue
                abb=abbreviate(phrase)
                abbreviations[abb]=phrase
                start = datetime.now()
                if phrase[-1] == 0:
                    searchandreplace(phrase,abb[0:-1],src) #O(n*length of phrase*number of times phrase appears in the text)
                else:
                    searchandreplace(phrase,abb,src) #O(n*length of phrase*number of times phrase appears in the text)
    print "key :"
    for key in abbreviations:
        if abbreviations[key][-1] == 0:
            print key[0:-1] + ": " + ' '.join(abbreviations[key][0:-1])
        else:
            print key + ": " + ' '.join(abbreviations[key][0:-1])
    print ' '.join(src)


start = datetime.now()
#iterate(test2)
cProfile.run('iterate(test2)')
print (datetime.now() - start)
