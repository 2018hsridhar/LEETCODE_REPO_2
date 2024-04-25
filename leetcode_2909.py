'''
URL := https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/
2909. Minimum Sum of Mountain Triplets II

Category : Linear Scan, Greedy, Two Pass

Complexity : 
Let N := len(nums)
T = O(N)
S = O(N) ( E ) O(1) ( I )

'''
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minSum = float('inf')
        leftMins = [float('inf') for i in range(len(nums))]
        rightMins = [float('inf') for i in range(len(nums))]
        obsMin = float('inf')
        for i in range(len(nums)):
            leftMins[i] = obsMin
            obsMin = min(obsMin,nums[i])
        obsMin = float('inf')
        for i in range(len(nums) - 1, -1,-1):
            rightMins[i] = obsMin
            obsMin = min(obsMin, nums[i])
        for i in range(0,len(nums),1):
            if(leftMins[i] < nums[i] and nums[i] > rightMins[i]):
                curSum = leftMins[i] + nums[i] + rightMins[i]
                minSum = min(minSum, curSum)
        return -1 if (minSum == float('inf')) else minSum
        
