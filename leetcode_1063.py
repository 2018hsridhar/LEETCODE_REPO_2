# Uusally sliding window ( maybe a heap for dynamic sorting )
# Heaps + sliding window to analyze : streaming and sorting
# URL := https://leetcode.com/problems/number-of-valid-subarrays/description/
# 1063. Number of Valid Subarrays
# preferd for O(1) append and remove ( List is O(N) )
# 15 minutes passed first time
from collections import deque

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        numValidSubArrays = 0
        n = len(nums)
        monotonicStack = deque()
        rightPtr = 0
        while(rightPtr < n):
            el = nums[rightPtr]
            idx = rightPtr
            if(len(monotonicStack) > 0):
                while(len(monotonicStack) > 0):
                    lastPair = monotonicStack.pop()
                    mostRecentVal = lastPair[0]
                    if(mostRecentVal <= el):
                        monotonicStack.append(lastPair)
                        break
                    else:
                        mostRecentIdx = lastPair[1]
                        numSubArrs = abs(idx - mostRecentIdx)
                        numValidSubArrays += numSubArrs
            # an operation which always happens :-)
            monotonicStack.append([el,idx])
            rightPtr += 1
        while(len(monotonicStack) > 0):
            curPair = monotonicStack.pop()
            numSubArrs = abs(n - curPair[1])
            numValidSubArrays += numSubArrs
        return numValidSubArrays
        
