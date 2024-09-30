Python3 Greedy Solution O(nlgn) time O(1) Space Iterative-only leveraging sorts and induction

2018hsridhar
100 Days Badge 2022
28
0
a few seconds ago
C++
Python3
Array
Greedy
1+
Intuition and Approach
Induct and exhaust principle

First work of the negative numbers -> conv to positive
Sort numbers again ( if no more negative numbers )
See problem title
Complexity
Let N:= length of the input

Time complexity:
O(NlgN)

Space complexity:
O(1) ( Explicit and Implicit )

Code
'''
URL := https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
1005. Maximize Sum Of Array After K Negations
'''
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        lPtr = 0
        curSum = sum(nums)
        for lPtr in range(len(nums)):
            curVal = nums[lPtr]
            if(curVal < 0 and k > 0):
                nums[lPtr] = abs(nums[lPtr])
                k-= 1
                curSum = curSum + abs(curVal) + abs(curVal)
            else:
                break

        # sort again : from 0 to largest positive value ( and re-evaluate the sum ) 
        nums.sort()
        curSum = sum(nums)
        if(k % 2 == 1):
            # must negate the most minimal non-neg element
            # but leverage the shit out of the zero case
            firstEl = nums[0]
            curSum = curSum - firstEl - firstEl
        return curSum
        
