'''
1620. Coordinate With Maximum Network Quality
URL := https://leetcode.com/problems/coordinate-with-maximum-network-quality/description/

Approach, Constraints, and Intuition : 
50 towers at worst
Grid dimensinos at worst 50x50

For each integral coordinate, excecute BFS/DFS until we hit a radius at a given distance
Or flood fill instead, from each tower, and add value at each unvisted cell

15 minutes spent
How to represent our grid properly? SMH
You're on the dollar here :-) !!!
Get back to it later :-) !!!
'''
class Solution:

    def floodFill(self, tower:List[int], grid:List[List[int]], visited:List[List[bool]], radius:int):
        [tR,tC,quality] = tower
        queue = [[tR,tC]]
        dirs = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1]
        ]
        while(len(queue) > 0):
            [curR,curC] = queue[0]
            del queue[0]
            if(visited[curR][curC] == False):
                visited[curR][curC] = True
                dist = sqrt(pow((curR - tR),2) + pow((curC - tC),2))
                if(dist <= radius):
                    score = abs(quality / (1 + dist))
                    grid[curR][curC] += math.floor(score)
                for [dx,dy] in dirs:
                    childR = curR + dx
                    childC = curC + dy
                    if(self.isInBounds(childR,childC,grid)):
                        child = [childR,childC]
                        queue.append(child)

    def isInBounds(self, x:int,y:int,grid:List[List[int]]) -> bool:
        return ((0 <= x and x < len(grid)) and (0 <= y and y < len(grid[0])))

    # Close -> missing a few test cases oh gosh

    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # [1] Standard flood fill algorithm
        m = 51
        n = 51
        grid = [[0 for j in range(n)] for i in range(m)]
        for tower in towers:
            visited = [[False for j in range(n)] for i in range(m)]
            self.floodFill(tower,grid, visited, radius)
        # [2] Modularizable -> get the best coordinate
        bestCoord = [float('inf'),float('inf')]
        bestQuality = 0
        for r in range(m):
            for c in range(n):
                cellQuality = grid[r][c]
                if(cellQuality > bestQuality):
                    bestQuality = cellQuality
                    bestCoord[0] = r
                    bestCoord[1] = c
                elif(cellQuality == bestQuality):
                    bestQuality = cellQuality
                    if(r < bestCoord[0]):
                        bestCoord[0] = r
                        bestCoord[1] = c
                    elif(r == bestCoord[0] and c < bestCoord[1]):
                        bestCoord[0] = r
                        bestCoord[1] = c
        return bestCoord

        
