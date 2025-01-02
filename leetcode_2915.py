'''
2915. Length of the Longest Subsequence That Sums to Target
URL := https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/description/

Complexity
N = len(nums)
T = Target
T = O(NT)
S = O(NT) ( Exp ) O(N) ( Imp ) 
'''
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # target + 1 ( for indexing reasons ) across rows
        memo = [[-2 for col in range(len(nums))] for row in range(target + 1)]
        startIndex = 0
        bestSeqLen = self.solve(nums,memo,target, startIndex)
        return bestSeqLen

    # (A) Select the num at index or (B) do not select num at index
    # oh we want length : careful here ( maximization to get the longest serquence ) 
    # all vals >= 1 vacuous solution to zero
    def solve(self, nums: List[int], memo : List[List[int]], target:int, parentIndex:int) -> int:
        # 0 always solveable ( invariant of problem ) 
        curLen = -1
        if(parentIndex >= len(nums)):
            if(target == 0):
                return 0
            return -1
        if(memo[target][parentIndex] != -2):
            return memo[target][parentIndex]
        if(target == 0):
            return 0
        elif(target > 0):
            curVal = nums[parentIndex]
            childTarget = target - curVal
            childIndex = parentIndex + 1
            childCaseTwo = self.solve(nums,memo,target,childIndex)
            if(childCaseTwo != -1):
                curLen = childCaseTwo
            if(childTarget >= 0):
                # bug here : if recursive returns -1
                childCaseOne = self.solve(nums,memo, childTarget, childIndex)
                if(childCaseOne != -1):
                    curLen = max(curLen, 1 + childCaseOne)
        memo[target][parentIndex] = curLen
        return memo[target][parentIndex]
        
