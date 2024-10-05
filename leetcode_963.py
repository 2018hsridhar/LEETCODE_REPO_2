'''
URL := https://leetcode.com/problems/minimum-area-rectangle-ii/description/
963. Minimum Area Rectangle II

Min Area rectangle ( use float hey Python hides this behavior from you ) 

Complexity
Let P := #-points
50 points max
Time = O(pow(P,4))

Close -> some floating point precisoin error going on here
[[2,1],[2,3],[3,1],[3,3]]

How to test all orders of points here?
'''
import math

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        minAreaRect = float('inf')
        targetConst = pi * 0.5
        for i in range(0,len(points),1):
            for j in range(i+1,len(points),1):
                for k in range(j+1,len(points),1):
                    for l in range(k+1,len(points),1):
                        point1 = points[i]
                        point2 = points[j]
                        point3 = points[k]
                        point4 = points[l]
                        # six orders to test out ( keep point one fixed ) 
                        vecOne = self.makeVec(point1,point2)
                        vecTwo = self.makeVec(point2,point3)
                        vecThree = self.makeVec(point3,point4)
                        vecFour = self.makeVec(point4,point1)
                        thetaOne = abs(self.getTheta(vecOne,vecTwo))
                        thetaTwo = abs(self.getTheta(vecTwo,vecThree))
                        thetaThree = abs(self.getTheta(vecThree,vecFour))
                        thetaFour = abs(self.getTheta(vecFour,vecOne))
                        if(thetaOne == targetConst and thetaOne == thetaTwo and thetaTwo == thetaThree and thetaThree == thetaFour):
                            curAreaRect = self.magnitude(vecOne) * self.magnitude(vecTwo)
                            minAreaRect = min(minAreaRect, curAreaRect)
        if (minAreaRect == float('inf')):
            minAreaRect = 0
        return minAreaRect

    def getTheta(self, vecOne:List[int], vecTwo:List[int]) -> float:
        numerator = self.dotProd(vecOne,vecTwo)
        denominator = self.magnitude(vecOne) * self.magnitude(vecTwo)
        targetExpr = numerator / denominator
        theta = acos(targetExpr)
        return theta

    def makeVec(self, vecOne: List[int], vecTwo: List[int]) -> List[float]:
        vector = []
        for a,b, in zip(vecOne,vecTwo):
            vector.append(b-a)
        return vector

    def dotProd(self, vecOne: List[int], vecTwo: List[int]) -> float:
        mag = 0.0
        for a,b in zip(vecOne,vecTwo):
            mag += (a * b)
        return mag

    def magnitude(self, vec: List[int]) -> float:
        mag = math.sqrt(self.dotProd(vec,vec))
        return mag






        
