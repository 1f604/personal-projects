# -*- coding: UTF-8 -*-
# #abbreviator version 0.01
#finished on 1st November 2015
#This is the naive version - extremely slow for any realistic input - takes ages to process more than a few thousand words
#Likely worse than O(n^3) performance
#Does not handle the case where a phrase ends with a punctuation like a comma or full stop.
#In future versions, implement option to specify min number of repeats to abbreviate
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
SHORTEST_ABBREV = 3 #abbreviate phrases of no shorter than 2 words


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

From C1, it follows that the earlier discussion of deviance is, apparently, determined by the system of base rules exclusive of the lexicon. By combining adjunctions and certain deformations, an important property of these three types of EC is necessary to impose an interpretation on problems of phonemic and morphological analysis. On our assumptions, this analysis of a formative as a pair of sets of features is not quite equivalent to an abstract underlying order. Analogously, the fundamental error of regarding functional notions as categorial suffices to account for the strong generative capacity of the theory. Furthermore, a descriptively adequate grammar is rather different from the levels of acceptability from fairly high (eg (99a)) to virtual gibberish (eg (98d)).
It may be, then, that this selectionally introduced contextual feature suffices to account for the ultimate standard that determines the accuracy of any proposed grammar. To characterize a linguistic level L, the fundamental error of regarding functional notions as categorial is not quite equivalent to the requirement that branching is not tolerated within the dominance scope of a complex symbol. Summarizing, then, we assume that the theory of syntactic features developed earlier is not to be considered in determining a parasitic gap construction. Furthermore, any associated supporting element raises serious doubts about a corpus of utterance tokens upon which conformity has been defined by the paired utterance test. Of course, the descriptive power of the base component is, apparently, determined by the traditional practice of grammarians.
Clearly, relational information is not quite equivalent to nondistinctness in the sense of distinctive feature theory. For any transformation which is sufficiently diversified in application to be of any interest, the theory of syntactic features developed earlier is not subject to an abstract underlying order. If the position of the trace in (99c) were only relatively inaccessible to movement, the notion of level of grammaticalness suffices to account for a stipulation to place the constructions into these various categories. A consequence of the approach just outlined is that this analysis of a formative as a pair of sets of features is unspecified with respect to the requirement that branching is not tolerated within the dominance scope of a complex symbol. Comparing these examples with their parasitic gap counterparts in (96) and (97), we see that an important property of these three types of EC raises serious doubts about the system of base rules exclusive of the lexicon.
It may be, then, that an important property of these three types of EC is not subject to a general convention regarding the forms of the grammar. By combining adjunctions and certain deformations, a subset of English sentences interesting on quite independent grounds is not quite equivalent to a corpus of utterance tokens upon which conformity has been defined by the paired utterance test. From C1, it follows that a descriptively adequate grammar suffices to account for nondistinctness in the sense of distinctive feature theory. On the other hand, the theory of syntactic features developed earlier raises serious doubts about an abstract underlying order. If the position of the trace in (99c) were only relatively inaccessible to movement, a case of semigrammaticalness of a different sort may remedy and, at the same time, eliminate a parasitic gap construction.
"Class is meaningless" says Marx. The subject is interpolated into a
subcultural capitalism that includes reality as a totality.

If one examines Derridaist reading, one is faced with a choice: either
accept capitalist materialism or conclude that society has intrinsic meaning.
But Sontag suggests the use of the textual paradigm of expression to challenge
the status quo. If subcultural capitalism holds, we have to choose between
capitalist materialism and postcapitalist discourse.

Therefore, many situationisms concerning Derridaist reading exist. The
primary theme of la Tournier’s[1] essay on subcultural
capitalism is the bridge between sexual identity and society.

However, Derrida’s model of the capitalist paradigm of discourse holds that
the raison d’etre of the reader is deconstruction. The characteristic theme of
the works of Madonna is the collapse, and thus the absurdity, of
postpatriarchialist culture.

It could be said that Lacan promotes the use of subcultural capitalism to
analyse and read society. The subject is contextualised into a dialectic
Marxism that includes language as a paradox.

2. Contexts of paradigm

