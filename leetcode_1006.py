'''
URL = https://leetcode.com/problems/clumsy-factorial/
1006. Clumsy Factorial

15 mins to solutioning :-)
'''
class Solution:
    def clumsy(self, n: int) -> int:
        inMD = True
        secondLayer = []
        while(n > 0):
            if(inMD):
                tempRes = n
                delta = 1
                if(n - 1 >= 1):
                    tempRes *= (n-1)
                    delta += 1
                if(n - 2 >= 1):
                    # not golang here : funcs exported by pkgs lowercase
                    tempRes = math.floor(tempRes / (n-2))
                    delta += 1
                n -= delta
                secondLayer.append(tempRes)
                inMD = False
            elif(not inMD):
                secondLayer.append(n)
                n -= 1
                inMD = True
        clumsyRes = secondLayer[0]
        inAdd = True
        for i in range(1,len(secondLayer), 1):
            curVal = secondLayer[i]
            if(inAdd):
                clumsyRes += curVal
            else:
                clumsyRes -= curVal
            inAdd = not inAdd
        return clumsyRes
