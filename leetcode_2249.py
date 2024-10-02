Intuition and Approach
Each circle is inscribed in some "square" with a square length = diameter. Figure out the corner points of each square, enumerate, and count the number of unseen, valid lattice points.

Complexity
Time complexity:
C:=#−circles
X:=maximalsquaredistanceofanycircle
O(C∗pow(X,2))

Space complexity:
O(C∗pow(X,2)) ( Explicit )
O(1) ( Implicit )

Code
'''
2249. Count Lattice Points Inside a Circle
Two hundred circles max and a bound of x_i,y_i is also known
URL := https://leetcode.com/problems/count-lattice-points-inside-a-circle/description/
'''
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        totalNumLatticePoints = 0
        visitedPoints = dict()
        for circle in circles:
            # python doesn't really shield you from terribel scope issues :-(
            numLatticeInCircle = self.getCircleUnseenLatticePoints(circle, visitedPoints)
            totalNumLatticePoints += numLatticeInCircle
        return totalNumLatticePoints

    def getCircleUnseenLatticePoints(self, circle:List[int], visitedPoints: dict()) -> int:
        numUnseenLatticePoints = 0 
        # array destructing assignemnt!
        [cx,cy,radius] = circle
        left = cx - radius
        right = cx + radius
        top = cy - radius
        bottom = cy + radius
        # range loop step syntax super clean
        for px in range(left,right+1,1):
            for py in range(top,bottom+1,1):
                # self.<...> method dispatch bind to the class
                distToCenter = self.l2Norm(px,cx,py,cy)
                if(distToCenter <= radius):
                    if(px not in visitedPoints):
                        visitedPoints[px] = set()
                    yPointsForX = visitedPoints[px]
                    if(py not in yPointsForX):
                        visitedPoints[px].add(py)
                        numUnseenLatticePoints += 1
        return numUnseenLatticePoints

    # gotta import the math module
    # do library imports have to be at the top?
    def l2Norm(self, x1,x2,y1,y2) -> float:
        xDist = abs(x2-x1)
        yDist = abs(y2-y1)
        return math.sqrt(pow(xDist,2) + pow(yDist,2))