The main theme of Humphrey’s[2] analysis of subcultural
capitalism is the common ground between sexual identity and society. In a
sense, the characteristic theme of the works of Spelling is the role of the
artist as poet. Several demodernisms concerning the difference between language
and society may be found.

In the works of Spelling, a predominant concept is the distinction between
destruction and creation. It could be said that the example of Derridaist
reading intrinsic to Spelling’s Charmed is also evident in Beverly
Hills 90210, although in a more prepatriarchialist sense. The subject is
interpolated into a subcultural capitalism that includes truth as a reality.

However, dialectic theory suggests that language is capable of significance,
given that narrativity is distinct from reality. Buxton[3]
holds that we have to choose between capitalist materialism and Baudrillardist
simulacra.

But any number of narratives concerning submaterial theory exist. If
subcultural capitalism holds, the works of Gaiman are modernistic.

Thus, the premise of Foucaultist power relations states that expression
comes from the collective unconscious. The subject is contextualised into a
capitalist materialism that includes art as a whole.
The main theme of Long’s[1] analysis of socialist realism
is the common ground between class and truth. But the subject is contextualised
into a Lacanist obscurity that includes consciousness as a reality. Derrida’s
critique of socialist realism holds that truth is capable of deconstruction,
but only if reality is interchangeable with art.

In a sense, in Natural Born Killers, Stone affirms cultural
narrative; in JFK, however, he examines Lacanist obscurity. Baudrillard
suggests the use of socialist realism to attack sexist perceptions of society.

Thus, Lyotard uses the term ‘Lacanist obscurity’ to denote the paradigm of
neocapitalist class. Any number of theories concerning the bridge between
sexual identity and reality may be discovered.

2. Socialist realism and material postdialectic theory

In the works of Stone, a predominant concept is the distinction between
creation and destruction. Therefore, if cultural narrative holds, the works of
Stone are postmodern. The characteristic theme of the works of Stone is not
dematerialism, but subdematerialism.

The main theme of la Tournier’s[2] analysis of neotextual
constructivist theory is the role of the participant as writer. In a sense, the
opening/closing distinction intrinsic to Stone’s Heaven and Earth
emerges again in Platoon. Debord promotes the use of cultural narrative
to read and challenge consciousness.

Thus, Bataille uses the term ‘material postdialectic theory’ to denote the
paradigm, and therefore the stasis, of precapitalist class. The premise of
cultural narrative implies that expression is created by the masses.

It could be said that the primary theme of the works of Stone is the role of
the participant as observer. Tilton[3] states that the works
of Stone are empowering.

Therefore, socialist realism holds that art serves to disempower minorities,
given that Derrida’s critique of cultural narrative is invalid. Sartre uses the
term ‘material postdialectic theory’ to denote not construction, but
postconstruction.

3. Narratives of absurdity

“Consciousness is part of the paradigm of language,” says Foucault; however,
according to Werther[4] , it is not so much consciousness
that is part of the paradigm of language, but rather the defining
characteristic, and subsequent collapse, of consciousness. It could be said
that a number of desituationisms concerning postdialectic socialism exist.
Sontag suggests the use of cultural narrative to deconstruct sexism.

If one examines material postdialectic theory, one is faced with a choice:
either reject cultural narrative or conclude that academe is intrinsically
impossible. Thus, the premise of material postdialectic theory implies that
sexual identity has objective value, but only if culture is distinct from
reality; if that is not the case, we can assume that discourse comes from the
collective unconscious. The characteristic theme of d’Erlette’s[5] essay on cultural narrative is the role of the poet as
reader.

Therefore, Sartre uses the term ‘socialist realism’ to denote the common
ground between culture and class. The example of cultural narrative prevalent
in Stone’s JFK is also evident in Heaven and Earth, although in a
more precapitalist sense.

It could be said that Derrida uses the term ‘material postdialectic theory’
to denote the role of the writer as observer. The primary theme of the works of
Stone is not, in fact, narrative, but postnarrative.

But the subject is interpolated into a cultural narrative that includes
sexuality as a paradox. Debord uses the term ‘material postdialectic theory’ to
denote the difference between narrativity and society.

4. Cultural narrative and Lyotardist narrative

The characteristic theme of Sargeant’s[6] analysis of
socialist realism is the dialectic, and hence the rubicon, of cultural
language. It could be said that Sontag promotes the use of subsemantic
deconstruction to analyse class. Many theories concerning the bridge between
society and class may be revealed.

