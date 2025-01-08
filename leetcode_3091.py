'''
URL := https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/description/
3091. Apply Operations to Make Sum of Array Greater Than or Equal to k

Compexity
T = O(K)
S = O(1) ( E ) O(1) ( I ) 

Leverage number theory, greedyness, and HINT #1 for its solutioning !!!
'''
class Solution:
    def minOperations(self, k: int) -> int:
        minNumOps = float('inf')
        # always start at base = 1 here!
        for incrementOp in range(1,k+1,1):
            incrOps = (incrementOp - 1)
            duplOps = max(0,(int)(math.ceil(k / incrementOp)) - 1)
            numOpsTotal = incrOps + duplOps
            minNumOps = min(minNumOps, numOpsTotal)
        return minNumOps
        
