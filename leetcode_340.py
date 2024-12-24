'''
340. Longest Substring with At Most K Distinct Characters
URL := https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
Most sliding window problems involve dealing with input tapes

Compelxity
T = O(N)
S = O(1) ( E and I ) 
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        lenLongest = 0
        lPtr = 0
        rPtr = 0
        n = len(s)
        charFreq = dict()
        for rPtr,let in enumerate(s):
            if(let not in charFreq):
                charFreq[let] = 0
            charFreq[let] += 1
            # close out portion precedes eval portion
            while(len(charFreq) > k and lPtr <= rPtr):
                leftLet = s[lPtr]
                charFreq[leftLet] -= 1
                if(charFreq[leftLet] == 0):
                    del charFreq[leftLet]
                lPtr += 1
            curNumChars = len(charFreq)
            if(curNumChars <= k):
                window = (rPtr - lPtr + 1)
                lenLongest = max(lenLongest, window)
        return lenLongest
        
