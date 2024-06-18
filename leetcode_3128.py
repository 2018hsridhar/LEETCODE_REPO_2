'''
3128. Right Triangles
URL := https://leetcode.com/problems/right-triangles/description/

Seems prefix sum based TBH ( elements need not have adjacency to one another )
Complexity
Let M, N := dim (grid )
T = O(MN)
S = O(MN) ( E ) O(1) ( I ) 

'''
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        numRightTri = 0
        m = len(grid)
        n = len(grid[0])
        numOnesNorth = [[0 for j in range(n)] for i in range(m)]
        numOnesSouth = [[0 for j in range(n)] for i in range(m)]
        numOnesEast = [[0 for j in range(n)] for i in range(m)]
        numOnesWest = [[0 for j in range(n)] for i in range(m)]
        # [1] populate ones north
        # [2] populate ones south
        for c in range(n):
            oneNorth = 0
            oneSouth = 0
            for r in range(m):
                numOnesNorth[r][c] = oneNorth
                oneNorth += (int)(grid[r][c])
            for r in range(m-1,-1,-1):
                numOnesSouth[r][c] = oneSouth
                oneSouth += (int)(grid[r][c])
        # [3] populate ones west
        # [4] populate ones east
        for r in range(m):
            oneWest = 0
            for c in range(n):
                numOnesWest[r][c] = oneWest
                oneWest += (int)(grid[r][c])
            oneEast = 0
            for c in range(n-1,-1,-1):
                numOnesEast[r][c] = oneEast
                oneEast += (int)(grid[r][c])
        for r in range(m):
            for c in range(n):
                if(grid[r][c] == 1):
                    numNorthEast = numOnesNorth[r][c] * numOnesEast[r][c]
                    numSouthEast = numOnesSouth[r][c] * numOnesEast[r][c]
                    numNorthWest = numOnesNorth[r][c] * numOnesWest[r][c]
                    numSouthWest = numOnesSouth[r][c] * numOnesWest[r][c]
                    numRightTri += sum([numNorthEast, numSouthEast, numNorthWest, numSouthWest])
        return numRightTri
