'''
URL := https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/description/
2311. Longest Binary Subsequence Less Than or Equal to K

Categories : Linear Scan, Single Pass, Greedy, Math, Pow-of-2

Complexity
N = len(input)
T = O(N)
S = O(1) ( Explicit ) O(1) ( Implicit ) 
'''
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        lengthLongest = 0
        n = len(s)
        toPow = 0
        curVal = 0
        base = 2
        for ptr in range(len(s) - 1, -1,-1):
            let = s[ptr]
            val = (int)(let)
            if(val == 0):
                lengthLongest += 1
            elif(val == 1):
                delta = pow(base,toPow)
                nextVal = curVal + delta
                if(nextVal <= k):
                    curVal = nextVal
                    lengthLongest += 1
            toPow += 1
        return lengthLongest
        
