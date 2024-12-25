# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
'''
URL := https://leetcode.com/problems/sum-of-consecutive-subarrays/description/
3284. Sum of Consecutive Subarrays

Decompose the probem into different cases
(A) Increasing, len >= 2
(B) Decreasing, len >= 2
(C) All elements
Capture sums, based on frequency
Get each interval : know ( start, end) of each interval 
30 mins to solutioning :-) 
Complexity
N = #-records
T = O(N)
S = O(N) ( E ) O(1) ( I )
'''
class Solution:
    def getSum(self, nums: List[int]) -> int:
        finalSum = 0
        ascIntervals = []
        # for ASC intervals
        n = len(nums)
        lPtr = 0
        rPtr = 0
        while(rPtr < n - 1):
            curEl = nums[rPtr]
            nextEl = nums[rPtr + 1]
            if(curEl == nextEl - 1):
                rPtr += 1
            else:
                window = (rPtr - lPtr + 1)
                if(window >= 2):
                    interval = [lPtr,rPtr]
                    ascIntervals.append(interval)
                rPtr += 1
                lPtr = rPtr
        finalWindow = (len(nums) - lPtr)
        if(finalWindow >= 2):
            finalInterval = [lPtr,rPtr]
            ascIntervals.append(finalInterval)
        # DESC intervals
        descIntervals = []
        lPtr = 0
        rPtr = 0
        while(rPtr < n - 1):
            curEl = nums[rPtr]
            nextEl = nums[rPtr + 1]
            if(curEl == nextEl + 1):
                rPtr += 1
            else:
                # broken, but figure out why ... do not 2x count it
                # [100,99] and [99,100] -> do not once count too ?? 
                window = (rPtr - lPtr + 1)
                if(window >= 2):
                    interval = [lPtr,rPtr]
                    descIntervals.append(interval)
                rPtr += 1
                lPtr = rPtr
        finalWindow = (len(nums) - lPtr)
        if(finalWindow >= 2):
            finalInterval = [lPtr,rPtr]
            descIntervals.append(finalInterval)
        modulo = pow(10,9) + 7
        # for el in nums:
            # finalSum += el
        visited = set()
        # handle overlap case : change from ASC to DESC ( you're almost there TBH ) 
        for [start,end] in ascIntervals:
            for idx in range(start,end+1,1):
                visited.add(idx)
                lenToEnd = (end - idx) + 1
                lenFromBegin = (idx - start + 1)
                finalSum += lenToEnd * lenFromBegin * nums[idx]
        for [start,end] in descIntervals:
            for idx in range(start,end+1,1):
                if(idx in visited):
                    finalSum -= nums[idx]
                visited.add(idx)
                lenToEnd = (end - idx) + 1
                lenFromBegin = (idx - start + 1)
                finalSum += lenToEnd * lenFromBegin * nums[idx]
        for idx in range(len(nums)):
            if(idx not in visited):
                finalSum += nums[idx]
        finalSum %= modulo
        return finalSum

```
