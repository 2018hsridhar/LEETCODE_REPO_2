'''
3301. Maximize the Total Height of Unique Towers
URL := https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

Approach : Greedy, Linear Scan

Complexity Analysis :
N = len(input)
Time = O(NlgN)
Space = O(1) ( Explicit ) O(1) ( Implicit ) 
'''
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        mts = 0
        n = len(maximumHeight)
        maximumHeight.sort(reverse=True)
        # handling of duplicates
        # be greedy -> try to equal the tower ( or less ) 
        # go for the first available value not yet used
        # Some value <= curTowerHeight
        maxTowerHit = maximumHeight[0]
        for tower in maximumHeight:
            if(tower == maxTowerHit):
                maxTowerHit -= 1
                mts += tower
            elif(tower < maxTowerHit):
                mts += tower
                maxTowerHit = tower - 1
            elif(tower > maxTowerHit):
                if(maxTowerHit == 0):
                    return -1
                mts += maxTowerHit
                # do not set tower height -> can still use it
                # case : [8,8,8,1] => 8,7,6,1
                maxTowerHit -= 1
        return mts
