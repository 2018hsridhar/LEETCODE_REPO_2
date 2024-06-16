'''
URL := https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/
3034. Number of Subarrays That Match a Pattern I

Pattern matching subarrays to a given pattern of numbers

Complexity :
Let N := len(arr) and M := len(pattern)
T = O(MN)
Space = O(1) ( E ) O(1) ( I ) 

Commit Log :
(A) Bounds allow for good brute force solutioning :-) !
(B) Can we use a sliding window ( to be better ) -> probably not :-(
    One efficiency : RabinKarp inspired -> match patern from the start?
(C) Why an if cond when a bool cond works :-)

15 mins to solutioning -> EASY problem !

'''
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        numMatches = 0
        n = len(nums)
        p = len(pattern)
        # n = 6, p = 2 -> final index = 3 ( range of 4 reasoning ) 
        for lPtr in range(n - p):
            leftMatchesPattern = True
            for offset, patternVal in enumerate(pattern):
                leftEl = nums[lPtr + offset]
                rightEl = nums[lPtr + offset + 1]
                if(patternVal == 1 and leftEl >= rightEl):
                    leftMatchesPattern = False
                elif(patternVal == 0 and leftEl != rightEl):
                    leftMatchesPattern = False
                elif(patternVal == -1 and leftEl <= rightEl):
                    leftMatchesPattern = False
            # numMatches = (numMatches + 1 ) if(leftMatchesPattern) else (numMatches)
            numMatches += int(leftMatchesPattern)
        return numMatches
