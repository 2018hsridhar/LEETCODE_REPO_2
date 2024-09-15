Intuition and Approach
Greedy based problem where we sort by a combination of [element,index] for each pair in the input array, and then read the sorted records right to left. Reading this way, we can find the leftmost element which satisfies our condition.

Complexity
Let N:= length of the input list

Time complexity:
O(NlgN)

Space complexity:
O(1) ( Explcit )
O(1) ( Implicit )

Code
'''
URL := https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/description/
2863. Maximum Length of Semi-Decreasing Subarrays
'''
import math

class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        records = []
        for idx,val in enumerate(nums):
            record = [val,idx]
            records.append(record)
        records.sort(key = lambda x : (x[0],x[1]))
        n = len(records)
        maxLength = 0
        readPtr = n - 1
        bestMinIndex = float('inf')
        while(readPtr >= 0):
            el = records[readPtr]
            rightIdx = el[1]
            if(bestMinIndex != float('inf')):
                leftIdx = bestMinIndex
                if(leftIdx < rightIdx):
                    curLength = (rightIdx - leftIdx) + 1
                    maxLength = max(maxLength, curLength)
            bestMinIndex = min(bestMinIndex, rightIdx)
            readPtr -= 1
        return maxLength
