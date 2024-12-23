'''
URL := https://leetcode.com/problems/expressive-words/description/
809. Expressive Words

Ideas
(A) Two pointers racing
(B) Compress both strings and ask frequency as they occur ( get the digitFreq ) 
    compare RLE : e.g.
        ( first ) hello => h1:e1:l2:o1
        ( second ) heeellooo => h1:e3:l2:o3
        for each letter in (first), get size in (second), provided they are the same
        check size(second) >= (first) and size(second) >= three
        If conditions met, good to go
        can tokenized into records

'''
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        numStretchy = 0
        rleS = self.getRLE(s)
        for word in words:
            rleWord = self.getRLE(word)
            ptrWord = 0
            ptrS = 0
            metStretchReq = True
            if(len(rleS) != len(rleWord)):
                metStretchReq = False
            else:
                while(ptrWord < len(rleWord) and ptrS < len(rleS)):
                    recordWord = rleWord[ptrWord]
                    recordS = rleS[ptrS]
                    if(recordWord[0] == recordS[0]):
                        if(recordWord[1] != recordS[1]):
                            groupCond = (recordWord[1] < recordS[1] and recordS[1] >= 3)
                            if(groupCond == False):
                                metStretchReq = False
                    else:
                        metStretchReq = False 
                    ptrWord += 1
                    ptrS += 1
            if(metStretchReq):
                numStretchy += 1
        return numStretchy
        
    def getRLE(self, s:str):
        rle = []
        lastLetter = s[-1]
        ptr = 0
        n = len(s)
        runCount = 1
        curLet = ''
        while(ptr < n - 1):
            curLet = s[ptr]
            nextLet = s[ptr+1]
            if(curLet == nextLet):
                runCount += 1
            else:
                record = [curLet,runCount]
                rle.append(record)
                runCount = 1
            ptr += 1
        lastRecord = [lastLetter,runCount]
        rle.append(lastRecord)
        return rle
