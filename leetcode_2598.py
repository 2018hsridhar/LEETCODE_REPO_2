'''
2598. Smallest Missing Non-negative Integer After Operations
URL := https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description/
Apply ops any number of times -> get modulo -> think greedily -> add offsets to remainders

N := len(nums)
Time = O(NlgN)
Space = O(N) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        modFreq = dict()
        for num in nums:
            mod = num % value
            if(mod not in modFreq):
                modFreq[mod] = 0
            modFreq[mod] += 1
        remainders = []
        for mod,freqMod in modFreq.items():
            for scale in range(freqMod):
                remVal = mod + (scale*value)
                remainders.append(remVal)
        remainders.sort()
        if(remainders[0] > 0):
            curMex = 0
            return 0
        else:
            for idx in range(len(remainders) - 1):
                valOne = remainders[idx]
                valTwo = remainders[idx+1]
                if(valTwo - valOne > 1):
                    curMex = valOne + 1
                    return curMex
            curMex = remainders[-1] + 1
        return curMex


        
