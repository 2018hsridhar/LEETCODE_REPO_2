Intuition and Approach
Think of Kadane's algorithm here

Complexity
N:= len(input list)

Time complexity:
O(N)

Space complexity:
O(1) ( Explicit and Implicit )

Code
'''
URL := https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
1749. Maximum Absolute Sum of Any Subarray

A variation of Kadane's algorithm, but, with a slight twist/delta this time :-) 
'''
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mas = 0
        maxPositiveDist = 0
        maxNegativeDist = 0

        # (A) the positive case
        runSum = 0 
        for el in nums:
            runSum += el
            if(runSum > 0):
                maxPositiveDist = max(maxPositiveDist,runSum)
            else:
                runSum = 0

        # (B) the negative case
        runSum = 0 
        for el in nums:
            runSum += el
            if(runSum < 0):
                maxNegativeDist = min(maxNegativeDist,runSum)
            else:
                runSum = 0

        # print(maxPositiveDist)
        # print(maxNegativeDist)
        mas = max(abs(maxPositiveDist), abs(maxNegativeDist))

        return mas
        
