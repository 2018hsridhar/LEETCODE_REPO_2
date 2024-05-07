'''
URL := https://leetcode.com/problems/count-alternating-subarrays/description/
3101. Count Alternating Subarrays

Complexity
Let N := #-els in the input
Time := O(N)
Space := O(1) ( E ) O(1) ( I ) 

Category 
Linear Scan, Single Pass, Counting, Sliding Window Technique, Two Pointers

Cases :
(A) [0,0,0]
(B) [1,1,1]
(C) [0]
(D) [1]
(E) [0,1,0,1,0]
(F) [1,0,1,0,1]
(G) [0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,1]
(H) [1,1,1,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0]

'''
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        cas = 0
        # Why write while loops first -> for loops should be written first
        # It's interesting to see stylistic evolution here!
        # always check with an oscilattor
        curVal = 1-nums[0]
        curWindowSize = 0
        for nextVal in nums:
            if(nextVal == curVal):
                cas += (curWindowSize * (curWindowSize+1) / 2)
                curWindowSize = 1
            else:
                curVal = nextVal
                curWindowSize += 1
        # Get the last window size accounted for
        # Natural num summation
        cas += (curWindowSize * (curWindowSize+1) / 2)
        return int(cas)

    # sum natural numbers -> functionalize it :-)
    def snn(self,n:int) -> int:
        return (n * (n+1) / 2)
        
