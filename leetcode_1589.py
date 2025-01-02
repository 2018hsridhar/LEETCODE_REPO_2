'''
URL := https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/
1589. Maximum Sum Obtained of Any Permutation

For each value, we need to know it's frequency 
Be greedy : most frequent elem => takes largest(nums) most times. Least frequent elem => smallest
10 minutes to solutioning :-)

'''
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        modulo = pow(10,9) + 7
        maxTotalSum = 0
        n = len(nums)
        prefixSum = [0 for idx in range(len(nums))]
        for [start,end] in requests:
            prefixSum[end] += 1
            if(start - 1 >= 0):
                prefixSum[start-1] += -1
        freqs = [0 for idx in range(n)]
        runFreq = 0
        for idx in range(len(freqs) - 1, -1,-1):
            runFreq += prefixSum[idx]
            freqs[idx] = runFreq
        freqs.sort(key = lambda x : -1 * x)
        nums.sort(key = lambda x : -1 * x)
        # print(prefixSum)
        # print(freqs)
        # print(nums)
        for num,freq in zip(nums,freqs):
            maxTotalSum += (num * freq)
        ans = maxTotalSum % modulo
        return ans
        
