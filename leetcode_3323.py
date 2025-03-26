Intuition and Approach
Seems a greedy problem : add one interval
(A) First merge pre=-existing intervals : we can check if any are connectable already
(B) Add longest interval - going to the right
(C) Binary search index of leftmost valid interval and count extra #-intervals
Categories : Sort, Greedy, Single Pass, Array

Complexity
N=len(input)

Time complexity:

O(NlgN)

Space complexity:

O(N) ( Explicit )

O(1) ( Implicit )

Code
'''
3323. Minimize Connected Groups by Inserting Interval
URL := https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/description/
'''
class Solution:
    def minConnectedGroups(self, intervals: List[List[int]], k: int) -> int:
        # [1] Merge the intervals ( with frequency info ) :-) 
        intervals.sort(key = lambda x : (x[0], x[1]))
        curInterval = intervals[0]
        mergeInt = [[curInterval[0], curInterval[1]]]
        del intervals[0]
        for interval in intervals:
            curInterval = mergeInt[-1]
            if(self.hasIntersection(curInterval,interval)):
                toMerge = self.mergeInt(curInterval,interval)
                del mergeInt[-1]
                mergeInt.append(toMerge)
            else:
                mergeInt.append([interval[0],interval[1]])
        targetNumber = len(mergeInt)
        for index,interval in enumerate(mergeInt):
            rightMostPoint = interval[1] + k
            low = index + 1
            high = len(mergeInt) - 1
            bestRightIndex = -1
            while(low <= high):
                mid = math.floor((0.5)*(low + high))
                curInt = mergeInt[mid]
                if(curInt[0] <= rightMostPoint):
                    low = mid + 1
                    bestRightIndex = max(bestRightIndex, mid)
                else:
                    high = mid - 1
            if(bestRightIndex != -1):
                numConnectIntervals = bestRightIndex - index
                connGroupsCount = len(mergeInt) - numConnectIntervals
                targetNumber = min(targetNumber, connGroupsCount)
        return targetNumber

    def hasIntersection(self, segOne: List[int], segTwo: List[int]) -> bool:
        caseOne = (segTwo[0] <= segOne[0] and segOne[0] <= segTwo[1])
        caseTwo = (segOne[0] <= segTwo[0] and segTwo[0] <= segOne[1])
        meetsCriteria = caseOne or caseTwo
        return meetsCriteria

    def mergeInt(self, segOne: List[int], segTwo: List[int]) -> List[int]:
        left = min(segOne[0],segTwo[0])
        right = max(segOne[1],segTwo[1])
        merged = [left,right]
        return merged
