'''
URL := https://leetcode.com/problems/maximum-array-hopping-score-i/description/
3205. Maximum Array Hopping Score I

Category
N = len(nums)
T = O(pow(N,2))
S = O(N) ( E ) O( 1 ) ( I ) 
BUDP Techniques
'''
import math

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ms = float("-inf")
        n = len(nums)
        FLAG_VALUE = float("-inf") # 
        START = 0
        dp = [FLAG_VALUE for idx in range(n)]
        for i in range(len(nums) - 1, -1, -1):
            curVal = nums[i]
            parentProblem = 0 # min score := 0 by default
            for j in range(i+1,n,1):
                jumpDist = abs(i - j)
                jumpProfit = jumpDist * nums[j]
                childProblem = jumpProfit + dp[j]
                parentProblem = max(parentProblem, childProblem)
            dp[i] = parentProblem
        ms = dp[START]
        return ms
        
