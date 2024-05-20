'''
2789. Largest Element in an Array after Merge Operations
URL := https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/description/

Complexity :
Let N := len(nums)
Time := O(N)
Space := O(1) ( E ) O(1) ( I ) 

'''
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        mav = 0
        runningSum = 0
        for ptr in range(len(nums) - 1,-1,-1):
            runningSum += nums[ptr]
            if(ptr - 1 >= 0 and nums[ptr - 1] > runningSum):
                runningSum = 0
                # it will reset in the next step : start fresh 'as-is'
            mav = max(mav, runningSum)
        return mav
        
