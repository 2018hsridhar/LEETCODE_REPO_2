'''
840. Magic Squares In Grid
URL := https://leetcode.com/problems/magic-squares-in-grid/description/

This classifies on easier end of a medium -> but let's solution leveraging prefix sums ( to scale)
20 mins ( coding and debugging )
'''
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        numMagicSquares = 0
        rowSums = self.getRowSums(grid)
        colSums = self.getColSums(grid)
        bottomRightSums = self.getBottomRight(grid)
        upperRightSums = self.getUpperRight(grid)

        offset = 3
        # and check numbers are distinct
        for i in range(2,m,1):
            for j in range(2,n,1):
                # 3 steps up and left
                gridNumbers = set()
                minVal = 1
                maxVal = 9
                for x in range(i,i-3,-1):
                    for y in range(j,j-3,-1):
                        gridNumbers.add(grid[x][y])
                        minVal = min(minVal,grid[x][y])
                        maxVal = max(maxVal,grid[x][y])
                allDistinct = (len(gridNumbers) == 9 and minVal == 1 and maxVal == 9)
                sumSet = set()
                # rowSums
                for x in range(offset):
                    rowSum = rowSums[i-x][j]
                    if(j - offset >= 0):
                        rowSum -= rowSums[i-x][j-offset]
                    sumSet.add(rowSum)

                # colSums
                for x in range(offset):
                    colSum = colSums[i][j-x]
                    if(i - offset >= 0):
                        colSum -= colSums[i-offset][j-x]
                    sumSet.add(colSum)

                # bomttomRight
                bottomRightSum = bottomRightSums[i][j]
                if(i-offset >= 0 and j-offset >= 0):
                    bottomRightSum -= bottomRightSums[i-offset][j-offset]
                sumSet.add(bottomRightSum)

                # topRightSum
                topRightSum = upperRightSums[i-2][j]
                if(i-2+offset >= 0 and i-2+offset < m and j-offset >= 0):
                    topRightSum -= upperRightSums[i-2+offset][j-offset]
                sumSet.add(topRightSum)
                if(len(sumSet) == 1 and allDistinct):
                    numMagicSquares += 1
        return numMagicSquares




    def getBottomRight(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        brSums = [[grid[i][j] for j in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                brSums[i][j] += brSums[i-1][j-1]
        return brSums

    def getUpperRight(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        urSums = [[grid[i][j] for j in range(n)] for i in range(m)]
        for i in range(m-2,-1,-1):
            for j in range(1,n,1):
                urSums[i][j] += urSums[i+1][j-1]
        return urSums

    def getRowSums(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        rowSums = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            runSum = 0
            for j in range(n):
                runSum += grid[i][j]
                rowSums[i][j] = runSum
        return rowSums
        
    def getColSums(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        colSums = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            runSum = 0
            for i in range(m):
                runSum += grid[i][j]
                colSums[i][j] = runSum
        return colSums
