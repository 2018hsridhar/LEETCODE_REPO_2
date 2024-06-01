'''
2597. The Number of Beautiful Subsets
URL := https://leetcode.com/problems/the-number-of-beautiful-subsets/description/

Commit log : 
(A) Power to the default initialization of values in listComp
(B)

Cases :
a. [2,4,6,10,12,15,17,21], k = 2

25 minutes
surprisingly close

There's a sorting DP idea for sure here :-)
Not accounting for future deltas properly here :-(
    {4,5,7,10} 

'''
class Solution:    
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        numSubsets = [1 for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            curNumSubsets = 1
            # print("Working with val = " + str(nums[i]))
            for j in range(i+1,len(nums),1):
                curDelta = abs(nums[j] - nums[i])
                if(curDelta != k):
                    curNumSubsets += numSubsets[j]
            numSubsets[i] = curNumSubsets
        numBeat = sum(numSubsets)
        print(numSubsets)
        return numBeat
