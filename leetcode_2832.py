Intuition and Approach
See problem code

Complexity
Let N:= length of the input array

Time complexity:

O(N)

Space complexity:

O(N) ( Explicit )

O(1) ( Implicit )

Code
'''
Intuition and Approach :

30 minutes to solutioning :-)
URL := https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/description/
2832. Maximal Range That Each Element Is Maximum in It

'''
class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        toTheLeft = self.solveRangeValuesLeft(nums)
        toTheRight = self.solveRangeValuesRight(nums)
        deltas = [-1 for i in range(len(nums))]
        for idx in range(len(nums)):
            deltas[idx] = abs(toTheLeft[idx] - toTheRight[idx]) + 1
        return deltas
    
    def solveRangeValuesRight(self, nums: List[int]) -> List[int]:
        rightMostValues = []
        monoStackLeft = []
        for idx in range(len(nums) - 1, -1,-1):
            val = nums[idx]
            rightMostIdx = idx
            record = [val,idx]
            if(len(monoStackLeft) == 0):
                monoStackLeft.append(record)
                rightMostValues.append(rightMostIdx)
            else:
                while(len(monoStackLeft) > 0):
                    topRecord = monoStackLeft[-1]
                    topRecVal = topRecord[0]
                    topRecIdx = topRecord[1]
                    if(val >= topRecVal):
                        monoStackLeft.pop(len(monoStackLeft) - 1)
                        rightMostIdx = topRecIdx
                    else:
                        rightMostIdx = topRecIdx - 1
                        break
                if(len(monoStackLeft) == 0):
                    rightMostIdx = len(nums) - 1
                # must always start with new index
                monoStackLeft.append(record)
                rightMostValues.append(rightMostIdx)
        rightMostValues.reverse()
        return rightMostValues

    def solveRangeValuesLeft(self, nums: List[int]) -> List[int]:
        leftMostValues = []
        monoStackRight = []
        for idx,val in enumerate(nums):
            leftMostIdx = idx
            record = [val,idx]
            if(len(monoStackRight) == 0):
                monoStackRight.append(record)
                leftMostValues.append(leftMostIdx)
            else:
                while(len(monoStackRight) > 0):
                    topRecord = monoStackRight[-1]
                    topRecVal = topRecord[0]
                    topRecIdx = topRecord[1]
                    if(val >= topRecVal):
                        monoStackRight.pop(len(monoStackRight) - 1)
                        leftMostIdx = topRecIdx
                    else:
                        leftMostIdx = topRecIdx + 1
                        break
                if(len(monoStackRight) == 0):
                    leftMostIdx = 0
                # must always start with new index
                monoStackRight.append(record)
                leftMostValues.append(leftMostIdx)
        return leftMostValues


        
