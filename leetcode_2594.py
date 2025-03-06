'''
2594. Minimum Time to Repair Cars
URL := https://leetcode.com/problems/minimum-time-to-repair-cars/description/

Complexity
K = range to bsearch on : pow(10,15) in this case
N = len(ranks)
T = O(NlgK)
S = O(1) ( E ) O(1) ( I ) 

Intuition and Approach : Leverage Binary Search. 
Only pow(10,6) cars at max. Can define an arbitrarily large floating number to finish quickly
Ranks of value 100 at worst. Imagine each rank is 1 at best.
'''
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        minTimeToRepair = float('inf')
        ranks.sort()
        low = 1
        high = pow(10,15)
        while(low <= high):
            mid = (int)((0.5)*(low + high))
            numCarsRepaired = 0
            for rank in ranks:
                carsPerRank = floor(sqrt((float)(mid)/(float)(rank)))
                numCarsRepaired += carsPerRank
            if(numCarsRepaired >= cars):
                minTimeToRepair = min(minTimeToRepair,mid)
                high = mid - 1
            else:
                low = mid + 1
        return minTimeToRepair

        
        
