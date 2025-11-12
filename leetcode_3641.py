'''
3641. Longest Semi-Repeating Subarray
URL := https://leetcode.com/problems/longest-semi-repeating-subarray/

sliding window technique ( 2 pointers ) 
Complexity
N = len(nums)
T = O(N) S = O(N) ( E ) O(1) ( I ) 
'''
from collections import defaultdict

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        lsa = leftPtr = rightPtr = 0
        kRepSet = set()
        valFreq = defaultdict(int)
        THRESHOLD = 2
        CUTOFF = 1
        for rightPtr in range(len(nums)):
            # [1] Get right val and add it in
            rightVal = nums[rightPtr]
            valFreq[rightVal] += 1
            if(valFreq[rightVal] >= THRESHOLD):
                kRepSet.add(rightVal)
            # [2] test len ( at most ) 
            # [2a] evict from kRepSet if > THRESHOLD
            while(len(kRepSet) > k and leftPtr <= rightPtr):
                leftVal = nums[leftPtr]
                valFreq[leftVal] -= 1
                if(valFreq[leftVal] == CUTOFF and leftVal in kRepSet):
                    kRepSet.remove(leftVal)
                elif(valFreq[leftVal] == 0):
                    del valFreq[leftVal] # clean memory footprint dynamically
                leftPtr += 1
            if(len(kRepSet) <= k):
                window = rightPtr - leftPtr + 1
                lsa = max(lsa, window)
        return lsa
        
