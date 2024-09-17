Intuition and Approach
Category : Binary Search, Greedy, Linear Scan
This is a problem where we want to minimize repeated computation : no hero can take on a monster of magnitute greater than themselves, so if we first sort the monsters by their size ( and then by number of coins ) and then we compute a prefix sum of the number of coins across monsters growing by height, we can return the maximal number of coins a hero can obtain

Complexity
Let N:= length of the input list

Time complexity:
O(NlgN)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
'''
URL := https://leetcode.com/problems/maximum-coins-heroes-can-collect/description/
2838. Maximum Coins Heroes Can Collect
'''

import math 

class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        n = len(heroes)
        m = len(monsters)
        maxCoins = [0 for idx in range(len(heroes))]
        records = [[monster,coin,coin] for monster,coin in zip(monsters,coins)]
        records.sort(key = lambda x : (x[0],x[1]))
        for idx in range(1,len(records),1):
            records[idx][2] += records[idx-1][2]
        for idx, hero in enumerate(heroes):
            maxNumCoins = self.bSearchBestMax(records,hero)
            maxCoins[idx] = maxNumCoins
        return maxCoins

    # returns value, not index of the value
    def bSearchBestMax(self, records: List[List[int]], hero:int) -> int:
        bestMax = 0
        low = 0
        high = len(records) -1
        while(low <= high):
            mid = math.floor((low + high) / 2)
            curRecord = records[mid]
            curMonster = curRecord[0]
            curMax = curRecord[2]
            if(curMonster <= hero):
                bestMax = max(bestMax, curMax)
                low = mid + 1
            # can't defeat go lower
            elif(curMonster > hero):
                high = mid - 1
        return bestMax
