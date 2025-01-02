'''
2831. Find the Longest Equal Subarray
URL := https://leetcode.com/problems/find-the-longest-equal-subarray/description/

Categories : Map, Frequency, Sliding Window, Counting
11 minutes to solutioning :-)

'''
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        # 1 is a default invariant answer
        les = 1
        numIndices = dict()
        for index,num in enumerate(nums):
            if(num not in numIndices):
                numIndices[num] = []
            numIndices[num].append(index)
        for keyNum in numIndices:
            numIndices[keyNum].sort()
        for key, indicesKey in numIndices.items():
            lPtr = 0
            rPtr = 0
            n = len(indicesKey)
            gaps = [abs(indicesKey[i+1] - indicesKey[i] - 1) for i in range(len(indicesKey) - 1)]
            runK = k
            for rPtr in range(len(gaps)):
                curVal = gaps[rPtr]
                runK -= curVal
                while(runK < 0 and lPtr <= rPtr):
                    leftEl = gaps[lPtr]
                    runK += leftEl
                    lPtr += 1
                if(runK >= 0):
                    slideWindow = (rPtr - lPtr) + 2
                    les = max(les, slideWindow)
                rPtr += 1
        return les
