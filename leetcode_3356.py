'''
URL := https://leetcode.com/problems/zero-array-transformation-ii/description/
3356. Zero Array Transformation II

No need for array - leverage a map of indices for query building on bsearch approach 

T = O(Nlg(Q))
S = O(Q) ( Exp ) O(1) ( Imp ) 

Super close ( the zero case here )!
'''
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        meetsBaseCase = True
        for num in nums:
            if(num > 0):
                meetsBaseCase = False
                break
        if(meetsBaseCase):
            return 0
        bestK = float('inf')
        low = 0
        high = len(queries) - 1
        while(low <= high):
            mid = (int)((0.5)*(low + high))
            queryMap = dict()
            # 1. Build queries
            for qPtr in range(mid+1):
                [left,right,qVal] = queries[qPtr]
                if(right not in queryMap):
                    queryMap[right] = 0
                queryMap[right] += qVal
                actualLeft = left - 1
                if(actualLeft >= 0):
                    if(actualLeft not in queryMap):
                        queryMap[actualLeft] = 0
                    queryMap[actualLeft] += (-1 * qVal)
            # 2. Go throguh each elem, backwards, and test
            delta = 0
            becomesZeroArray = True
            for elemPtr in range(len(nums) - 1, -1,-1):
                elem = nums[elemPtr]
                if(elemPtr in queryMap):
                    delta += queryMap[elemPtr]
                newElem = elem - delta
                if(newElem > 0):
                    becomesZeroArray = False
                    break
            if(becomesZeroArray):
                high = mid - 1
                bestK = min(mid+1,bestK)
            elif(not becomesZeroArray):
                low = mid + 1
        if(bestK == float('inf')):
            bestK = -1
        return bestK

        
