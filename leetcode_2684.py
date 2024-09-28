Intuition and Approach
See title

Complexity
Let M, N := dimensions(input)

Time complexity:
O(MN)

Space complexity:
O(MN) ( Explicit )
O(1) (Implicit)

Code
'''
URL := https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/
2684. Maximum Number of Moves in a Grid

Category : Iterative, Dynamic Programming, Recursion, Greedy, Maximization ( Optimization ) 

Complexity : 
Let M, N := dims(grid)
Time = O(MN)
Space = O(MN) ( E ) O(1) ( I ) 
'''

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        maxNumMoves = 0
        m = len(grid)
        n = len(grid[0])
        # sometimes it's a read from the parent too
        cache = [[0 for i in range(n)] for j in range(m)]
        # set lst col to 0 : no traversal possible
        lastCol = n - 1
        firstCol = 0
        for row in range(m):
            cache[row][lastCol] = 0
        dirs = [[-1,1],[0,1],[1,1]]
        # read rows any order
        for j in range(n-2,-1,-1):
            # read columns backwards
            for i in range(m):
                curVal = grid[i][j]
                parentProblem = 0
                for dirVal in dirs:
                    childR = i + dirVal[0]
                    childC = j + dirVal[1]
                    if(self.isInBounds(childR,childC,grid)):
                        childVal = grid[childR][childC]
                        if(childVal > curVal):
                            subProblem = cache[childR][childC]
                            parentProblem = max(parentProblem, 1 + subProblem)
                cache[i][j] = parentProblem
                if(j == firstCol):
                    maxNumMoves = max(maxNumMoves, cache[i][firstCol])
        return maxNumMoves

    def isInBounds(self, r:int, c:int, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        return ((0 <= r and r < m) and (0 <= c and c < n))
