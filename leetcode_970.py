'''
URL := https://leetcode.com/problems/powerful-integers/description/
970. Powerful Integers

Category : Number Theory, Iteration, Computation

Complexity :

Commit Log Messages :
    # not `true`, but, `True`
    #shit : the case of x, y being one -> special case handling here

8 mins to slutioning -> trivial problem
'''
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        myPowerInts = set()
        i = 0
        if(x == 1 and y == 1 and bound >= 2):
            return [2]  
        elif( x == 1 or y == 1) :
            alpha = max(x,y)
            i = 0
            while(True):
                powInt = pow(alpha,i) + 1
                if(powInt > bound):
                    break
                myPowerInts.add(powInt)
                i += 1
        else:
            while(True):
                xI = pow(x,i)
                if(xI > bound):
                    break
                j = 0
                while(True):
                    yJ = pow(y,j)
                    powInt = xI + yJ
                    if(powInt > bound):
                        break
                    myPowerInts.add(powInt)
                    j += 1
                i += 1
        return list(myPowerInts)        
