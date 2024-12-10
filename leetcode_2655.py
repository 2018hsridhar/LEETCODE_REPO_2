'''
URL := https://leetcode.com/problems/find-maximal-uncovered-ranges/description/
2655. Find Maximal Uncovered Ranges
Classic range coverage sort intervals ASC order type of problem - spin / variation of other problems TBH

Complexity
N := len(ranges)
Time = O(nlgn)
S = O(1) ( Exp and Imp )
'''
class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        # sort ranges ASC order
        ranges.sort(key = lambda x : (x[0],x[1]))
        mergedRanges = []
        for curRange in ranges:
            if(len(mergedRanges) == 0):
                mergedRanges.append(curRange)
            else:
                mostRecent = mergedRanges[-1]
                if(self.hasIntersection(mostRecent,curRange)):
                    modifRange = self.mergeIntervals(mostRecent,curRange)
                    mergedRanges[-1] = modifRange
                else:
                    mergedRanges.append(curRange)
        # Some cells covered : other cells uncovered
        # must be maximal length ( or not ) 
        # sort by start point ASC order ( huh calculate later ) 
        answer = []
        if(len(mergedRanges) == 0):
            return [[0,n-1]]
        firstRange = mergedRanges[0]
        if(firstRange[0] > 0):
            headUncov = [0,firstRange[0] - 1]
            answer.append(headUncov)
        for ptr in range(len(mergedRanges) - 1):
            rangeOne = mergedRanges[ptr]
            rangeTwo = mergedRanges[ptr + 1]
            if(rangeOne[1] < rangeTwo[0] - 1):
                uncovLeft = rangeOne[1] + 1
                uncovRight = rangeTwo[0] - 1
                uncovRange = [uncovLeft,uncovRight]
                answer.append(uncovRange)
        lastRange = mergedRanges[-1]
        if(lastRange[1] != n - 1):
            tailUncov = [lastRange[1] + 1, n-1]
            answer.append(tailUncov)
        return answer

    def hasIntersection(self, a: List[int], b:List[int]) -> bool:
        caseOne = (a[0] <= b[0]) and (b[0] <= a[1])
        caseTwo = (b[0] <= a[0]) and (a[0] <= b[1])
        status = (caseOne or caseTwo)
        return status

    def mergeIntervals(self, a: List[int], b:List[int]) -> List[int]:
        left = min(a[0],b[0])
        right = max(a[1],b[1])
        interval = [left,right]
        return interval
