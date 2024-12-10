'''
URL := https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/description/
3365. Rearrange K Substrings to Form Target String

Classif : Hashmaps, Counting, Enumeration, Splitting, Tokenizations
Both strings share equal lengths

Complexity
N := len(s), k := #-substrings
Time = O(N)
Space = O(K) ( E ) O(1) ( I ) 
'''
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        canRearrange = True
        tokenMapS = self.makeTokenMap(s,k)
        tokenMapT = self.makeTokenMap(t,k)
        canRearrange = canRearrange and self.getCompareMapStatus(tokenMapS,tokenMapT)
        canRearrange = canRearrange and self.getCompareMapStatus(tokenMapT,tokenMapS)
        return canRearrange

    def getCompareMapStatus(self, mapA: dict, mapB:dict) -> bool:
        canRearrange = True
        for k, freqA in mapA.items():
            if(k not in mapB):
                canRearrange = False
                break
            freqB = mapB[k]
            if(freqA != freqB):
                canRearrange = False
                break
        return canRearrange

    def makeTokenMap(self, s:str, k:int) -> dict:
        tokenLen = (int)(len(s) / k)
        tokenMap = dict()
        for ptr in range(0,len(s),tokenLen):
            token = s[ptr:ptr + tokenLen]
            if(token not in tokenMap):
                tokenMap[token] = 0
            tokenMap[token] += 1
        return tokenMap
        
