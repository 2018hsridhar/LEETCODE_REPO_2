Python3 Solution Leveraging Binary Search and Prefix Sums for Minimzing Delta to TargetVal

Hari Sridhar
100 Days Badge 2022
29
0
a few seconds ago
Python3
Array
Binary Search
Sorting
1+
Intuition and Approach
Categories : Binary Search, Sorting, Arrays

Complexity
Time complexity:
N := len(input)
O(N)+O(lgN)

Space complexity:
O(N) ( E )
O(1) ( I )

Code
'''
URL := https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/description/
1300. Sum of Mutated Array Closest to Target


'''
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        fullSum = sum(arr)
        low = 0
        high = arr[-1]
        prefixSum = [0 for idx in range(len(arr))]
        runSum = 0
        n = len(arr)
        for idx,val in enumerate(arr):
            runSum += val
            prefixSum[idx] = runSum
        diffToVal = float('inf')
        value = float('inf')
        while(low <= high):
            targetVal = (int)(0.5 * (low + high))
            targetIdx = self.getConversionIndex(arr,targetVal)
            # handle edge case here
            if(targetIdx != -1):
                curSum = 0
                deltaToEnd = (n - targetIdx)
                if(targetIdx == 0):
                    curSum = deltaToEnd * targetVal
                else:
                    curSum = (deltaToEnd * targetVal) + prefixSum[targetIdx - 1]
                curAbsDist = abs(curSum - target)
                if(curAbsDist <= diffToVal):
                    if(curAbsDist < diffToVal):
                        value = targetVal
                    elif(curAbsDist == diffToVal):
                        value = min(value,targetVal)
                    diffToVal = curAbsDist
                if(curSum >= target):
                    high = targetVal - 1
                elif(curSum < target):
                    low = targetVal + 1
        return value

    # Get index of conversion
    def getConversionIndex(self, arr:List[int], target:int) -> int:
        low = 0
        high = len(arr) - 1
        targetIdx = float('inf')
        while(low <= high):
            mid = (int)(0.5 * (low + high))
            curVal = arr[mid]
            if(curVal >= target):
                targetIdx = min(targetIdx,mid)
                high = mid - 1
            else:
                low = mid + 1
        if(targetIdx == float('inf')):
            targetIdx = -1
        return targetIdx
