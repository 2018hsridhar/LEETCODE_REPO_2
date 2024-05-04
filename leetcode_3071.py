'''
URL := https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/description/
3071. Minimum Operations to Write the Letter Y on a Grid

Category : Enumeration, Loops, Counting, Modular Arithmetic

Complexity
Let N := grid dimensions : row and col
Time := O(N^2)
Space := O(1) ( E & I ) 
'''
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        yCount = [0,0,0]
        notYCount = [0,0,0]
        m = len(grid)
        n = len(grid[0])
        # huge upper bound : all cells, theoretically speaking ( is a known ) 
        myMinOps = n*n
        for i in range(0,m,1):
            for j in range(0,n,1):
                cellVal = grid[i][j]
                status = self.isAYCell(i,j,grid)
                # print("At i = " + str(i) + ", j = " + str(j) + "\t status = " + str(status))
                if(status):
                    # gaaah all concats for to be strings here
                    yCount[cellVal] += 1
                else:
                    notYCount[cellVal] += 1
        # print(yCount)
        # print(notYCount)
        # expectedVal : [0,1,2]
        for expectedVal in range(len(yCount)):
            offOne = (expectedVal + 1) % 3
            offTwo = (expectedVal + 2) % 3
            # say this is to 0 : count <1>,<2>
            yToExpected = yCount[offOne] + yCount[offTwo]
            # and get count 1 ( for all else ) and count 2 ( for all else )
            # always use the expected value : we can not equal this out of bounds
            # can use either offOne or offTwo -> both can operate
            notYToExpectedOne = notYCount[expectedVal] + notYCount[offOne]
            notYToExpectedTwo = notYCount[expectedVal] + notYCount[offTwo]
            myMinOps = min(myMinOps, yToExpected + notYToExpectedOne)
            myMinOps = min(myMinOps, yToExpected + notYToExpectedTwo)
        return myMinOps

    # compiler "name not defined" issues gaah!
    def isAYCell(self, i:int, j:int, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # floor() func gaaah
        centerX = floor(m/2)
        centerY = floor(n/2)
        meetsCriteria = False
        if(i == j and i <= centerX):
            meetsCriteria = True
        elif(j == n - 1 - i and i <= centerX):
            meetsCriteria = True
        elif(i >= centerX and j == centerY):
            meetsCriteria = True
        return meetsCriteria

        
