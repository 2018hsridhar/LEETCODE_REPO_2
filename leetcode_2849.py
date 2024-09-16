'''
2849. Determine if a Cell Is Reachable at a Given Time
URL := https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/description/
'''
Complexity
Time complexity:
O(1)

Space complexity:
O(1) ( Explicit )
O(1) ( Implicit )

Code
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        deltaY = abs(sy - fy)
        deltaX = abs(sx - fx)
        minMoves = max(deltaX,deltaY)
        status = True
        if(deltaX > 0 or deltaY > 0):
            status = (t >= minMoves)
        elif(deltaX == 0 and deltaY == 0):
            status = (t > 1) or ( t == 0)
        return status
        
