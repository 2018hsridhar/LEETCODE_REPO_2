'''
2865. Beautiful Towers I
https://leetcode.com/problems/beautiful-towers-i/description/

18 minutes TTS : Time-To-Solutioning

'''
class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        bestHeightMaxSum = 0
        prefixSumLeft = 0
        leftMaxValue = []
        leftSum = []
        rightSum = []
        rightMaxValue = []
        prefixSumRight = 0
        # Pass 1 : given a height, find the permissible building heights allow
        # Set up initial sums ( to the left ) ( at a given index ) 
        for rightIndex, height in enumerate(heights):
            record = [height, rightIndex,rightIndex]
            leftBestIndex = rightIndex
            while(len(leftMaxValue) > 0):
                curBestRec = leftMaxValue[-1]
                prevVal = curBestRec[0]
                if(prevVal > height):
                    del leftMaxValue[-1]
                    prevDelta = curBestRec[2] - curBestRec[1] + 1
                    prefixSumLeft -= prevDelta * prevVal
                    leftBestIndex = curBestRec[1]
                else:
                    break
            record[1] = leftBestIndex
            leftMaxValue.append(record)
            delta = record[2] - record[1] + 1
            prefixSumLeft += delta * height
            leftSum.append(prefixSumLeft)
        # print(leftSum)
        # left Sum ( includes current building height) 
        # right sum ( can also include current building height) 
        # can decrement one later
        # revrse iteration : 
        for leftIndex in range(len(heights) - 1,-1,-1):
            height = heights[leftIndex]
            record = [height, leftIndex,leftIndex]
            rightBestIndex = leftIndex
            while(len(rightMaxValue) > 0):
                curBestRec = rightMaxValue[-1]
                prevVal = curBestRec[0]
                if(prevVal > height):
                    del rightMaxValue[-1]
                    prevDelta = curBestRec[2] - curBestRec[1] + 1
                    prefixSumRight -= prevDelta * prevVal
                    rightBestIndex = curBestRec[2]
                else:
                    break
            record[2] = rightBestIndex
            rightMaxValue.append(record)
            delta = record[2] - record[1] + 1
            prefixSumRight += delta * height
            rightSum.append(prefixSumRight)
        actualRightSum = list(reversed(rightSum))
        for idx in range(len(heights)):
            height = heights[idx]
            lS = leftSum[idx]
            rS = actualRightSum[idx]
            curSum = lS + rS - height
            bestHeightMaxSum = max(bestHeightMaxSum, curSum)
        return bestHeightMaxSum

