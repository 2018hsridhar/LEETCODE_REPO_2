'''
URL := https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
1838. Frequency of the Most Frequent Element

Complexity :
Let N := len(nums)
T = O(N)
S = O(1) ( E & I ) 

Harder than it seems due to sliding window

Category : Greedy, Sliding Window, Sorting, Prefix Summation, Array

'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        maxFreq = 1
        nums.sort()
        n = len(nums)
        rPtr = n-1
        lPtr = rPtr
        curDelta = 0
        curWindSize = 0
        # always start Lptr @ rPtr : aaccounts for cur el itself ( identity case )
        while(rPtr >= 0 and lPtr >= 0):
            curDelta += nums[rPtr] - nums[lPtr]
            curWindSize += 1
            lPtr -= 1
            if(curDelta <= k):
                maxFreq = max(maxFreq, curWindSize)
            elif(curDelta > k):
                rightEl = nums[rPtr]
                nextWindSize = (curWindSize - 1)
                curDelta -= (rightEl * nextWindSize)
                if(rPtr - 1 >= 0):
                    secondRight = nums[rPtr - 1]
                    curDelta += (secondRight * nextWindSize)
                rPtr -= 1
                # NOP instruction above where you'll add back again and incr wind size again
                curDelta -= nums[rPtr] - nums[lPtr]
                curWindSize = nextWindSize
                curWindSize -= 1
        return maxFreq
        
