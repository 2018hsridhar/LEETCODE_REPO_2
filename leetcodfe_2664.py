'''
URL := https://leetcode.com/problems/the-knights-tour/description/
2664. The Knight’s Tour

Approach and Intuition -> DFS/BFS, State Space Exploration, Graphs
Each cell visit once ( starting cell already visited ) 

M, N are small enough inputs for a recursive solution
15 minutes
close, but not getting some knight movement here exactly ??? HUH
'''
class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        startR = r
        startC = c
        # Favorite way of initialization of tiny lists in Python3
        # get all knight moves too
        dirs = [
            [1,2],
            [1,-2],
            [-1,2],
            [-1,-2],
            [2,1],
            [2,-1],
            [-2,1],
            [-2,-1],
        ]
        seqNum = 0
        # Hack at grid initialization
        board = [[-1 for j in range(n)] for i in range(m)]
        knightTour = self.dfs(board, startR,startC,dirs, seqNum)
        return board

    def dfs(self, grid:List[List[int]], curR:int, curC:int, dirs:List[List[int]], seqNum:int) -> bool:
        assignableCell = False
        if(grid[curR][curC] == -1):
            m = len(grid)
            n = len(grid[0])
            grid[curR][curC] = seqNum
            # found an assignation here
            if(seqNum == (m * n) - 1):
                return True
            childSeqNum = seqNum + 1
            for [dx,dy] in dirs:
                childR = curR + dx
                childC = curC + dy
                if(self.isInBounds(childR, childC, grid)):
                    assignableCell = assignableCell or self.dfs(grid,childR,childC,dirs,childSeqNum)
            if(not assignableCell):
                grid[curR][curC] = -1
        return assignableCell

    # Nicest lambda function I've ever seen
    def isInBounds(self, x:int, y:int, grid:List[List[int]]) -> bool:
        return ((0 <= x and x < len(grid)) and (0 <= y and y < len(grid[0])))
        
        
