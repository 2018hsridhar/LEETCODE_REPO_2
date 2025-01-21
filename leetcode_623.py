'''
632. Smallest Range Covering Elements from K Lists
URL := https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/

Complexity
N = #-records total
T = O(N)
S = O(1) ( E ) O(1) ( I )
'''
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 1. Initialize our records
        k = len(nums)
        records = []
        for recordIndex,inputList in enumerate(nums):
            for num in inputList:
                record = [num,recordIndex]
                records.append(record)
        records.sort(key = lambda x : (x[0],x[1]))
        print(records)
        # 2. The meat of the algo
        maxWindowLen = float('inf')
        smallestRange = []
        n = len(records)
        recordFreq = dict()
        leftPtr = 0
        rightPtr = 0
        while(rightPtr < n):
            record = records[rightPtr]
            rightEl = record[0]
            rightIndex = record[1]
            if(rightIndex not in recordFreq):
                recordFreq[rightIndex] = 0
            recordFreq[rightIndex] += 1
            while(len(recordFreq) == k and leftPtr <= rightPtr):
                leftRecord = records[leftPtr]
                leftEl = leftRecord[0]
                curWindowLen = (rightEl - leftEl) + 1
                if(curWindowLen < maxWindowLen):
                    maxWindowLen = curWindowLen
                    smallestRange = [leftEl,rightEl]
                leftIndex = leftRecord[1]
                nextFreq = recordFreq[leftIndex] - 1
                recordFreq[leftIndex] = nextFreq
                if(nextFreq == 0):
                    del recordFreq[leftIndex]
                leftPtr += 1
            rightPtr += 1
        return smallestRange
