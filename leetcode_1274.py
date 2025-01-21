# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

'''
1274. Number of Ships in a Rectangle
URL := https://leetcode.com/problems/number-of-ships-in-a-rectangle/description/

Clarifying questions :
- each integer point @ most 1 ship
- handle the boundary condition
- 10 ships @ max in a rectangle

Thought Process :
- seems like a quadTree esque recursive divide-and-conquer problem
- 1K dimensionality max topRight : [1000 x 1000] 2D-grid

Complexity
15 mins dumb recursion errors here SMH
'''

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        shipCount = self.internalHelper(sea, bottomLeft, topRight)
        return shipCount

    # Classifical internal function structure :-) !
    # Use API only ( a blindfolded case no access to underneath abstractions ) 
    def internalHelper(self, sea: 'Sea', bottomLeft: 'Point', topRight: 'Point',) -> int:
        curShipCount = 0
        x1 = bottomLeft.x
        y1 = bottomLeft.y
        x2 = topRight.x
        y2 = topRight.y
        # Bounds checking a lot here
        if(x1 >= 0 and x2 >= 0 and y1 >= 0 and y2 >= 0 and x1 <= x2 and y1 <= y2):
            if(sea.hasShips(topRight,bottomLeft)):
                # SMH dumb recursive depth case
                if(x1 == x2 and y1 == y2):
                    return 1
                xMid = (int)((0.5)*(x1 + x2))
                yMid = (int)((0.5)*(y1 + y2))
                midPoint = Point(xMid,yMid)
                # It's quadrants, but caeful on the mid eval
                # SMH recursive have to extert bad caution here : not even rectangles TBH
                q1 = self.internalHelper(sea, Point(xMid+1,yMid+1),topRight)
                q2 = self.internalHelper(sea,Point(x1,yMid+1),Point(xMid,y2))
                q3 = self.internalHelper(sea, bottomLeft,Point(xMid,yMid))
                q4 = self.internalHelper(sea,Point(xMid+1,y1),Point(x2,yMid))
                # special case : only one quadrant -> ret one
                curShipCount += (q1+q2+q3+q4)
        return curShipCount
        
