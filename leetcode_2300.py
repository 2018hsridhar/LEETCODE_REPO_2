'''
URL := https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
2300. Successful Pairs of Spells and Potions

Category : Sorting, Binary Search, Array
Complexity
Let S := #=spells, P := #-potions
Time = O(SlgS) + O(PlgP)
Space = O(1) ( E & I ) 

'''
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        numPairs = [-1 for i in range(len(spells))]
        potions.sort()
        for index, spell in enumerate(spells):
            minPotionValue = int(ceil(success / spell))
            numPairs[index] = len(potions) - self.bSearch(minPotionValue, potions)
        return numPairs

    # Liking pythonic List[numeric] type representation
    # 0 out to potions length : if no delta possible
    # forget self : complaint on position args number
    def bSearch(self, minPotionVal: int, potions: List[int]) -> int:
        leftMostIdx = len(potions)
        low = 0
        high = len(potions) - 1
        while(low <= high):
            mid = int(low + (high - low) / 2)
            val = potions[mid]
            # val is exact enough, but can we perform more left again?
            # "==" sign not useful
            if(val == minPotionVal):
                leftMostIdx = min(leftMostIdx, mid)
                high = mid - 1
            # val is big enough, but we may be able to perform better
            elif(val > minPotionVal):
                leftMostIdx = min(leftMostIdx, mid)
                high = mid - 1
            # val not big enough : please go higher up
            elif(val < minPotionVal):
                low = mid + 1
        return leftMostIdx