“Society is part of the failure of reality,” says Debord. However, if
socialist realism holds, the works of Pynchon are reminiscent of Lynch. An
abundance of dematerialisms concerning Sontagist camp exist.

Thus, the main theme of the works of Pynchon is a mythopoetical whole. Marx
suggests the use of socialist realism to attack hierarchy.

In a sense, the primary theme of d’Erlette’s[7] model of
postdeconstructivist theory is the defining characteristic of material sexual
identity. Baudrillard promotes the use of Lyotardist narrative to challenge and
read consciousness.

Therefore, Marx uses the term ‘socialist realism’ to denote not narrative,
as Sontagist camp suggests, but prenarrative. Many theories concerning the
common ground between society and sexual identity may be found.

However, Debord’s analysis of socialist realism states that language is
fundamentally meaningless, given that the premise of posttextual appropriation
is valid. The closing/opening distinction intrinsic to Pynchon’s Gravity’s
Rainbow emerges again in The Crying of Lot 49.

5. Discourses of stasis

If one examines cultural narrative, one is faced with a choice: either
accept socialist realism or conclude that the Constitution is capable of truth.
Therefore, the subject is contextualised into a Lyotardist narrative that
includes culture as a totality. Lacan’s model of cultural narrative implies
that the significance of the writer is significant form, but only if reality is
equal to truth.

The main theme of the works of Pynchon is not theory, but pretheory. In a
sense, the subject is interpolated into a cultural paradigm of reality that
includes sexuality as a reality. Sartre suggests the use of Lyotardist
narrative to deconstruct outdated perceptions of society.

Therefore, in Gravity’s Rainbow, Pynchon analyses subsemanticist
structural theory; in Mason & Dixon, although, he examines socialist
realism. The premise of postcapitalist situationism suggests that narrativity
is used to entrench capitalism.

However, the paradigm, and eventually the futility, of cultural narrative
which is a central theme of Pynchon’s The Crying of Lot 49 is also
evident in Vineland, although in a more self-sufficient sense. Bataille
promotes the use of the conceptualist paradigm of narrative to analyse class.

But Sontag’s essay on cultural narrative implies that language, perhaps
surprisingly, has significance, given that Lyotardist narrative is invalid.
Foucault uses the term ‘cultural narrative’ to denote a mythopoetical whole.
"""
test3="""
  IANA Considerations for Three Letter Acronyms

Status of This Memo

   This memo provides information for the Internet community.  It does
   not specify an Internet standard of any kind.  Distribution of this
   memo is unlimited.

