'''
URL := https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/description/
2874. Maximum Value of an Ordered Triplet II

Complexity : 
Let N := len(nums)
Time := O(N)
Space := O(N) ( E ) O(1) ( I ) 

Largest more positive value observed to one's lef
Largest more positive value to one's right

No value is negative, but a triplet evaluation can be negative. 
Ignore border cases -> eval only the center.

'''
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        mtv = 0
        # Iterable style syntax for list comprehension.
        largestLeft = [float('inf') for i in range(len(nums))]
        largestRight = [float('inf') for i in range(len(nums))]
        largestVal = float('-inf') # special values
        for i in range(0, len(nums), 1):
            largestLeft[i] = largestVal
            largestVal = max(largestVal, nums[i])
        largestVal = float('-inf') # dodge -1* multiplication step : faster init
        for i in range(len(nums) - 1, -1, -1):
            largestRight[i] = largestVal
            largestVal = max(largestVal, nums[i])
        for i in range(len(nums)):
            if largestLeft[i] != float('-inf') and largestRight[i] != float('-inf'):
                curTripletVal = (largestLeft[i] - nums[i]) * largestRight[i]
                if(curTripletVal >= 0):
                    mtv = max(mtv, curTripletVal)
        return mtv
        
