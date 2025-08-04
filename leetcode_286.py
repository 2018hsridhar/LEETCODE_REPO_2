'''
URL := https://leetcode.com/problems/walls-and-gates/description/
286. Walls and Gates

Distance to nearest gate ( or INF ) if unreachable
Complexity
T = O(MN)
S = O(MN) ( E ) O(1) ( I ) 
'''
class Solution:

    def isInBounds(self,r,c,grid) -> bool:
        caseOne = (0 <= r and r < len(grid))
        caseTwo = (0 <= c and c < len(grid[0]))
        inGrid = (caseOne and caseTwo)
        return inGrid

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # wall or obstacle
        WALL = -1 
        GATE = 0
        # Check if value holds true
        EMPTY = 2147483647
        ROOT_LEVEL = 0
        m = len(rooms)
        n = len(rooms[0])
        lot = []
        for r in range(m):
            for c in range(n):
                if(rooms[r][c] == GATE):
                    record = [r,c,ROOT_LEVEL]
                    lot.append(record)
        # bfs it now ( level strictly incr :-) ) 
        dirs = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1]
        ]
        while(len(lot) > 0):
            parent = lot.pop(0)
            [pr,pc,pl] = parent
            cl = pl + 1
            for dx,dy in dirs:
                cr = pr + dx
                cc = pc + dy
                if(self.isInBounds(cr,cc,rooms)):
                    if(rooms[cr][cc] == EMPTY):
                        rooms[cr][cc] = cl
                        childRec = [cr,cc,cl]
                        lot.append(childRec)
