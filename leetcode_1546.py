'''
1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
URL := https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/description/
Categories : prefix sum, hashmap, DP, running sum
Think right->left type of thing

Compelxity
T = O(N)
S = O(N) ( Explicit ) O(1) ( Implicit ) 
'''
# sumFreq needs to be a latest index type of thing
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        sumFreq = dict()
        sumFreq[0] = 0
        prefixSum = 0
        numNotOverlapAtPos = [0 for idx in range(len(nums))]
        for idx,num in enumerate(nums):
            curSubProblem = 0
            if(idx >= 1):
                curSubProblem = numNotOverlapAtPos[idx-1]
            prefixSum += num
            delta = prefixSum - target
            if(delta in sumFreq):
                leftIndex = sumFreq[delta]
                adjustedLeft = leftIndex
                if(leftIndex >= 1):
                    adjustedLeft = leftIndex - 1
                # with adjust left, get count of numNonOverlap
                numToLeft = numNotOverlapAtPos[leftIndex]
                # hacky but passes -> investigate later!
                if(prefixSum != 0 and delta == 0 and leftIndex == 0):
                    numToLeft = 0
                considerCase = 1 + numToLeft
                curSubProblem = max(curSubProblem, considerCase)
            numNotOverlapAtPos[idx] = curSubProblem
            sumFreq[prefixSum] = idx
        numNotOverlap = max(numNotOverlapAtPos)
        return numNotOverlap
