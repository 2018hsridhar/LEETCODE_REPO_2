'''
URL := https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/
1926. Nearest Exit from Entrance in Maze

Complexity
M, N = dimensions(grid)
You'll know how to solution this :-) !!!

Distance from a point : LOT ( level-order traversal ) 
Wait ... why not lOT, but just from the entrace? Seems faster?
Check border cells at the end ( vice versa ) ?

'''
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Start from the border and treat empty cells as 'exits'
        # Ignore if cell_exit = cell_entrance
        shortestPath = float('inf')
        m = len(maze)
        n = len(maze[0])
        [eR,eC] = entrance
        EMPTY = '.'
        WALL = '+'
        frontier = []

        # the actual DFS/LOT traversal
        frontier.append([eR,eC,0])
        FLAG = -1
        # FLAG value can be wrong ( -1 if a cell not hit ) 
        # careful here too!
        distanceMap = [[FLAG for j in range(n)] for i in range(m)]
        dirs = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1]
        ]
        while(len(frontier) > 0):
            parent = frontier[0]
            [px,py,pr] = parent
            del frontier[0]
            if(distanceMap[px][py] == FLAG):
                distanceMap[px][py] = pr
                cr = pr + 1
                for [dx,dy] in dirs:
                    cx = px + dx
                    cy = py + dy
                    # if not out of bounds
                    if(self.isInBounds(cx,cy,m,n)):
                        if(maze[cx][cy] != WALL):
                            childRec = [cx,cy,cr]
                            frontier.append(childRec)
        # print(distanceMap)
        for r in range(m):
            for c in range(n):
                # crtieria conditions
                if(self.isBorderCell(r,c,m,n) and distanceMap[r][c] != FLAG and maze[r][c] != WALL):
                    if(not (r == eR and c == eC)):
                        curDist = distanceMap[r][c]
                        shortestPath = min(shortestPath,curDist)
        if(shortestPath == float('inf')):
            shortestPath = -1
        return shortestPath

    def isInBounds(self, r:int, c:int, m:int, n:int) -> bool:
        return ((0 <= r and r < m) and (0 <= c and c < n))

    def isBorderCell(self, r:int, c:int, m:int, n:int) -> bool:
        caseOne = (r == 0 or r == m - 1)
        caseTwo = (c == 0 or c == n-1)
        return (caseOne or caseTwo)

        
