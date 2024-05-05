'''
659. Split Array into Consecutive Subsequences
URL = https://leetcode.com/problems/split-array-into-consecutive-subsequences/


'''
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        isPoss = True
        numFreq = {}
        for val in nums:
            if val not in numFreq:
                numFreq[val] = 0
            numFreq[val] += 1
        for k, v in numFreq.items():
            valLeftTwo = k - 2
            valLeftOne = k - 1
            valRightOne = k + 1
            valRightTwo = k + 2
            countLeft = 0
            countRight = 0
            countMid = 0
            leftRem = numFreq[valLeftOne] if valLeftOne in numFreq else 0
            rightRem = numFreq[valRightOne] if valRightOne in numFreq else 0
            # we need remaining on the left and on the right -> not the chains on the left and the right
            if(valLeftTwo in numFreq and valLeftOne in numFreq):
                countLeft = min(v,min(numFreq[valLeftTwo],numFreq[valLeftOne]))
                leftRem = numFreq[valLeftOne] - countLeft
            if(valRightTwo in numFreq and valRightOne in numFreq):
                countRight = min(v,min(numFreq[valRightOne], numFreq[valRightTwo]))
                rightRem = numFreq[valRightOne] - countRight
            # don't mid count if left and right already include
            if(valLeftOne in numFreq and valRightOne in numFreq):
                countMid = max(0,min(v, min(leftRem,rightRem)))
            totalChainCount = countLeft + countMid + countRight
            if(totalChainCount < numFreq[k]):
                isPoss = False
                break
        return isPoss
        
