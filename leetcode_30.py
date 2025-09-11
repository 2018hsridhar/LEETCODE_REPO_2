'''
30. Substring with Concatenation of All Words
URL := https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

Biggest help : words all share the same length

Complexity
N = len(s)
W = len(words)
K = len(words[i]) [ INVARIANT ] 

TIME = O(NK*W) ( POLY ) ( but can this get bad ) ?
SPACE = O(W) ( E ) O(1) ( I ) 

Word len bounded by 30 -> only so many positions to check in the sliding window
 |aaa|bbb|ccc|ddd|eee|fff|ggg
a|aab|bbc|ccd|dde|eef|ffg|ggg
^ this type of thinking?

Groups of 2 : aa|bb|cc|dd OR a|ab|bc|cd|d OR |aa|bb ( modular arithmetic )
It's a bunch of loops and a hash check ( 5000 ops max )?
Can it be done faster?

For each word -> get (A) Index it belongs too
E.g. foo -> indices (1),(4),(7) type of thing ( okay a basic matching )
Sliding window fixed length is a quick check for a 1x scan

barfoofoobarthefoobarman
bar => 0,9,18,
foo => 3,6,15
the => 12,
man => 21
Ok I'm at index=14, and I sub 9 - the, foo, and bar show up

O(NW) prefered with alloc of space -> count of words matching expectations
Seems better
45 minutes spent ( go solve something else :-| ) ( SMHHH ) +++ - > talent elsewhere buddy? ( come b ack again ) ( this IS not worth the investment for ROI of time ) ( SMH Gnarly bug here ) 

Yeah each word => an array of indices 
bar => [0,0,1,1,1,1,1,1,1,1,1,2,...] and so on => counts go on
ok
Yeah I knew that prefix sum solution was a bad one
Yeah I bet it's a TLE at this point -> go do something else bruh


'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        startingIndices = []
        k = len(words[0])
        w = len(words)
        n = len(s)
        windowLen = (w*k)
        uniqWords = set()
        # [1] Hashmap population
        wordFreq = dict()
        for word in words:
            uniqWords.add(word)
            if(word not in wordFreq):
                wordFreq[word] = 0
            wordFreq[word] += 1
        # [2] Get starting indices ( sliding window )
        # get length and do a check here? hmmm
        # yeah better to go with that POLY time - but - O()
        for startLeftPos in range(k):
            numTokensHit = 0
            runMap = dict()
            leftPos = startLeftPos
            cond = leftPos + k
            while(cond <= n):
                startIndex = leftPos - windowLen + k
                rightPos = leftPos + k
                if(rightPos <= n):
                    token = s[leftPos:rightPos]
                    if(token not in runMap):
                        runMap[token] = 0
                    runMap[token] += 1
                    numTokensHit += 1
                if(numTokensHit > w):
                    numTokensHit -= 1
                    # remove left token
                    leftOfWin = leftPos - windowLen
                    winRight = leftOfWin + k
                    firstToken = s[leftOfWin:winRight]
                    if(firstToken in runMap):
                        runMap[firstToken] -= 1
                        if(runMap[firstToken] == 0):
                            del runMap[firstToken]
                # Map comparison ( major step ) ( cuts both ways )
                # get window end here right
                # damn you're close ( SMHHH what's going on here ) 
                # I'm missing something ( a doubling case ) 
                # it's a duplicate case with the wrong index HUH
                if(self.mapsEqual(runMap,wordFreq)):
                    startingIndices.append(startIndex)
                leftPos += k
                cond = leftPos + k
        return startingIndices
    
    def mapsEqual(self,runMap:dict,wordFreq:dict) -> bool:
        equalFirst = True
        equalSecond = True
        for a, b in runMap.items():
            if(a not in wordFreq):
                equalFirst = False
            else:
                if(runMap[a] != wordFreq[a]):
                    equalFirst = False
        for c, d in wordFreq.items():
            if(c not in runMap):
                equalSecond = False
            else:
                if(wordFreq[c] != runMap[c]):
                    equalSecond = False
        if(equalFirst and equalSecond):
            return True
        return False