Copyright Notice

   Copyright (c) 2009 IETF Trust and the persons identified as the
   document authors.  All rights reserved.

   This document is subject to BCP 78 and the IETF Trust's Legal
   Provisions Relating to IETF Documents in effect on the date of
   publication of this document (http://trustee.ietf.org/license-info).
   Please review these documents carefully, as they describe your rights
   and restrictions with respect to this document.

   This document may contain material from IETF Documents or IETF
   Contributions published or made publicly available before November
   10, 2008.  The person(s) controlling the copyright in some of this
   material may not have granted the IETF Trust the right to allow
   modifications of such material outside the IETF Standards Process.
   Without obtaining an adequate license from the person(s) controlling
   the copyright in such materials, this document may not be modified
   outside the IETF Standards Process, and derivative works of it may
   not be created outside the IETF Standards Process, except to format
   it for publication as an RFC or to translate it into languages other
   than English.

Abstract

   Three Letter Acronyms (TLAs) are commonly used to identify components
   of networks or protocols as designed or specified within the IETF.  A
   common concern is that one acronym may have multiple expansions.
   While this may not have been an issue in the past, network
   convergence means that protocols that did not previously operate
   together are now found in close proximity.  This results in
   contention for acronyms, and confusion in interpretation.  Such
   confusion has the potential to degrade the performance of the
   Internet as misunderstandings lead to misconfiguration or other
   operating errors.

   Given the growing use of TLAs and the relatively small number
   available, this document specifies a Badly Construed Proposal (BCP)
   for the management of a registry of TLAs within the IETF, and the
   procedures for the allocation of new TLAs from the registry.

1.  Introduction

   A Three-Letter Acronym (TLA) is a popular form of abbreviation
   usually based on the initial letters of a three-word term.  A formal
   definition of a TLA is provided in Section 2.

   TLAs are particularly popular within the Internet community where
   they serve as abbreviations in the spoken and written word.  As their
   popularity has grown, the measure of the value of an RFC (q.v.) is
   not only its successful implementation, interoperability, and
   deployment, but also the number of TLAs included in the text.

   For example, the Transmission Control Protocol (itself a TLA - TCP)
   [RFC0793] is extremely successful.  The specification contains no
   fewer than 20 distinct TLAs (although it should be noted that some
   are simple abbreviations rather than proper acronyms).  On the other
   hand, the Internet Stream Protocol Version 2 [RFC1819] is ambiguously
   referred to using the TLA ST2, and also as STII which is clearly not
   a TLA.  Further, the STII specification contains only 12 distinct
   TLAs, and it should be no surprise that STII has been far less
   successful than TCP.

   A common concern amongst diligent protocol implementers is that one
   acronym may have multiple expansions.  While this may not have been
   an issue in the past, network convergence means that protocols that
   did not previously operate together are now found in close proximity.
   Not only does this result in contention for acronyms, and confusion
   in interpretation of specification, it also leads to many wasted
   hours trying to select appropriate and suitably-unique names for
   variables within source code implementations.  Such confusion has the
   potential to degrade the performance of the Internet as
   misunderstandings lead to coding errors, compilation failures,
   misconfiguration, and other operating errors.

   Furthermore, it should be noted that we are rapidly approaching World
   Acronym Depletion (WAD).  It has been estimated that, at the current
   rate of TLA allocation, we will run out by the end of September this
   year.  This timescale could be worsened if there is the expected
   growth in demand for mobile acronyms, IP-TLAs, and TLA-on-demand.
   According to the definition provided in Section 2, there are 36**3 -
   10**3 = 45656 TLAs in total.  This number will so easily be depleted
   that we must institute some policy for conservation.

   The Internet Assigned Numbers Authority (IANA, helpfully, a four-
   letter acronym - although note that a four-letter acronym is an FLA
   and hence is, in its own way, a TLA) maintains registries of names
   and numbers for use within the Internet in order to avoid duplicate
   allocation of one of those names or numbers and the consequent
   confusion and failed interoperability that would arise.  It is,
   therefore, wholly appropriate that the IANA should manage the
   assignment and use of TLAs within the Internet.

   This document specifies a Badly Construed Proposal for the management
   of a registry of TLAs within the IETF, and the procedures for the
   allocation of new TLAs from the registry.

1.1.  RFC Editor Terminology List

   It is worth observing that the RFC Editor currently maintains a list
   of common terms, abbreviations, and acronyms.  While this list is
   highly useful for the construction of documents, it does not provide
   unambiguous interpretation of acronyms.

2.  Formal Definition of TLA

   Acronym - a word made up of the initial letters of the words in a
      phrase.

      For example, IETF is an acronym formed from the first letters of
      the phrase International Essential Tremor Foundation [URL-IETF].

   Three Letter Acronym (TLA) - an acronym comprising exactly three
      letters.

      For example, RFC is a TLA formed of the first letters of the
      phrase Rugby Football Club [URL-CARDIFF].

   For our usage, we also allow digits within a TLA.  Thus, P2P is an
   acronym meaning Purchase to Pay [URL-P2P].  The digits 2 and 4 are
   specially used by clever people who have noticed that, when spoken,
   they sound like the words 'to' and 'for'.  Whether this is helpful
   may be left as an exercise for the user considering the brief
   conversation, below.

   A - Do you use the Internet Streams Protocol?
   B - Yes.  Do you use ST, too?
   A - No, I use ST2.
   B - That's interesting.  C uses ST2, too.
   A - I have a car horn application called Toot-toot.
   B - Really? Do you use ST2 to Toot-toot, too?

   Note, however, that an acronym made up entirely of digits might be
   frowned upon.

   Lastly, we must consider case-sensitivity.  Although acronyms often
   include upper or lowercase letters, no assumptions should be made
   about the interpretation of the acronym based on the case of its
   letters, so that both QOS and QoS clearly refer to the Queen of the
   South football club [URL-QOS] and [URL-QoS].

2.1.  A Note on Vocalization

   Acronyms are often articulated as words in spoken text.  This can be
   helpful in generating a cosy feel or a marketing buzz around a
   concept that offers a less-favorable reality.  For example, Claws and
   Teeth (CAT) can be pronounced "cat" making it seem quite cuddly.

   Other acronyms are always spelled out in order to avoid accidental
   misinterpretation or litigation.  For example, do not refer to your
   neighbor's Daughter or Granddaughter as anything other than their
   D-O-G.

   But care should be taken with vocalization, as well.  It will be
   noted that some letters have more syllables than the words they are
   used to represent.  In these cases, acronyms are to be avoided.
   Thus, the world wide web must never be assigned the acronym WWW.

   Finally, a word of caution about attempting to pronounce acronyms as
   words.  This can lead to serious injury for the inexperienced unless
   they happen to be native speakers of Czech.  Do not try to say XML in
   front of your mother-in-law, and don't attempt to talk about Open
   Office dot Org in polite company.

3.  Backward and Forward Compatibility

   It should be obvious to most RFC readers (MRRs) that TLAs are already
   widely used in Internet specifications.  This work is not intended to
   unnecessarily invalidate existing RFCs, although where such
   invalidation is necessary or desirable, this work can be used for
   that purpose.

   In order to support existing documents, IANA is required to search
   all existing RFCs for every existing acronym usage (EAU), but may
   filter that search to exclude non-TLAs.

   It will be noted that, as a result of that search, many duplicate
   meanings will be discovered.  For example, "OAM" will be found in a
   large number of RFCs, yet its meaning may be as diverse as "on a
   mission", "order of Australia medal", and "orbital angular momentum".

   This contention is best resolved by the judgement of Solomon -- each
   acronym usage will be allocated its share of the letters currently in
   use.  If there are three uses of an acronym, they will get one letter
   each; two existing uses would get one-and-a-half letters each; etc.

4.  IANA Considerations

4.1.  New Registry

   The Internet TLA Registry (ITR) should track the following
   information:

      - TLA
      - Unique interpretation
      - Defining RFC

4.2.  Reserved Values

   Certain key values are reserved.  That is, they are allocated in the
   registry by this document and may not be used for any other purpose.

      Acronym   Expansion                             Reference
      --------+-------------------------------------+-----------
      TLA       Two Letter Acronym                    [RFC5513]
      TBD       Two Be Deleted                        [RFC5513]
      RFC       Ready for Compost                     [RFC5513]
      PoS       Not particularly good                 [RFC5513]
      VPN       Very possibly no use                  [RFC5513]
      TCP       Totally bad proposal                  [RFC5513]
      USA       Universal Source of Acronyms          [RFC5513]
      NBG       This document                         [RFC5513]
      BCP       Badly construed proposal              [RFC5513]

4.3. Allocation Policy

   IANA shall apply the following allocation policies according to
   [RFC5226].

   Experimental Use
      All TLAs of the form XX* where * is any letter or digit.

   First Come First Served
      All TLAs of the form X**, Y**, or Z** where * is any letter or
      digit.  Excepted from this are the TLAs of the form XX* as above.

   IETF Review
      All other TLAs.

5.  Security Considerations

   Many security algorithms are identified by TLAs.  It is a clear
   requirement that someone implementing, for example, MD5 should be
   understood to have encoded the well-known Maybe-Decrypted-
   Deciphered-Decoded-Disambiguated-and-Degraded algorithm, and not any
   other security algorithm with the same acronym.

6.  Acknowledgements

   I would like to thank the MPLS-TP design team for holding seemingly
   endless meetings during which the need for this document became
   apparent.

   Thanks to Daniel King for noticing that this document is a BCP.
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
    for sequenceLength in range(min(LONGEST_ABBREV,len(src)/2),SHORTEST_ABBREV-1,-1): 
        out = printRepeatingPhrases(src, sequenceLength) 
        if (out):
            for phrase in out: 
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
                    searchandreplace(phrase,abb[0:-1],src) 
                else:
                    searchandreplace(phrase,abb,src) 
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
