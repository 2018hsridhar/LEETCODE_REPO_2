'''
URL := https://leetcode.com/problems/longest-ideal-subsequence/description/
2370. Longest Ideal Subsequence

Complexity
Let N := len(string)
T = O(N^2)
S = O(N) ( E ) O(1 ) ( I ) 

Categories
BUDP, Naive Recursion, Scanning, String Manipulation 

Motivations :
[a] String lengths in text processing ( according to externally imposed constraints )
[b] Do all langs in the world have ordinal ordering naturally? Imposable in any where for numeric system ( even character langs like Traditional Mandarin ) .
[c] PY written as calculator esque langauge
[d] O(N^2) runs into a TLE for sure -> how to make O(N) -> more mem -> hash table :-) 
Sublte -> Indentation error issue
'''
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        lis = 0
        # signage store on single bit matters @ scale w/millions of records
        # use 0 instead ( -1 for debug better )
        # memo = [-1 for i in range(len(s))]
        # https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python
        # for i, leftChar in enumerate(s):
        charHt = dict()
        for index, leftChar in reversed(list(enumerate(s))):
            curLis = 1
            if leftChar not in charHt:
                charHt[leftChar] = 1
            # alawys in character cyclicity here, now isn't it the case :-)
            # print("Hit char = " + leftChar + "      ord = " + str(curOrd))
            # eval via alphabet order ( max char here )
            # nasty ass bug over here ( should've been 0 ) for double repeating characters
            for delta in range(0,k+1,1):
                posChar = self.getCharOffset(leftChar,delta)
                negChar = self.getCharOffset(leftChar,delta * -1)
                if(self.meetsCriteria(leftChar,posChar,charHt, k)):
                    curLis = max(curLis, 1 + charHt[posChar])
                if(self.meetsCriteria(leftChar,negChar,charHt, k)):
                    curLis = max(curLis, 1 + charHt[negChar])
            charHt[leftChar] = max(charHt[leftChar], curLis)
            lis = max(lis, curLis)
        return lis - 1

    def getCharOffset(self, leftChar:str, delta:int) -> str:
        baseChar = 'a'
        curOrd = ord(leftChar) - ord(baseChar)
        offsetChar = chr(ord(baseChar) + ((curOrd + delta) + 26) % 26)
        return offsetChar
    
    def meetsCriteria(self, leftChar:str, rightChar:str, charHt:dict, k:int) -> bool:
        minChar = min(leftChar,rightChar)
        maxChar = max(leftChar,rightChar)
        if (minChar in charHt and maxChar in charHt and (ord(maxChar) - ord(minChar) <= k)):
            return True
        return False
