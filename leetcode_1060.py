Python3 O(N) Time O(1) Space Iterative-only algorithm compare two consecutive els and range size che

2018hsridhar
100 Days Badge 2022
28
0
a few seconds ago
C++
Python3
Array
Intuition and Approach
First missing number ( but from the minimal element -> not from 0 ) !
See problem description

Complexity
Let N:=len(nums)

Time complexity:
O(N)(naive)O(log(N))(efficient)

Space complexity:
O(1)(EXP)O(1)(IMP)

Code
'''
URL := https://leetcode.com/problems/missing-element-in-sorted-array/description/
1060. Missing Element in Sorted Array
'''

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        prevEl = nums[0]
        for ptr in range(1,len(nums),1):
            curEl = nums[ptr]
            gap = abs(curEl - prevEl)
            window = gap - 1
            nextK = k - window
            if(nextK <= 0):
                break
            else:
                k = nextK
            prevEl = curEl
        firstMissingEl = prevEl + k        
        return firstMissingEl
