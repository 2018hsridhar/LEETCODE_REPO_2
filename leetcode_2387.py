'''
2387. Median of a Row Wise Sorted Matrix
URL := https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/description/

Time = O(Mlg(N)lg(R))
Space = O(1) ( Explicit and Implicit ) 

Ehhh circle back to this later TBH
'''
class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        # 9 els -> middle = 4 ( index wise ) range [0,8]
        m = len(grid)
        n = len(grid[0])
        numEls = m * n
        midIndex = 0.5 * ((m * n) - 1 )
        cap = (int)(midIndex)
        median = -1
        low = 1
        high = pow(10,6)
        while(low <= high):
            candid = (int)(0.5 * (low + high))
            numElsLess = 0
            numElsGreater = 0
            for row in range(m):
                curLess = self.bSearchLess(grid[row],candid)
                curMore = self.bSearchMore(grid[row],candid)
                numElsLess += curLess
                numElsGreater += curMore
            # check ranges : bsearch on that range
            # close, but almost there :-)
            upperBound = (numEls - numElsGreater)
            # close - it's in handling of duplicates SMH. 
            # print(numElsLess)
            # print(numElsGreater)
            # print(m*n)
            # print(midIndex)
            # if(numElsLess == cap and numElsGreater == cap):
            if(numElsLess <= midIndex and midIndex <= upperBound):
                # This was the condition !
                if(numElsLess <= cap and numElsGreater <= cap):
                    # oh I mean, we've a median value - but is it guaranteed
                    # seems to be case? I think we get convergence cuz of ineq strictness?
                    median = candid
                    break
                elif(numElsLess > cap):
                    high = candid - 1
                elif(numElsGreater > cap):
                    low = candid + 1
            elif(numElsLess > midIndex):
                high = candid - 1
            elif(midIndex > upperBound):
                low = candid + 1
        return median

    def bSearchLess(self, nums:List[int], target:int) -> int:
        low = 0
        high = len(nums) - 1
        numEls = 0
        while(low <= high):
            mid = (int)(0.5 * (low + high))
            candid = nums[mid]
            if(candid < target):
                low = mid + 1
                numEls = max(numEls,(mid + 1))
            elif(candid >= target):
                high = mid - 1
        return numEls

    def bSearchMore(self, nums:List[int], target:int) -> int:
        low = 0
        high = len(nums) - 1
        n = len(nums)
        numEls = 0
        while(low <= high):
            mid = (int)(0.5 * (low + high))
            candid = nums[mid]
            if(candid > target):
                high = mid - 1
                numEls = max(numEls,n - mid)
            elif(candid <= target):
                low = mid + 1
        return numEls
        
