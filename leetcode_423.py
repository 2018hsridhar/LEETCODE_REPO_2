'''
URL := https://leetcode.com/problems/01-matrix/description/
542. 01 Matrix


'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        # nearest 0, for each cell ( or it's 0 itself )
        # start a BFS/DFS for each 0 cell and expand outwards
        visited = dict()
        lot = []
        finalDistances = [[-1 for j in range(n)] for i in range(m)]
        for row in range(m):
            for col in range(n):
                if(mat[row][col] == 0):
                    lot.append([row,col])
        for row in range(m):
            visited[row] = set()
        rootLevel = 0
        dirs = [
            [1,0],
            [-1,0],
            [0,-1],
            [0,1]
        ]
        self.dfs(dirs,lot,rootLevel,visited,finalDistances)
        return finalDistances

    def dfs(self, dirs,lot, rootLevel,visited,finalDistances):
        childLot = []
        childLevel = rootLevel + 1
        # print(lot)
        if(len(lot) == 0):
            return
        else:
            for [pR,pC] in lot:
                if(pC not in visited[pR]):
                    # print('[ %s, %s]',%(pR,pC))
                    # print("Row = %s",%(pR))
                    # print("Row = " + (str)(pR) + "\t col = " + (str)(pC))
                    visited[pR].add(pC)
                    finalDistances[pR][pC] = rootLevel
                    for [dx,dy] in dirs:
                        cR = pR + dx
                        cC = pC + dy
                        if(self.isInBounds(cR,cC,finalDistances)):
                            childLot.append([cR,cC])
            self.dfs(dirs,childLot,childLevel,visited,finalDistances)

    def isInBounds(self, x,y,grid) -> bool:
        return ((0 <= x and x < len(grid)) and (0 <= y and y < len(grid[0])))



        
