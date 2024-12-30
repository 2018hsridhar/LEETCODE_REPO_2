'''
# 930. Binary Subarrays With Sum
# URL := https://leetcode.com/problems/binary-subarrays-with-sum/description/
# Intuition : Two pointers, sliding window, linear scan, running summation, Hashmap
# Complexity
# Let N := len(nums)
# T = O(N)
# S = O(N) ( E ) O(1) ( I ) 

Capture singleton case properly too!
'''
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        numSubArr = 0
        prefixSumFreq = dict()
        # default case of the '0' goal too :-) 
        prefixSumFreq[0] = 1
        prefixSum = 0
        for num in nums:
            # 1. Execute calculation to goal state : how often is the goal inside
            prefixSum += num
            target = prefixSum - goal
            if(target in prefixSumFreq):
                targetFreq = prefixSumFreq[target]
                numSubArr += targetFreq
            # 2. Update frequency
            if(prefixSum not in prefixSumFreq):
                prefixSumFreq[prefixSum] = 0
            prefixSumFreq[prefixSum] += 1
        return numSubArr
