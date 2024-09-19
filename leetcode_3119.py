Intuion and Approach :
Think of a greedy approach. We want to maximize the number of potholes we want to fill,
and we want to minimize exploring our combinatorial solution space by focusing on a single
combination for the solution. There are two seperate cases of potholes
(A) Consecutive pothole lengths >= budget
(B) Pothole lengths < budget
where in (A) stops us from future processing but (B) informs us to carry on input processing

Complexity
Let N:= len(input)

Time complexity:
O(NlgN)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
'''
URL := https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/description/
3119. Maximum Number of Potholes That Can Be Fixed
'''
class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        ptr = 0
        n = len(road)
        runLen = 0
        # part (1) populate and then sort our records
        records = []
        while(ptr < n):
            if(road[ptr] == 'x'):
                runLen += 1
            elif(road[ptr] == '.'):
                if(runLen > 0):
                    records.append(runLen)
                runLen = 0
            ptr += 1
        if(runLen > 0):
            records.append(runLen)
        records.sort(key = lambda x : -1 * x)
        # part (2) Run through records get optimal number holes
        recordPtr = 0
        numRecords = len(records)
        numHoles = 0
        while(budget > 0 and recordPtr < numRecords):
            curRecord = records[recordPtr]
            curCost = curRecord + 1
            if(curCost >= budget):
                numHoles += (budget - 1)     
                budget = 0    
                break
            else:
                numHoles += curRecord
                budget -= curCost
            recordPtr += 1
        return numHoles
        
