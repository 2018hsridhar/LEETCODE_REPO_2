'''
URL := https://leetcode.com/problems/count-number-of-bad-pairs/description/
2364. Count Number of Bad Pairs

'''
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        deltas = [(nums[idx] - idx) for idx in range(len(nums))]
        deltaFreq = dict()
        for delta in deltas:
            if(delta not in deltaFreq):
                deltaFreq[delta] = 0
            deltaFreq[delta] += 1
        numGoodPairs = 0
        n = len(nums)
        numPairsTotal = self.snn(n - 1)
        # print(deltaFreq)
        for candid, candidFreq in deltaFreq.items():
            if(candidFreq >= 2):
                numGoodPairs += self.snn(candidFreq - 1)
        numBadPairs = numPairsTotal - numGoodPairs
        return numBadPairs

    def snn(self, x:int) -> int:
        if(x <= 0):
            return 0
        target = 0
        target = (int)((x+1)*x * 0.5)
        return target
        
