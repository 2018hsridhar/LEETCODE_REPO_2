Complexity
Let N:=length(input list)

Time complexity:
O(NlgN)

Space complexity:
O(N) ( Explicit)
O(1) ( Implicit )

Code
'''
2599. Make the Prefix Sum Non-negative
URL := https://leetcode.com/problems/make-the-prefix-sum-non-negative/description/
'''
import heapq

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        minOps = 0
        mostNegRecord = []
        runSum = 0
        for idx,val in enumerate(nums):
            record = [val,idx]
            if(val < 0):
                heapq.heappush(mostNegRecord, record)
            runSum += val
            while(runSum < 0 and len(mostNegRecord) > 0):
                worstMinRecord = heapq.heappop(mostNegRecord)
                worstMinEl = worstMinRecord[0]
                runSum += (abs)(worstMinEl)
                # always push back to the end anyways
                minOps += 1
                if(runSum >= 0):
                    break
        return minOps
         
