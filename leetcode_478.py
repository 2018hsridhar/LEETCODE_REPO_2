'''
URl := https://leetcode.com/problems/generate-random-point-in-a-circle/description/
478. Generate Random Point in a Circle

Who the heck was bright enough to figure out a circle could be reduced to two dimensions : theta and r?
Triangle properties built up to intuitions :-O 

Complexity : O(1) All operations ( not focused on URD - uniform random distribution - library)

'''
import math
import random 

class Solution:

    # we need theta as an offset, and the center as the vector starting point
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.cx = x_center
        self.cy = y_center

    # Uniform random points ( includes points on the circle )
    def randPoint(self) -> List[float]:
        # felled by a lack of a square root woah
        radius_mx = math.sqrt(random.uniform(0,1))
        theta = random.uniform(0,360)
        # theta = theta_mx * 360
        hypotheneuse = radius_mx * self.radius
        x_dist = hypotheneuse * math.sin(math.radians(theta))
        y_dist = hypotheneuse * math.cos(math.radians(theta))
        px  = self.cx + x_dist
        py = self.cy + y_dist
        point = [px,py]
        return point
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
