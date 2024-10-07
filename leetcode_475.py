Intuition and Approach
See title

Complexity
Let
H:= number homes
N:= number heaters

Time complexity:
O(HlgN)

Space complexity:
O(1) ( Explicit and Implicit )

Code
'''
475. Heaters
URL := https://leetcode.com/problems/heaters/description/

Fixed warm radius heaters -> solution for the minimum radius standard with 100% home coverage.
'''
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        bestRadius = float('-inf')
        # maximal radius ( across each home )
        for house in houses:
            leftIdx = self.getLeftIndex(house,heaters)
            rightIdx = self.getRightIndex(house,heaters)
            if(leftIdx == -1 and rightIdx != -1):
                heatRight = heaters[rightIdx]
                rightDist = abs(heatRight - house)
                bestRadius = max(bestRadius, rightDist)
            elif(leftIdx != -1 and rightIdx == -1):
                heatLeft = heaters[leftIdx]
                leftDist = abs(house - heatLeft)
                bestRadius = max(bestRadius, leftDist)
            else:
                heatLeft = heaters[leftIdx]
                heatRight = heaters[rightIdx]
                leftDist = abs(house - heatLeft)
                rightDist = abs(heatRight - house)
                bestRadius = max(bestRadius, min(leftDist,rightDist))
        return bestRadius

    def getLeftIndex(self, house:int, heaters:List[int]) -> int:
        leftIndex = -1
        low = 0
        high = len(heaters) - 1
        while(low <= high):
            mid = (int)((low + high ) / 2)
            curHeat = heaters[mid]
            if(curHeat == house):
                leftIndex = mid
                break
            elif(curHeat > house):
                high = mid - 1
            elif(curHeat < house):
                leftIndex = max(leftIndex, mid)
                low = mid + 1
        return leftIndex

    def getRightIndex(self, house:int, heaters:List[int]) -> int:
        rightIndex = float('inf')
        low = 0
        high = len(heaters) - 1
        while(low <= high):
            mid = (int)((low + high ) / 2)
            curHeat = heaters[mid]
            if(curHeat == house):
                rightIndex = mid
                break
            elif(curHeat < house):
                low = mid + 1
            elif(curHeat > house):
                rightIndex = min(rightIndex, mid)
                high = mid - 1
        if(rightIndex == float('inf')):
            rightIndex = -1
        return rightIndex
