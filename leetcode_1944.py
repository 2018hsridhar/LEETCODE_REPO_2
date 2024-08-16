# URL := https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/
# 1944. Number of Visible People in a Queue

# import collections for deque operations
# slightly harder : 0 can see 1,2,4 ( not 3 though )
from collections import deque

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        monotonicStack = deque([])
        n = len(heights)
        answer = [-1 for idx in range(n)]
        for idx in range(n-1,-1,-1):
            curEl = heights[idx]
            numRightVisible = 0
            # no one to the right case : 0 as default value
            while(len(monotonicStack) > 0):
                mostRecentPair = monotonicStack.pop()
                numRightVisible += 1
                if(curEl <= mostRecentPair[1]):
                    monotonicStack.append(mostRecentPair)
                    break
            monotonicStack.append([idx,curEl])
            answer[idx] = numRightVisible 
        return answer
