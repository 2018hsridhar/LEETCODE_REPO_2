'''
URL := https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description/
2981. Find Longest Special Substring That Occurs Thrice I

Cartegories : BSearch, Hashmaps, Counting
Complexity
S = len(S)
T = O(lg(S)*S)
S = O(S) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def maximumLength(self, s: str) -> int:
        low = 1
        high = len(s)
        n = len(s)
        THRICE = 3
        bestLength = -1
        while(low <= high):
            mid = (int)((0.5)*(low + high))
            freqMap = dict()
            metThriceCond = False
            for leftPtr in range(0,n+1-mid,1):
                rightPtr = (leftPtr + mid)
                substr = s[leftPtr:rightPtr]
                uniqLetters = set(substr)
                if(len(uniqLetters) == 1):
                    if(substr not in freqMap):
                        freqMap[substr] = 0
                    freqMap[substr] += 1
                    if(freqMap[substr] >= THRICE):       
                        metThriceCond = True 
            if(metThriceCond):
                bestLength = max(bestLength,mid)
                low = mid + 1
            elif(not metThriceCond):
                high = mid - 1
        return bestLength
