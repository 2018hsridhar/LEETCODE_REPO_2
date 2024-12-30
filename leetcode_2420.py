'''
Can we leverage monotonic stacks? Seeps DP ( compute to Right, comptue to Left ) type of pattern yet again?
2420. Find All Good Indices
URL := https://leetcode.com/problems/find-all-good-indices/description/
It's counting/prefix Sum : it's the length of the sequences yet again

Complexity
T = O(N)
S = O(N) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        goodIndices = []
        # Pass 1 : go right and check
        leftPassLen = [1 for idx in range(len(nums))]
        runLen = 0
        prevEl = float('inf')
        for rightPtr, rightEl in enumerate(nums):
            if(rightEl <= prevEl):
                runLen += 1
            elif(rightEl > prevEl):
                runLen = 1
            prevEl = rightEl
            leftPassLen[rightPtr] = runLen
        # print(leftPassLen)
        # Pass 2 : go left and check
        rightPassLen = [1 for idx in range(len(nums))]
        runLen = 0
        prevEl = float('inf')
        n = len(nums)
        for leftPtr, leftEl in reversed(list(enumerate(nums))):
            if(leftEl <= prevEl):
                runLen += 1
            elif(leftEl > prevEl):
                runLen = 1
            prevEl = leftEl
            rightPassLen[leftPtr] = runLen
        for idx in range(1,len(nums)-1,1):
            leftFreq = leftPassLen[idx-1]
            rightFreq = rightPassLen[idx+1]
            if(leftFreq >= k and rightFreq >= k):
                goodIndices.append(idx)
        goodIndices.sort()
        return goodIndices

        
