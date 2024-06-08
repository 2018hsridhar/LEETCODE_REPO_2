'''
1696. Jump Game VI
URL := https://leetcode.com/problems/jump-game-vi/

DP solution is O(n*k) but it remains acceptable ( nope -> out of bounds)
We need some other structures to assist out now ( as well as to expedite solutioning ) 
since k can grow huge -> can we use something else instead and avoid checking all k?
- sliding window atop the DP approach

'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [(sys.maxsize * -1) for i in range(len(nums))]
        # remember : we have to ugh ... actually jump
        # we can't just choose ... not to jump ( 3,-6,-3) -> local best is a 0, not a 3
        # last index is default known -> all other indices to check now
        # base case handling
        dp[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums) - 2, -1,-1):
            localBestToEnd = dp[i]
            for j in range(i+1,min(len(nums), i+k+1), 1):
                candidateState = nums[i] + dp[j]
                if(candidateState > localBestToEnd):
                    localBestToEnd = candidateState
            dp[i] = localBestToEnd
        maxRes = dp[0]
        return maxRes
