'''
URL := https://leetcode.com/problems/maximal-rectangle/
85. Maximal Rectangle

It's a natural extension question
R := #-rows
C := #-cols
Space ( ignore memCopy for datatype converesion ) : O(R)
T = O(RC)
'''
class Solution:
    # Damn why a string rep ( that's dumb )
    # Ignore the conversion step :-) 
    def maximalRectangle(self, input: List[List[str]]) -> int:
        numRows = len(input)
        numCols = len(input[0])
        matrix = [[(int)(input[r][c]) for c in range(numCols)] for r in range(numRows)]
        for c in range(numCols):
            for r in range(numRows):
                curVal = matrix[r][c]
                matrix[r][c] = curVal
                if(curVal > 0 and r - 1 >= 0):
                    matrix[r][c] += matrix[r-1][c]
        myMaximalRect = 0
        for row in range(numRows):
            curRow = matrix[row][:]
            curRowBestHeight = self.largestRectangleArea(curRow)
            myMaximalRect = max(myMaximalRect, curRowBestHeight)
        return myMaximalRect

        
    def largestRectangleArea(self, heights: List[int]) -> int:
        # the left pass
        largestRect = 0
        monoStack = []
        areaToLeft = [0 for idx in range(len(heights))]
        areaToRight = [0 for idx in range(len(heights))]
        # [1] Handle the left case
        for index, curHeight in enumerate(heights):
            leftIndex = index
            rightIndex = index
            while(len(monoStack) > 0):
                mostRecentRec = monoStack[-1]
                mostRecentHeight = mostRecentRec[0]
                if(mostRecentHeight < curHeight):
                    break
                else:
                    leftIndex = mostRecentRec[1]
                    del monoStack[-1]
            leftWindow = abs(rightIndex - leftIndex + 1)
            monoStack.append([curHeight,leftIndex,rightIndex])
            areaToLeft[index] = leftWindow
        # [2] Handle the right case
        # Isn't enumearte(...) obj reversible?
        monoStack = []
        n = len(heights)
        for index in range(len(heights) -1, -1,-1):
            curHeight = heights[index]
            leftIndex = index
            rightIndex = index
            while(len(monoStack) > 0):
                mostRecentRec = monoStack[-1]
                mostRecentHeight = mostRecentRec[0]
                if(mostRecentHeight < curHeight):
                    break
                else:
                    rightIndex = mostRecentRec[2]
                    del monoStack[-1]
            monoStack.append([curHeight,leftIndex,rightIndex])
            rightWindow = abs(rightIndex - leftIndex + 1)
            areaToRight[index] = rightWindow
        for index, height in enumerate(heights):
            totalWidth = areaToLeft[index] + areaToRight[index] - 1
            curRectArea = totalWidth * height
            largestRect = max(largestRect, curRectArea)
        return largestRect
