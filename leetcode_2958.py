'''
URL := https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/
2958. Length of Longest Subarray With at Most K Frequency

Categories : Linear Scan, One Pass, Counting, Maps, Enumeration, Constraints Satisfiability 

Complexity
Let N := len(nums)
Time := O(N)
Space := O(N) ( E ) O(1) ( I ) 
'''
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        msl = 0
        valFreq = dict()
        leftPtr = 0
        curWindow = 0
        for rightPtr,val in enumerate(nums):
            if val not in valFreq:
                # gaaah KeyError statement
                valFreq[val] = 0
            # hey can't add if already equal to k -> need to remove now
            # while loop versus if when a condition is met -> using 
            # iterative code for cond logic :-O 
            # guard safety : more guarntees made?
            while(valFreq[val] >= k and leftPtr <= rightPtr):
                leftVal = nums[leftPtr]
                valFreq[leftVal] -= 1
                leftPtr += 1
            # needs an offset back :-)
            valFreq[val] += 1
            curWindow = rightPtr - leftPtr + 1
            msl = max(msl,curWindow)
        return msl
