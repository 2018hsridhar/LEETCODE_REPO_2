'''
URL := https://leetcode.com/problems/minimum-sensors-to-cover-grid/description/
3648. Minimum Sensors to Cover Grid

Complexity
T = S = O(1) ( E ) ( I ) 
'''
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        windowSize = (k*2) + 1
        numRowOps = (int)(m/windowSize) 
        if((int)(m % windowSize) != 0):
            numRowOps += 1
        numColOps = (int)(n/windowSize)
        if((int)(n % windowSize) != 0):
            numColOps += 1
        bestAnswer = (int)(numRowOps * numColOps)
        return bestAnswer
