'''
1562. Find Latest Group of Size M
URL := https://leetcode.com/problems/find-latest-group-of-size-m/description/

Solution using hashtables : change (start,end) of intervals
And track counts of 1's as we go too

15 minutes spent - almost there :-) 
It's tricky, but your intuitions are almost there. Circle back again later :-) !
'''
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        sMap = dict()
        eMap = dict()
        bestStep = -1
        # For each interval (s,e), capture number of 1's
        # E.g. for interval (0,4), eMap[4] = 5 and sMap[0] = 5 type of thing
        # for interval (4,8), eMap[8] = 5 => leftPos = 4
        # [1] Two maps - start and end - capture changes in the locations of the 1's
        # sMap, eMap mirror-esque images : leverage property
        windowFreq = dict()
        n = len(arr)
        for index,position in enumerate(arr):
            leftPos = position - 1
            rightPos = position + 1
            adjS = position
            adjE = position
            delOldLeftPos = False
            delOldRightPos = False
            if(leftPos >= 1 and leftPos in eMap):
                adjS = leftPos - (eMap[leftPos] - 1) 
                delOldLeftPos = True
            if(rightPos <= n and rightPos in sMap):
                adjE = rightPos + (sMap[rightPos] - 1)
                delOldRightPos = True
            if(delOldLeftPos):
                oldLeft = eMap[leftPos]
                del eMap[leftPos]
                if(leftPos - (oldLeft-1) in sMap):
                    del sMap[leftPos - (oldLeft-1)]
                windowFreq[oldLeft] -= 1
                if(windowFreq[oldLeft] == 0):
                    del windowFreq[oldLeft]
            if(delOldRightPos):
                oldRight = sMap[rightPos]
                del sMap[rightPos]
                if(rightPos + oldRight in eMap):
                    del eMap[rightPos + oldRight]
                windowFreq[oldRight] -= 1
                if(windowFreq[oldRight] == 0):
                    del windowFreq[oldRight]

            # new window information
            window = (adjE - adjS) + 1
            sMap[adjS] = window
            eMap[adjE] = window
            if(window not in windowFreq):
                windowFreq[window] = 0
            windowFreq[window] += 1
            # you are very very close: keep persistent at it
            if(m in windowFreq):
                bestStep = index+1

        return bestStep
        
            

