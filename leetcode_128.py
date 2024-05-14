'''
URL := https://leetcode.com/problems/longest-consecutive-sequence/description/
128. Longest Consecutive Sequence

Category : Sets, Maps?, Linear Scan, Iteration, Math, Counting

Complexity :
Let N := number of elements
Time := O(N)
Space := O(N) ( E ) O( 1 ) ( I ) 

Correct but ran into a TLE
Correct but seems like repeated work?
How to avoid repetitive work here?
Sorted key structure?

'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestConsec = 0
        numSet = set(nums)
        visitedNums = set()
        for numKey in numSet:
            if(numKey not in visitedNums):
                # de-facto one element : always start there
                curSeqLen = 1
                # the negative side
                nextVal = numKey - 1
                while(nextVal in numSet and nextVal not in visitedNums):
                    curSeqLen += 1
                    visitedNums.add(nextVal)
                    nextVal = nextVal - 1
                # then the positive side
                nextVal = numKey + 1
                while(nextVal in numSet and nextVal not in visitedNums):
                    curSeqLen += 1
                    visitedNums.add(nextVal)
                    nextVal = nextVal + 1
                longestConsec = max(longestConsec, curSeqLen)
        return longestConsec
        
