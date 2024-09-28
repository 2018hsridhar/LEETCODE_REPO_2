Intuition and Approach
See title

Complexity
Let N:= length of the input

Time complexity:
O(N)

Space complexity:
O(1) ( Explicit and Implicit )

Code
'''
795. Number of Subarrays with Bounded Maximum
URL := https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/

Complexity
Let N := len(input)

Time = O(N)
Space = O(1) ( E ) O(1) ( I ) 
'''
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        curPtr = n - 1
        rightRangePtr = -1
        leftRangePtr = -1
        numSubArr = 0
        hitElInRange = False
        while(curPtr >= 0):
            curEl = nums[curPtr]
            if(left <= curEl and curEl <= right):
                if(rightRangePtr == -1):
                    rightRangePtr = curPtr
                if(leftRangePtr == -1):
                    leftRangePtr = curPtr
                hitElInRange = True
                leftRangePtr = curPtr
                numRanges = (rightRangePtr - leftRangePtr) + 1
                numSubArr += numRanges
            elif(curEl < left):
                if(rightRangePtr == -1):
                    rightRangePtr = curPtr
                if(leftRangePtr == -1):
                    leftRangePtr = curPtr
                if(hitElInRange):
                    numRanges = (rightRangePtr - leftRangePtr) + 1
                    numSubArr += numRanges
            elif(curEl > right):
                hitElInRange = False
                rightRangePtr = -1
                leftRangePtr = -1
            curPtr -= 1
        return numSubArr        
