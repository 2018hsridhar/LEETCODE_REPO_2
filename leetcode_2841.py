'''
URL := https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/description/
2841. Maximum Sum of Almost Unique Subarray

Categories : hashmap, sliding window, array, two pointers, linear scan
Complexity
T = O(N)
S = O(N) ( Explicit ) O(1) ( Implicit ) 

k is a known : almost unique ( at least m distinct )
'''
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        runSum = 0
        maxSum = 0
        lPtr = 0
        # `NameError` for names not defined
        freqMap = dict()
        for rPtr,num in enumerate(nums):
            if(num not in freqMap):
                freqMap[num] = 0
            freqMap[num] += 1
            runSum += num
            if(rPtr >= k):
                lPtr = rPtr - k
                leftEl = nums[lPtr]
                nextFreq = freqMap[leftEl] - 1
                freqMap[leftEl] = nextFreq
                if(nextFreq == 0):
                    del freqMap[leftEl]
                runSum -= leftEl 
            curNumEls = len(freqMap)
            if(curNumEls >= m and rPtr >= k - 1):
                maxSum = max(maxSum,runSum)
        return maxSum
        
