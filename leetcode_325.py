'''
325. Maximum Size Subarray Sum Equals k
URL := https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/

Complexity
N := len(input)
T = O(N)
S = O(N) ( Explicit ) O(1) ( Implicit ) 

Sum of 0 is default on the left ( remember that ) 

'''
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        indexNumSeenLeft = dict()
        indexNumSeenLeft[0] = 0
        prefixSum = 0
        maxLen = 0
        for rightIdx, num in enumerate(nums):
            prefixSum += num
            if(prefixSum not in indexNumSeenLeft):
                indexNumSeenLeft[prefixSum] = rightIdx
            target = prefixSum - k
            curWindow = 0
            if(target in indexNumSeenLeft):
                if(target != 0):
                    leftIdx = indexNumSeenLeft[target]
                    curWindow = (rightIdx - leftIdx)
                elif(target == 0):
                    curWindow = (rightIdx + 1)
                maxLen = max(maxLen,curWindow)
        return maxLen
