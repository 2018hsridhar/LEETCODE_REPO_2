'''
3457. Eat Pizzas!
URL := https://leetcode.com/problems/eat-pizzas/description/

Compelxity
T = O(NlgN)
S = O(1) ( E and I ) 

Greedy, Sort, Single Pass Linear Scan

[1,2,3,4,5,6,7,8] => 8 + 6
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] => 
    16 + 14 + 13 + 11
    16 + 15 + 13 + 11 ( seems the max ) = 10*4 = 40 = 55
    Some split by two things going on 

[1,2,3,4,5,6,7,8,9,10,11,12] => 
12 + 11 + 9 = ANS ( 32 ) 
'''

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        maxTotalWeight = 0
        n = len(pizzas)
        numDays = (int)(n / 4)
        pizzas.sort()
        numEvens = (int)(ceil(numDays/2))
        numOdds = (int)(numDays - numEvens)
        for x in range(numEvens):
            maxTotalWeight += pizzas[-1]
            del pizzas[-1]
        for x in range(numOdds):
            del pizzas[-1]
            maxTotalWeight += pizzas[-1]
            del pizzas[-1]
        return maxTotalWeight
