'''
URL := https://leetcode.com/problems/minimum-rectangles-to-cover-points/description/
3111. Minimum Rectangles to Cover Points

Good geometry-based problem : rectangular covering -> greedy based sort
N := #-points
T := O(nlgn)
S := O(1) ( I ) O(1) ( E) 

It's a sliding window, but this time, geometric :-)

'''
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        numRect = 0
        points.sort()
        # huh defautl behavior lex sort does work
        curWidth = 0
        curPointX = points[0][0]
        for i in range(len(points)):
            nextPointX = points[i][0]
            if(nextPointX > curPointX):
                curWidth += (nextPointX - curPointX)
                if(curWidth > w):
                    numRect += 1
                    curWidth = 0
                curPointX = nextPointX
        numRect += 1
        return numRect

        
