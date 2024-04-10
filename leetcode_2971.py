'''
URL := https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/
2971. Find Polygon With the Largest Perimeter

Greedy, Prefix Sum, 15 mins to solutioning
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        lp = -1
        nums.sort()
        runSum = 0
        # perimeter = runSum + a_k value
        # enumerate(list) as non-pythonic way
        # terminating early at [1,1,2]
        # for idx,val in enumerate(nums):
        # really reduced mem footprint for range(len(list)) styling
        for idx in range(len(nums)):
            val = nums[idx]
            if(idx >= 2):
                # dyn typed lang forces this concatenation styling only
                # print("Run sum = " + str(runSum) + " \t val = " + str(val))
                if(runSum > val):
                    # gaaah math package is lowercase
                    # gaaah forgot package prefix too
                    lp = max(lp,runSum + val)
            runSum += val
        return lp
        
