'''
URL := https://leetcode.com/problems/climbing-stairs-ii/description/
3693. Climbing Stairs II

Complexity
Let N := len(costs)
T = O(N)
S = O(N) ( E ) O(1) ( I ) [ coudl be BUDP TBH ] 
'''
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        FLAG_VALUE = float("-inf")
        numStairs = n + 1
        DP = [FLAG_VALUE for idx in range(numStairs)]
        DP[0] = 0 # Init condition # default ) 
        for idx in range(1, numStairs, 1):
            parentProblemCost = float('inf') # huh only floats take large data TBH
            stepIndices = [idx-1,idx-2,idx-3]
            costJ = costs[idx - 1] # offsetting here needed
            costArray = []
            for stepIdx in stepIndices:
                if(stepIdx >= 0):
                    delta = abs(idx - stepIdx)
                    stepCost = costJ + (delta**2) + DP[stepIdx]
                    parentProblemCost = min(parentProblemCost, stepCost)
            DP[idx] = parentProblemCost
        minStairClimbCost = DP[-1]
        return minStairClimbCost
