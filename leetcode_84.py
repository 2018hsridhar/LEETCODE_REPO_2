'''
84. Largest Rectangle in Histogram
URL := https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Complexity
N = len(input)
T = O(N)
S = O(N) ( E ) O(1) ( I ) 

Intuition :
For each rectangle, find how left and how right you can go, for it's given height
Stop once you can not go in either or direction
This def a commonly occuring interview question too!!!
'''
class Solution:
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
