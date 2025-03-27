'''
2087. Minimum Cost Homecoming of a Robot in a Grid
URL := https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/description/

Intuition :
- Resembles Manhattan distance in the hiding TBH
- Already know direction of movememnt : L-R-U-D

Complexity
M = #-rows, N = #-cols
Time = O(Max(M,N))
Space = O(1) ( E ) O(1 ) ( I ) 
'''
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        minPathCost = 0
        [sR,sC] = startPos
        [hR,hC] = homePos
        [rowStep,colStep] = [1,1]
        if(sR > hR):
            rowStep = -1
            hR = hR - 1
        else:
            rowStep = 1
            hR = hR + 1
        if(sC > hC):
            colStep = -1
            hC = hC - 1
        else:
            colStep = 1
            hC = hC + 1
        for row in range(sR,hR,rowStep):
            minPathCost += rowCosts[row]
        for col in range(sC,hC,colStep):
            minPathCost += colCosts[col]
        # ahhh discount the first move ( home position )
        minPathCost -= rowCosts[sR]
        minPathCost -= colCosts[sC]
        return minPathCost
        
