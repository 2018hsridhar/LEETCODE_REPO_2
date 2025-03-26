'''
URL := https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/
3394. Check if Grid can be Cut into Sections

'''
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        hasValidCuts = False
        hozBars = []
        vertBars = []
        for [sx,sy,ex,ey] in rectangles:
            hozBar = [sx,ex]
            vertBar = [sy,ey]
            hozBars.append(hozBar)
            vertBars.append(vertBar)
        hozBars.sort(key = lambda x : (x[0],x[1]))
        vertBars.sort(key = lambda x : (x[0],x[1]))
        hozMerge = self.mergeIntervals(hozBars)
        vertMerge = self.mergeIntervals(vertBars)
        threshold = 2
        if(len(hozMerge) > threshold or len(vertMerge) > threshold):
            hasValidCuts = True
        return hasValidCuts

    def mergeIntervals(self, bars:List[int]) -> List[int]:
        merged = [bars[0]]
        del bars[0]
        for bar in bars:
            latestInt = merged[-1]
            if(self.hasOverlap(latestInt,bar)):
                mergeInt = self.merge(latestInt,bar)
                del merged[-1]
                merged.append(mergeInt)
            else:
                merged.append(bar)
        return merged

    def merge(self, intOne:List[int], intTwo:List[int]) -> List[int]:
        merged = [min(intOne[0],intTwo[0]), max(intOne[1],intTwo[1])]
        return merged

    def hasOverlap(self, intOne:List[int], intTwo:List[int]) -> bool:
        caseOne = (intOne[0] <= intTwo[0] and intTwo[0] < intOne[1])
        caseTwo = (intTwo[0] <= intOne[0] and intOne[0] < intTwo[1])
        return (caseOne or caseTwo)
