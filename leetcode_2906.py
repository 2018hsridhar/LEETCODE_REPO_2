'''
URL := https://leetcode.com/problems/construct-product-matrix/description/
2906. Construct Product Matrix

Leverage property : (a*b)modn = (amodn) * (bmodn) 
Commutative property and associative property

Complexity
M = len(grid)
N = len(grid[0])
T = O(MN)
S = O(MN) ( E ) O(1) ( I ) 
'''
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # put a const in syntax where needed
        MODULO = 12345
        numRows = len(grid)
        numCols = len(grid[0])
        finalProducts = [[1 for c in range(numCols)] for r in range(numRows)]
        rowProds = [1 for r in range(numRows)]
        for i in range(numRows):
            runModProd = 1
            for j in range(numCols):
                curMod = (grid[i][j] % MODULO)
                runModProd *= curMod
            rowProds[i] = runModProd
        # Populate from the left
        for r in range(numRows):
            runModProdLeft = 1
            for c in range(numCols):
                finalProducts[r][c] *= runModProdLeft
                curMod = (grid[r][c] % MODULO)
                runModProdLeft *= curMod
        # Populate from the right
        for r in range(numRows):
            runModProdRight = 1
            for c in range(numCols - 1, -1, -1):
                finalProducts[r][c] *= runModProdRight
                curMod = (grid[r][c] % MODULO)
                runModProdRight *= curMod
        # populate from above
        runModAbove = 1
        for r in range(numRows):
            for c in range(numCols):
                finalProducts[r][c] *= runModAbove
            curMod = rowProds[r]
            runModAbove *= curMod
        # populate from below
        runModBelow = 1
        for r in range(numRows-1,-1,-1):
            for c in range(numCols):
                finalProducts[r][c] *= runModBelow
            curMod = rowProds[r]
            runModBelow *= curMod
        # final adjust
        for r in range(numRows):
            for c in range(numCols):
                finalProducts[r][c] = finalProducts[r][c] % MODULO
        return finalProducts
        
