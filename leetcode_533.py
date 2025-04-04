'''
533. Lonely Pixel II
URL := https://leetcode.com/problems/lonely-pixel-ii/description/

The inputs to this problem are sufficiently tiny
Leverage hashmaps
Decompose into two steps
(A) Get each row with a column having `target` black pixels ( need not be consecutive ) 
(B) For each row meeting cond A, map to unique Keys and execute frequency counting

M = #-rows
N = #-cols
Time = O(MN)
Space = O(M)
# pixels meeting a condition hmmm
    - for each col, check number of unique rows hit : should be equal to one only
'''
class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        numLonelyBlack = 0
        m = len(picture)
        n = len(picture[0])
        BLACK = 'B'
        rowKeys = dict()
        # 1. Get row keys
        for row in range(m):
            colString = ''
            for col in range(n):
                colString += picture[row][col]
            if(row not in rowKeys):
                rowKeys[row] = colString
        # 2 Get row counts ( black pixel )
        # 3 Get col counts ( black pixel ) 
        # 4 iterate over cell and test both rules 
        # rules (2) and (3), then rule (1)
        rowCount = dict()
        colCount = dict()
        for row in range(m):
            rowBlackPixelCount = 0
            for col in range(n):
                if(picture[row][col] == BLACK):
                    rowBlackPixelCount += 1
            rowCount[row] = rowBlackPixelCount
        for col in range(n):
            colBlackPixelCount = 0
            for row in range(m):
                if(picture[row][col] == BLACK):
                    colBlackPixelCount += 1
            colCount[col] = colBlackPixelCount
        # Last step : it's a "rules engine" in the hiding
        for r in range(m):
            for c in range(n):
                if(picture[r][c] == BLACK):
                    ruleOne = (rowCount[r] == colCount[c] and rowCount[r] == target)
                    # the key count should be one ( in a given column ) 
                    uniqKeys = set()
                    for row, rowKey in enumerate(rowKeys):
                        if(picture[row][c] == BLACK):
                            uniqKeys.add(rowKeys[row])
                    ruleTwo = (len(uniqKeys) == 1)
                    meetsCond = (ruleOne and ruleTwo)
                    if(meetsCond):
                        numLonelyBlack += 1
        return numLonelyBlack
