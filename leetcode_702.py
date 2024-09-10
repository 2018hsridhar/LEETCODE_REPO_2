Intuition and Approach
Modified binary search : we don't know the size of the array
We still need to be logarithmic, but we do know a bound to the secret length ( of pow(10,4) max)

Complexity
Let N:= #-elements in the secret

Time complexity:
O(log(N))

Space complexity:
O(1) ( Explicit and Implicit )

Code
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:
'''
URL := https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description/
702. Search in a Sorted Array of Unknown Size
'''
import math

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        lower = 0
        upper = math.pow(10,4)
        searchResult = -1
        outOfBoundsVal = math.pow(2,31) - 1
        while(lower <= upper):
            mid = lower + math.floor(abs(upper - lower) / 2)
            candidate = reader.get(mid)
            if(candidate == outOfBoundsVal or candidate > target):
                upper = mid - 1
            elif(candidate < target):
                lower = mid + 1
            else:
                searchResult = mid
                break
        return searchResult
