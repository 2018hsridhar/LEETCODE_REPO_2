'''
2948. Make Lexicographically Smallest Array by Swapping Elements
URL := https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

Complexity
Let N := len(input)
Time = O(NlgN)
Space = O(1) ( E ) O(1) ( I ) 

Store original indices and sets of numbers for each corresponding index

Scenario #1 :: limit = 2
[1,3,5] = [0,1,2]
[9,8] = [3,4]
best output = [1,3,5,8,9]

Scenario #2 :: limit = 3
[1,1,2] = [0,4,5]
[6,7] = [1,2]
[18] = 3
best output = [1,6,7,18,1,2]

Approaches -> Union Find, Sorting, Greedy, Processing of Indices
15 minutes to problem solutioning !!!
'''
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        lesa = [-1 for idx in range(len(nums))]
        targetIndices = []
        for idx, num in enumerate(nums):
            record = [num,idx]
            targetIndices.append(record)
        targetIndices.sort(key = lambda  x: (x[0],x[1]))
        uuid = 0
        curPtr = 0
        runVal = targetIndices[0][0]
        runValSet = []
        runIdxSet = []
        runValMap = dict()
        runIdxMap = dict()
        while(curPtr < n):
            curRecord = targetIndices[curPtr]
            [curVal,curIdx] = targetIndices[curPtr]
            if(curVal - runVal <= limit):
                runVal = curVal
                runValSet.append(curVal)
                runIdxSet.append(curIdx)
            else:
                runValMap[uuid] = runValSet
                runIdxMap[uuid] = runIdxSet
                runValSet = []
                runIdxSet = []
                runValSet.append(curVal)
                runIdxSet.append(curIdx)
                runVal = curVal
                uuid += 1
            curPtr += 1
        runValMap[uuid] = runValSet
        runIdxMap[uuid] = runIdxSet
        for k, runIdxs in runIdxMap.items():
            runIdxs.sort()
            runVals = runValMap[k]
            ptr = 0
            for idx in runIdxs:
                lesa[idx] = runVals[ptr]
                ptr += 1
        return lesa
