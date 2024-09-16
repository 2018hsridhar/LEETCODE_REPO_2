Intuition and Approach :
Category :
Two Pointers, Linear Scan, Sorting

Sort the input
Identify the median element and count number of operations to get there
Search right and search left : for any element not satisfying inequality conditions for the median, update the el value accordingly
Complexity
Target complexity analysis:
Let N:= size of the input list

Time complexity:
O(NlgN)

Space complexity:
O(1) ( Explicit )
O(1) ( Implicit )

Code
'''
3107. Minimum Operations to Make Median of Array Equal to K
URL := https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/description/

'''
import math 

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        minOps = 0
        n = len(nums)
        nums.sort()
        medianIdx = -1
        medianIdx = math.floor(n / 2)
        if(n % 2 == 1):
            medianIdx = math.floor((n - 1)/2)
        minOps += abs(nums[medianIdx] - k)
        rightPtr = medianIdx + 1
        leftPtr = medianIdx - 1
        for rightPtr in range(medianIdx + 1, n,1):
            rightEl = nums[rightPtr]
            if(rightEl >= k):
                break
            minOps += abs(k - rightEl)
        for leftPtr in range(medianIdx - 1, -1,-1):
            leftEl = nums[leftPtr]
            if(leftEl <= k):
                break
            minOps += abs(k - leftEl)
        return minOps
