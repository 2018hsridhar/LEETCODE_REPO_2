Complexity
Let N:= length of input list

Time complexity:
O(N)

Space complexity:
O(1) ( Explicit and Implicit )

Code
'''
URL := https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
3191. Minimum Operations to Make Binary Array Elements Equal to One I
'''
class Solution:
    # hint : think inducitvely
    def minOperations(self, nums: List[int]) -> int:
        # do not read the final two indices ( test both are zeroed out as well !)
        minOps = 0
        for idx in range(len(nums) - 2):
            if(nums[idx] == 0):
                minOps += 1
                nums[idx] = 1 - nums[idx]
                nums[idx+1] = 1 - nums[idx+1]
                nums[idx+2] = 1 - nums[idx+2]
        if(not(nums[-1] == 1 and nums[-2] == 1)):
            return -1
        return minOps
