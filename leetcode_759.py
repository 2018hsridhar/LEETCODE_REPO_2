"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
'''
759. Employee Free Time
URL := https://leetcode.com/problems/employee-free-time/description/

Common, positive-len free time - all employees

Categories : Iterative, Sorting, Greedy, Intervals Extension

Complexity
E = #-employees, M = #-intervals per employee, N = E * M
N = #-intervals
T = O(NlogN)
S = O(N) ( E ) O(1) ( I ) 
10 minute solutioned :-) 
'''
class Solution:
    # Ahhh we need to return a List of intervals here
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        allIntervals = []
        busyTimes = []
        for employee in schedule:
            for interval in employee:
                allIntervals.append([interval.start,interval.end])
        allIntervals.sort(key = lambda x : (x[0],x[1]))
        for curInt in allIntervals:
            if(len(busyTimes) == 0):
                busyTimes.append(curInt)
            elif(len(busyTimes) > 0):
                mostRecentInt = busyTimes[-1]
                if(self.hasIntersection(mostRecentInt,curInt)):
                    mergedInt = self.merge(mostRecentInt,curInt)
                    del busyTimes[-1]
                    busyTimes.append(mergedInt)
                else:
                    busyTimes.append(curInt)
        busyTimes.sort(key = lambda x : (x[0],x[1]))
        freeTimes = []
        for ptr in range(len(busyTimes) - 1):
            intOne = busyTimes[ptr]
            intTwo = busyTimes[ptr+1]
            if(intOne[1] < intTwo[0]):
                freeInterval = Interval(intOne[1],intTwo[0])
                freeTimes.append(freeInterval)
        return freeTimes

    # Merges on inclusivity -> no exclusive ( [a,5] and [5,x] can merge )
    def hasIntersection(self, intOne:List[int], intTwo:List[int]) -> bool:
        x1 = intOne[0]
        y1 = intOne[1]
        x2 = intTwo[0]
        y2 = intTwo[1]
        intersectionality = (x1 <= x2 and x2 <= y1) or (x2 <= x1 and x1 <= y2)
        return intersectionality

    def merge(self, intOne:List[int], intTwo:List[int]) -> List[int]:
        left = min(intOne[0], intTwo[0])
        right = max(intOne[1], intTwo[1])
        merged = [left,right]
        return merged

        
