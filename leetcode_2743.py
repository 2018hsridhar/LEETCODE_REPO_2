'''
2743. Count Substrings Without Repeating Character
URL := https://leetcode.com/problems/count-substrings-without-repeating-character/description/

Complexity
T = O(N)
S = O(N) ( E ) 
O(1) ( I ) 

Approach & Category : Hashmap, Counting, Sliding Windows
TTC = 15 minutes
'''
class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        numSpecial = 0
        letterFreq = dict()
        n = len(s)
        left = 0
        for right, rightLet in enumerate(s):
            if(rightLet not in letterFreq):
                letterFreq[rightLet] = 0
            letterFreq[rightLet] += 1
            rightFreq = letterFreq[rightLet]
            if(rightFreq > 1):
                while(rightFreq > 1 and left <= right):
                    window = (right - left)
                    numSpecial += window
                    leftLet = s[left]
                    left += 1
                    letterFreq[leftLet] -= 1
                    rightFreq = letterFreq[rightLet]
        for leftPtr in range(left,n,1):
            window = (n - leftPtr)
            numSpecial += window
        return numSpecial

    def snn(self,n:int) -> int:
        ans = (int)((0.5)*(n)*(n+1))
        return ans
