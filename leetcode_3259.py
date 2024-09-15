Intuition and Approach
Always positive integral energy

Complexity
Let N:= #-hours we consume energy drinks for

Time complexity:
O(N)

Space complexity:
O(N) ( E ) O(1) ( I )

Code
'''
3259. Maximum Energy Boost From Two Drinks
URL := https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/description/

'''
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        maxCons = [energyDrinkA,energyDrinkB]
        # n-1 and n-2 cases
        n = len(energyDrinkA)
        secondToLast = len(energyDrinkA)-2
        drinkA = 0
        drinkB = 1
        maxCons[drinkA][secondToLast] += maxCons[drinkA][-1]
        maxCons[drinkB][secondToLast] += maxCons[drinkB][-1]
        for ptr in range(n-3,-1,-1):
            aVal = energyDrinkA[ptr]
            bVal = energyDrinkB[ptr]
            maxCons[drinkA][ptr] = max(aVal + maxCons[drinkA][ptr+1], aVal + maxCons[drinkB][ptr+2])
            maxCons[drinkB][ptr] = max(bVal + maxCons[drinkB][ptr+1], bVal + maxCons[drinkA][ptr+2])
        energy = max(maxCons[drinkA][0], maxCons[drinkB][0])
        return energy
