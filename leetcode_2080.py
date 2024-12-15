'''
URL := https://leetcode.com/problems/range-frequency-queries/description/
2080. Range Frequency Queries

Intuition and Approach
1. The value is a known, and suppose we had indices in sorted order
2. Let's leverage binary search to establish frequency quickly
3. All indices are unique
4. Cache indices since queries computed frequently

N := #-valus in array
Q := #-queries
T = O(QlgN)
S = O(N) ( Exp ) O(1) ( Imp ) 
'''
class RangeFreqQuery:


    def __init__(self, arr: List[int]):
        self.indexMap = dict()
        for idx,val in enumerate(arr):
            if(val not in self.indexMap):
                self.indexMap[val] = []
            self.indexMap[val].append(idx)

    def query(self, left: int, right: int, value: int) -> int:
        valFreq = 0
        if(value not in self.indexMap):
            return 0
        indices = self.indexMap[value]
        firstIdx = indices[0]
        lastIdx = indices[-1]
        # left < firstIdx : includes all values
        leftBound = 0
        if(left < firstIdx):
            leftBound = 0
        else:
            leftBound = self.bSearchLower(indices,left)
        rightBound = float('inf')
        if(right > lastIdx):
            rightBound = len(indices) - 1
        else:
            rightBound = self.bSearchUpper(indices, right)
        valFreq = abs(rightBound - leftBound + 1) # idx : 0,2 -> 3 :-)
        if(valFreq == float('inf')):
            valFreq = 0
        return valFreq

    # value closest to lowerBound ( or exactly lower Bound)
    # if lowerBound < index, return -1 too
    def bSearchLower(self, indices:List[int], lowerIdx:int) -> int:
        bestIdx = float('inf')
        low = 0
        high = len(indices) - 1
        while(low <= high):
            mid = (int)(0.5 * (low + high))
            val = indices[mid]
            if(val < lowerIdx):
                low = mid + 1
            elif(val > lowerIdx):
                bestIdx = min(bestIdx,mid)
                high = mid - 1
            elif(val == lowerIdx):
                bestIdx = mid
                break
        return bestIdx

    def bSearchUpper(self, indices:List[int], upperIdx:int) -> int:
        bestIdx = float('-inf')
        low = 0
        high = len(indices) - 1
        while(low <= high):
            mid = (int)(0.5 * (low + high))
            val = indices[mid]
            if(val < upperIdx):
                bestIdx = max(bestIdx,mid)
                low = mid + 1
            elif(val > upperIdx):
                high = mid - 1
            elif(val == upperIdx):
                bestIdx = mid
                break
        return bestIdx


        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
