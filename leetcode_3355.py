'''
URL := https://leetcode.com/problems/zero-array-transformation-i/
3355. Zero Array Transformation I

Complexity
T = O(N)
S = O(N) ( Exp ) O(1) ( Imp ) 

Process queries sequentially ( trick here ) - we can choos no selection too
Always decrement the value
can check : (val - curSum <= 0) ( if curSum >= val )
if curSum < val and val = 0, also ok too
'''
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        canTransform = True
        n = len(nums)
        prefixSums = [0 for idx in range(len(nums))]
        for [left,right] in queries:
            prefixSums[right] += 1
            if(left - 1 >= 0):
                prefixSums[left-1] -= 1
        runSum = 0
        for index in range(len(prefixSums) - 1, -1,-1):
            runSum += prefixSums[index]
            curVal = nums[index]
            passQueryStatus = (curVal == 0 or (0 < curVal and curVal <= runSum))
            if(passQueryStatus == False):
                canTransform = False
                break
        return canTransform
