'''
URL := https://leetcode.com/problems/water-bottles-ii/description/
3100. Water Bottles II

Category : Iterative, Loops, Simulation, Counting, Tabulation

Complexity
Let B := number of full bottles
Let E := number of empty bottles
T := todo
S := todo

15 mins to solutioning
'''
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        maxBottlesConsumed = 0
        numEmptyBottles = 0
        while(True):
            # greedily consume the most bottles in any given step
            # get the most empty bottles
            maxBottlesConsumed += numBottles
            numEmptyBottles += numBottles
            numBottles = 0
            # facilicate the exchange ( break if not possible )
            if(numEmptyBottles >= numExchange):
                numEmptyBottles -= numExchange
                numBottles += 1
                numExchange += 1
            else:
                break
        return maxBottlesConsumed
        
