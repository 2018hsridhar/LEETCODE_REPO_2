'''
URL := https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/description/
3627. Maximum Median Sum of Subsequences of Size 3

nums = [2,1,3,2,1,3]
nums = [1,1,2,2,3,3] => max median = 5
    SELECTION : 1,3,3 => 3
    1,2,2 => 2
It seems greedy, sort, and ordering ~ the largest element and the smallest element = discard
    in that case, evict (smallest, largest 2 next )

Complexity
N = len(input)
T = O(NLgN)
S = O(1) ( E ) O(1) ( I ) 
'''
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x : (1 * x))
        mms = 0
        n = len(nums)
        leftPtr = 0
        rightPtr = n - 1
        numOps = (int)(n / 3)
        for x in range(numOps):
            secondLastEl = nums[rightPtr - 1]
            mms += secondLastEl
            leftPtr += 1
            rightPtr -= 2
        return mms
