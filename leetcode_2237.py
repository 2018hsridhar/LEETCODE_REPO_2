'''
2237. Count Positions on Street With Required Brightness
URL := https://leetcode.com/problems/count-positions-on-street-with-required-brightness/description/

Categories : Prefix Sums, Linear Scan, Multiple Passes, Counting, Enumeration
Inclusive lighting on the number line

Complexity
T = O(N)
S = O(N) ( E ) O(1) ( I ) 

'''
class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        numValidPositions = 0
        prefixSums = [0 for idx in range(n)]
        for [lightPos,lightRange] in lights:
            lightLeft = max(0,lightPos - lightRange)
            lightRight = min(n-1,lightPos + lightRange)
            prefixSums[lightRight] += 1
            if(lightLeft - 1 >= 0):
                prefixSums[lightLeft-1] -= 1
        numberValidPositions = 0
        curSum = 0
        for index in range(len(requirement) - 1, -1,-1):
            curSum += prefixSums[index]
            curReq = requirement[index]
            if(curSum >= curReq):
                numValidPositions += 1
        return numValidPositions



        
