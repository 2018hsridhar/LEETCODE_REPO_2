'''
URL := https://leetcode.com/problems/right-triangles/description/
3128. Right Triangles

Complexity
Let M, N := dims(grid)
Time := O(MN)
S := O(1) ( I & E ) 

Commit Message :
    # Why is PY3 ruled by definitions and lambda styles for functions?
    # Typing out 'and' and 'or' seen as safer lang choices over '&' and '|' statements.
    # A semi-colon ':' governed language
    # self : referential to the name of own class ( in this case, Solution )

Oh -> it's actuall a count of 1's to the right and to the left : the problem simplifies

15 minutes -> go do this problem later. 
'''
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        nort = 0
        # 0-init list comp style
        oneCountBelow = [[0 for i in range(len(grid))] for j in range(len(grid[0]))]
        oneCountAbove = [[0 for i in range(len(grid))] for j in range(len(grid[0]))]
        oneCountRight = [[0 for i in range(len(grid))] for j in range(len(grid[0]))]
        oneCountLeft = [[0 for i in range(len(grid))] for j in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nort += self.getNorthEastStatus(grid,i,j)
                nort += self.getSouthEastStatus(grid,i,j)
                nort += self.getNorthWestStatus(grid,i,j)
                nort += self.getSouthWestStatus(grid,i,j)
        return nort
    
    def getNorthEastStatus(self, grid: List[List[int]], x:int, y:int) -> int:
        status = 0
        if(self.isInBounds(grid,x,y) and self.isInBounds(grid,x+1,y) and self.isInBounds(grid,x+1,y+1)):
            if(grid[x][y] == 1 and grid[x+1][y] == 1 and grid[x+1][y+1] == 1):
                status = 1
        return status

    def getSouthEastStatus(self, grid: List[List[int]], x:int, y:int) -> int:
        status = 0
        if(self.isInBounds(grid,x,y) and self.isInBounds(grid,x-1,y) and self.isInBounds(grid,x-1,y+1)):
            if(grid[x][y] == 1 and grid[x-1][y] == 1 and grid[x-1][y+1] == 1):
                status = 1
        return status

    def getNorthWestStatus(self, grid: List[List[int]], x:int, y:int) -> int:
        status = 0
        if(self.isInBounds(grid,x,y) and self.isInBounds(grid,x+1,y) and self.isInBounds(grid,x+1,y-1)):
            if(grid[x][y] == 1 and grid[x+1][y] == 1 and grid[x+1][y-1] == 1):
                status = 1
        return status

    def getSouthWestStatus(self, grid: List[List[int]], x:int, y:int) -> int:
        status = 0
        # written as for loop -> fixed range -> avoid branch logic -> more optimized under hood
        if(self.isInBounds(grid,x,y) and self.isInBounds(grid,x-1,y) and self.isInBounds(grid,x-1,y-1)):
            if(grid[x][y] == 1 and grid[x-1][y] == 1 and grid[x-1][y-1] == 1):
                status = 1
        return status

    def isInBounds(self, grid: List[List[int]], x:int, y:int) -> bool:
        m = len(grid)
        n = len(grid[0])
        return (0 <= x and x < m) and (0 <= y and y < n)
