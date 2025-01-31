'''
URL := https://leetcode.com/problems/beautiful-towers-ii/description/
2866. Beautiful Towers II

Categories : Array, Two Pointers, Stack, Monotonic Stack

Complexity
N = len(input)
T = O(N)
S = O(N) ( Explicit ) O(1) ( Implicit ) 

Mono stack : 
[6]
[5,5]
[3,3,3]
[3,3,3,9]
[2,2,2,2,2]
[2,2,2,2,2,7]
type of thinking 
'''
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        maxSum = 0
        n = len(maxHeights)
        sumOfHeights = [0 for idx in range(len(maxHeights))]
        leftHeights = [0 for idx in range(len(maxHeights))]
        rightHeights = [0 for idx in range(len(maxHeights))]
        monoStackLeft = []
        leftHeightSum = 0
        for index, height in enumerate(maxHeights):
            left = index
            right = index
            while(len(monoStackLeft) > 0):
                [mrHeight,mrLeft,mrRight] = monoStackLeft[-1]
                if(mrHeight >= height):
                    del monoStackLeft[-1]
                    leftHeightSum -= mrHeight * (mrRight - mrLeft + 1)
                    left = mrLeft
                else:
                    break
            record = [height,left,right]
            monoStackLeft.append(record)
            curWindow = right - left + 1
            leftHeightSum += height * curWindow
            leftHeights[index] = leftHeightSum
        rightHeightSum = 0
        monoStackRight = []
        for index in range(len(maxHeights) - 1, -1,-1):
            height = maxHeights[index]
            left = index
            right = index
            while(len(monoStackRight) > 0):
                [mrHeight,mrLeft,mrRight] = monoStackRight[-1]
                if(mrHeight >= height):
                    del monoStackRight[-1]
                    rightHeightSum -= mrHeight * (mrRight - mrLeft + 1)
                    right = mrRight
                else:
                    break
            record = [height,left,right]
            monoStackRight.append(record)
            curWindow = right - left + 1
            rightHeightSum += height * curWindow
            rightHeights[index] = rightHeightSum
        for index in range(n):
            curMountain = maxHeights[index]
            if(index -1 >= 0 and maxHeights[index-1] <= maxHeights[index]):
                curMountain += leftHeights[index-1]
            if(index+1 < n and maxHeights[index] >= maxHeights[index+1]):
                curMountain += rightHeights[index+1]
            maxSum = max(maxSum,curMountain)
        return maxSum





                
            
            
        
