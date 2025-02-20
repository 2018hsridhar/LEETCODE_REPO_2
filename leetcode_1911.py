'''
1911. Maximum Alternating Subsequence Sum
URL := https://leetcode.com/problems/maximum-alternating-subsequence-sum/

Approach & Categories : Arrays, Recursion, Dynamic Programming

Complexity
N = len(input)
T = O(N)
S = O(N) ( Exp ) O(1) ( Imp ) 

Intuition :
- Have to handle for both positive cases and negative cases
- Think : if we select an element as starter, it's x + bestNegCase
- Else if no select, it's bestRunningPositiveCase
'''
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        mas = 0
        n = len(nums)
        dp = [[0 for i in range(n)] for j in range(2)]
        # print(dp)
        # base case = the first element
        posIdx = 0
        negIdx = 1
        dp[posIdx][-1] = nums[-1]
        dp[negIdx][-1] = -1 * nums[-1]
        bestPosSum = dp[posIdx][-1]
        bestNegSum = dp[negIdx][-1]
        mas = max(bestPosSum,bestNegSum)
        for idx in range(len(nums) - 2, -1, -1):
            startVal = nums[idx]
            # why isn't an element considered individual here either. huh?
            curPosSum = max(startVal,startVal + bestNegSum)
            # The bug was here! CAUGHT IT !!!!
            curNegSum = max(-1*startVal, -1 * startVal + bestPosSum)
            bestPosSum = max(bestPosSum,curPosSum)
            bestNegSum = max(bestNegSum,curNegSum)
            dp[posIdx][idx] = bestPosSum
            dp[negIdx][idx] = bestNegSum
            # always start with positive element
            mas = max(mas,bestPosSum)
        return mas
