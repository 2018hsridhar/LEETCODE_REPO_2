'''
3169. Count Days Without Meetings
Variation on the intervals merge problem ( WTF does merging come up so often ) ?
URL := https://leetcode.com/problems/count-days-without-meetings/description/

Complexity
N = len(meetings)
T = O(NlgN)
S = O(1) ( E ) O(1) ( I ) 
'''
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        countOfDays = 0
        meetings.sort(key = lambda x : (x[0],x[1]))
        transform = [meetings[0]]
        del meetings[0]
        for meet in meetings:
            latestMeet = transform[-1]
            if(self.hasOverlap(latestMeet, meet)):
                merged = self.mergeInt(latestMeet,meet)
                del transform[-1]
                transform.append(merged)
            else:
                transform.append(meet)
        for leftIdx in range(len(transform) - 1):
            rightIdx = leftIdx + 1
            leftPair = transform[leftIdx]
            rightPair = transform[rightIdx]
            gapSize = abs(rightPair[0] - leftPair[1]) - 1
            countOfDays += gapSize
        startGap = (transform[0][0] - 1)
        endGap = (days - transform[-1][1])
        countOfDays += startGap
        countOfDays += endGap
        return countOfDays

    def mergeInt(self, m1, m2):
        left = min(m1[0], m2[0])
        right = max(m1[1], m2[1])
        return [left,right]

    def hasOverlap(self, m1, m2):
        caseOne = (m1[0] <= m2[0] and m2[0] <= m1[1])
        caseTwo = (m2[0] <= m1[0] and m1[0] <= m2[1])
        return (caseOne or caseTwo)
        
