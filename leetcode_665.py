'''
Count of wildcards idea ( seen graphically ) ?
665. Non-decreasing Array
URL := https://leetcode.com/problems/non-decreasing-array/description/
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # can modify the any other one element, but not the other -> there's rigidit
        # e.g. [1,4,2,5] -> [1,4,4,5] or 
        # [1,4,2,3] -> [1,2,2,3]
        # this is the situation @ hand : for every decrease, append it as a "wildcard"
        status = True
        wildHit = 0
        n = len(nums)
        for ptr in range(len(nums) - 1):
            firstVal = nums[ptr]
            secondVal = nums[ptr+1]
            if(secondVal < firstVal):
                changeCondLeft = False
                changeCondRight = False
                if(ptr > 0 and ptr + 2 < n):
                    prevVal = nums[ptr-1]
                    nextVal = nums[ptr+2]
                    if(prevVal <= firstVal and firstVal <= nextVal):
                        changeCondLeft = True
                    if(prevVal <= secondVal and secondVal <= nextVal):
                        changeCondRight = True
                    if(changeCondLeft or changeCondRight):
                        wildHit += 1
                    else:
                        return False
                else:
                    wildHit += 1
        if(wildHit > 1):
            status = False
        return status
