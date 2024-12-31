'''
2461. Maximum Sum of Distinct Subarrays With Length K
URL := https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

Complexity
N = len(input)
T = O(N)
S = O(K) ( Explicit ) O(1) ( Implicit ) 

'''
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = 0
        elFreq = dict()
        runSum = 0
        leftPtr = 0
        # enumerate(...) as unpacking an object code
        for rightPtr,num in enumerate(nums):
            runSum += num
            if(num not in elFreq):
                elFreq[num] = 0
            elFreq[num] += 1
            if(rightPtr >= k):
                leftPtr = rightPtr - k
                leftEl = nums[leftPtr]
                elFreq[leftEl] -= 1
                if(elFreq[leftEl] == 0):
                    del elFreq[leftEl]
                runSum -= leftEl
            if(rightPtr >= k-1 and len(elFreq) == k):
                maxSum = max(maxSum,runSum)
        return maxSum
