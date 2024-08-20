Intuition
Approach
Brute Force O(N^2) Approach ( no TLE ) to Solution, using intersection of two rectangles checking.
Make sure not to compute for cases where two rectangles do not intersection ( thus yielding an area of 0 ) when other pairwise combinations of rectangles would yield an actual positive minimal intersection for square area.

Complexity
Time complexity:
Let N := #-rectangles
Time = O(N^2)

Space complexity:
Space = O(1) ( Explicit ) O(1) ( implicit/recursive call stack )

Code
# URL := https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description/
# 3047. Find the Largest Area of Square Inside Two Rectangles
# 1000 rectangles at max : 10e6 pairwise intersections to compute
# Do inefficiency issues with O(pow(n,2)) arise up in compute?
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        lsa = 0
        n = len(bottomLeft)
        for i in range(n):
            for j in range(i+1,n,1):
                rectOne = [bottomLeft[i][0], bottomLeft[i][1], topRight[i][0], topRight[i][1]]
                rectTwo = [bottomLeft[j][0], bottomLeft[j][1], topRight[j][0], topRight[j][1]]
                rectIntersect = self.getIntersectRect(rectOne,rectTwo)
                if(len(rectIntersect) == 4):
                    xLen = abs(rectIntersect[2] - rectIntersect[0])
                    yLen = abs(rectIntersect[1] - rectIntersect[3])
                    squareLen = min(xLen,yLen)
                    # pow() optimized over * operator?
                    lsa = max(lsa, pow(squareLen,2))
        return lsa

    # in form (x1,y1,x2,y2)
    def getIntersectRect(self,rectOne:List[int], rectTwo:List[int]) -> int:
        x1 = max(rectOne[0], rectTwo[0])
        x2 = min(rectOne[2], rectTwo[2])
        y1 = max(rectOne[1], rectTwo[1])
        y2 = min(rectOne[3], rectTwo[3])
        if(x1 <= x2 and y1 <= y2):
            targetRect = [x1,y1,x2,y2]
        else:
            targetRect = []
        return targetRect
        
