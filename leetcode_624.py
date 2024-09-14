Target Complexity Analysis
Let M:=#-arrays

Time complexity:
Time:=O(MlgM)

Space complexity:
Space:=O(M) ( EXP )
O(1) ( IMP )

Code
'''
URL := https://leetcode.com/problems/maximum-distance-in-arrays/description/
624. Maximum Distance in Arrays
'''
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        minOverArrs = [[] for idx in range(m)]
        maxOverArrs = [[] for idx in range(m)]
        # record : [index,val] structure under insertion
        for index,array in enumerate(arrays):
            curMin = array[0]
            curMax = array[-1]
            minOverArrs[index] = [index,curMin]
            maxOverArrs[index] = [index,curMax]
        minOverArrs.sort(key = lambda x : (x[1],x[0]))
        maxOverArrs.sort(key = lambda x : (x[1],x[0]))
        minIdx = minOverArrs[0][0]
        maxIdx = maxOverArrs[-1][0]
        minVal = minOverArrs[0][1]
        maxVal = maxOverArrs[-1][1]
        if(minIdx != maxIdx):
            maxDist = abs(maxVal-minVal)
        else:
            caseTwoMinVal = minOverArrs[1][1]
            caseThreeMaxVal = maxOverArrs[-2][1]
            caseTwoDist = abs(caseTwoMinVal - maxVal)
            caseThreeDist = abs(caseThreeMaxVal - minVal)
            maxDist = max(caseTwoDist,caseThreeDist)
        return maxDist

        
