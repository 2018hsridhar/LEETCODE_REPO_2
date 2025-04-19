'''
URL := https://leetcode.com/problems/one-edit-distance/description/
161. One Edit Distance

Careful case : both strings equal - no differetn character - ret false

'''
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        if(s == t):
            return False
        lenDelta = abs(lenS - lenT)
        THRESH = 2
        if(lenDelta >= THRESH):
            return False
        sPtr = 0
        tPtr = 0
        numOps = 0
        while(sPtr < len(s) and tPtr < len(t)):
            sLet = s[sPtr]
            tLet = t[tPtr]
            if(sLet != tLet):
                # del and check
                if(numOps == 0):
                    if(len(s) > len(t)):
                        sPtr += 1
                        numOps += 1
                    elif(len(s) < len(t)):
                        # insert into s
                        tPtr += 1
                        numOps += 1
                    else:
                        sPtr += 1
                        tPtr += 1
                        numOps += 1
                elif(numOps == 1):
                    return False
            else:
                sPtr += 1
                tPtr += 1
        return True



                    
