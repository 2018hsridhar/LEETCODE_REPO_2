'''
URL := https://leetcode.com/problems/count-the-hidden-sequences/description/
2145. Count the Hidden Sequences

Complexity
N := len(differences)
T = O(N)
S = O(1) ( E ) 
'''
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        numHiddenSeqs = 0
        delta = 0
        minDelta = 0
        maxDelta = 0
        for difference in differences:
            delta += difference
            minDelta = min(minDelta,delta)
            maxDelta = max(maxDelta, delta)
        left = lower - minDelta
        right = upper - maxDelta
        numHiddenSeqs = right - left + 1
        return max(numHiddenSeqs,0)
        
