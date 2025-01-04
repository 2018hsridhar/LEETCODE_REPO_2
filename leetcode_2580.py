'''
2580. Count Ways to Group Overlapping Ranges
URL := https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/description/

Cenarios :
[[1,2],[3,4],[5,6]] => 8 ( 1+3+3+1 )
[[1,2],[3,4],[5,6],[7,8]] => 16
Bernoulli's triangle formual strikes yet again :-)

'''
from math import comb

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        modulo = pow(10,9) + 7
        # 1 integer present : [1,3] and [3,5] have overlap : ranges inclusive!
        numNonOverlapRanges = 1
        ranges.sort(key = lambda x : (x[0],x[1]))
        prevRange = ranges[0]
        del ranges[0]
        for curRange in ranges:
            if(self.hasIntersection(prevRange,curRange)):
                prevRange[1] = max(prevRange[1],curRange[1])
                prevRange[0] = min(prevRange[0],curRange[0])
            else:
                numNonOverlapRanges += 1
                prevRange = curRange
        # print(numNonOverlapRanges)
        # you have number, but need dumb bernoulli formula and can't be inefficient
        # 3C0,3C1,3C2,3C3
        # numWays = 0
        # for x in range(0,numNonOverlapRanges+1,1):
        #     numCombos = (math.comb(numNonOverlapRanges,x)) % modulo
        #     numWays += numCombos 
        # power of 2 in the hiding
        numWays = pow(2,numNonOverlapRanges)
        ans = numWays % modulo       
        return ans

    def hasIntersection(self, rOne:List[int], rTwo:List[int]) -> bool:
        caseOne = (rOne[0] <= rTwo[0] and rTwo[0] <= rOne[1])
        caseTwo = (rTwo[0] <= rOne[0] and rOne[0] <= rTwo[1])
        return (caseOne or caseTwo) 
