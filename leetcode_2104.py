Intuition and Approach
Categories : Dynamic Programming, Stack, Monotonic Stack, Linear Scan
See problem title

Complexity
N:=length(input)

Time complexity:
O(N)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
'''
URL := https://leetcode.com/problems/sum-of-subarray-ranges/description/
2104. Sum of Subarray Ranges

'''
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        globalMinSum = self.getGlobalMinSums(nums)
        globalMaxSum = self.getGlobalMaxSums(nums)
        globalSumRanges = globalMaxSum - globalMinSum
        return globalSumRanges

    # [1] The minimas of ranges
    def getGlobalMinSums(self, nums:List[int]) -> int:
        n = len(nums)
        globalMinSum = 0
        minMonoStack = []
        minRunSum = 0
        curPtr = n - 1
        while(curPtr >= 0):
            curEl = nums[curPtr]
            rightMostPtr = curPtr
            while(len(minMonoStack) > 0):
                mostLeftRecord = minMonoStack[-1]
                mostLeftVal = mostLeftRecord[0]
                mostLeftPtr = mostLeftRecord[2]
                if(curEl <= mostLeftVal):
                    minMonoStack.pop()
                    mostLeftWindow = mostLeftPtr - mostLeftRecord[1] + 1
                    minRunSum -= (mostLeftVal * mostLeftWindow)
                    rightMostPtr = mostLeftPtr
                else:
                    break
            record = [curEl,curPtr,rightMostPtr]
            window = (rightMostPtr - curPtr + 1)
            minMonoStack.append(record)
            minRunSum += (window * curEl)
            globalMinSum += minRunSum
            curPtr -= 1
        return globalMinSum

    # [1] The maximas of ranges
    def getGlobalMaxSums(self, nums:List[int]) -> int:
        n = len(nums)
        maxMonoStack = []
        maxRunSum = 0
        globalMaxSum = 0
        curPtr = n - 1
        while(curPtr >= 0):
            curEl = nums[curPtr]
            rightMostPtr = curPtr
            while(len(maxMonoStack) > 0):
                mostLeftRecord = maxMonoStack[-1]
                mostLeftVal = mostLeftRecord[0]
                mostLeftPtr = mostLeftRecord[2]
                if(curEl >= mostLeftVal):
                    maxMonoStack.pop()
                    mostLeftWindow = mostLeftPtr - mostLeftRecord[1] + 1
                    maxRunSum -= (mostLeftVal * mostLeftWindow)
                    rightMostPtr = mostLeftPtr
                else:
                    break
            record = [curEl,curPtr,rightMostPtr]
            window = (rightMostPtr - curPtr + 1)
            maxMonoStack.append(record)
            maxRunSum += (window * curEl)
            globalMaxSum += maxRunSum
            curPtr -= 1
        return globalMaxSum




        
