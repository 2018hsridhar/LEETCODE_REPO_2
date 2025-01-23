'''
689. Maximum Sum of 3 Non-Overlapping Subarrays
URL := https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

N = len(nums)
Complexity
T = O(N)
S = O(N) ( Explicit ) O(1) ( Implicit ) 

Categories : DP, Prefix Sums, Right-to-Left Scanning, Linear Scans
Three of length k 
Decomposition technique : sol(i,1), (i,2) and (i,3)

It's not sum - it's beset indices ( careful ! )
20 minutes and solutioned WOAH!!!
'''
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        bestIndices = []
        n = len(nums)
        numArrs = 3
        # 0 for all other values -> wait this stores indices
        # ok better idea -> store [value, {indices}] in each DP ?
        # special case : value = 1 -> no offset :-)
        initRecord = [0,[]]
        DP = [[initRecord for col in range(len(nums))] for row in range(numArrs)]
        for row in range(numArrs):
            runSum = 0
            curWindowSize = 0
            offset = k
            for col in range(len(nums) - 1, -1,-1):
                runSum += nums[col]
                curWindowSize += 1
                rightMostCol = col + offset
                if(curWindowSize == k):
                    curSumFromPosition = runSum 
                    curIndexSet = [col]
                    if(row > 0 and rightMostCol < n):
                        curSumFromPosition += DP[row - 1][rightMostCol][0]
                        DPIndexSet = DP[row - 1][rightMostCol][1]
                        curIndexSet += DPIndexSet
                    updatedRecord = [curSumFromPosition, curIndexSet]
                    # Is it the updated record OR the entry after me?
                    if(col + 1 < n):
                        if(updatedRecord[0] >= DP[row][col+1][0]):
                            DP[row][col] = updatedRecord
                        else:
                            DP[row][col] = DP[row][col+1]
                    # subtract right most val
                    if(rightMostCol-1 < n):
                        runSum -= nums[rightMostCol-1]
                    curWindowSize -= 1
        bestIndices = DP[2][0][1]
        return bestIndices



        
