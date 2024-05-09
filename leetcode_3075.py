'''
URL := https://leetcode.com/problems/maximize-happiness-of-selected-children/description/
3075. Maximize Happiness of Selected Children
'''
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        mhs = 0
        # in-place modification
        happiness.sort(reverse=True)
        for idx, initVal in enumerate(happiness):
            if(idx == k):
                break
            mhs += max(0,initVal - idx)
        return mhs
        
