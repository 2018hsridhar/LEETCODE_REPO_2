'''
2345. Finding the Number of Visible Mountains
URL := https://leetcode.com/problems/finding-the-number-of-visible-mountains/description/

Complexity
N = #-mountains
T = O(NlgN)
T = O(N) ( E ) O(1) ( I ) 

Cases :
Equality assessment is easy : lp = lc and rp = rc type of deal

If this were axis aligned though
(A) [[1,3],[1,3],[1,3],[4,6],[4,6]] -> 0
(B) [[1,10],[1,10],[5,3]] -> 0

Actually you're close ( 2 test cases failing ) 
'''
class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        FALSE_ID = float('-inf')
        numMountains = 0
        intervals = []
        for peakId,peak in enumerate(peaks):
            [x,y] = peak
            left = x - y
            right = x + y
            window = [left,right,peakId]
            intervals.append(window)
        intervals.sort(key = lambda x : (x[0],x[1]))
        # Intervals merge problem ( in the hiding ) -> greedy too
        # Imposition of lexical ordering
        # Greedy, sorted, continuous leftwards expansion idea
        curInterval = intervals[0]
        intervals.pop(0)
        numMountains = len(peaks)
        invisibleMountains = set()
        while(len(intervals) > 0):
            childInt = intervals.pop(0)
            [curLeft,curRight,curId] = curInterval
            [childLeft,childRight,childId] = childInt
            # if intersection, test the type of intersection
            if(self.hasIntersection(childInt,curInterval)):
                childInCur = self.isContained(childInt,curInterval)
                curInChild = self.isContained(curInterval,childInt)
                if(childInCur or curInChild):
                    if(childInCur and curInChild):
                        invisibleMountains.add(curId)
                        invisibleMountains.add(childId)
                    elif(childInCur):
                        invisibleMountains.add(childId)
                    elif(curInChild):
                        invisibleMountains.add(curId)
                    leftmost = min(curLeft,childLeft)
                    rightmost = max(curRight,childRight)
                    curInterval = [leftmost,rightmost,FALSE_ID]
                else:
                    # intersections, but not contained : the peaks are seperate.
                    # please march rightwards
                    curInterval = childInt
            else: # failed interesction ( there exist a gap between mountains )
                curInterval = childInt
        if(FALSE_ID in invisibleMountains):
            invisibleMountains.remove(FALSE_ID)
        visibleMountains = numMountains - len(invisibleMountains)
        return visibleMountains


    def isContained(self,smaller,bigger) -> bool:
        [l1,r1,i1] = smaller
        [l2,r2,i2] = bigger
        if(l2 <= l1 and r1 <= r2):
            return True
        return False

    def hasIntersection(self,intOne,intTwo) -> bool:
        [l1,r1,i1] = intOne
        [l2,r2,i2] = intTwo
        return (l1 <= l2 and l2 <= r1) or (l2 <= l1 and l1 <= r2 )
