'''
523. Continuous Subarray Sum
URL := https://leetcode.com/problems/continuous-subarray-sum/

Check if we have an array ( length critiera ) - not actual max Len
Always want leftmost ( greedy ) 
Edge case : If not in array -> if we meet k = 6 ( or 0 ) value -> full prefix sum
'''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = 0
        remIndices = {}
        threshold = 2
        remIndices[0] = -1
        haveGoodSubArr = False
        for rPtr,num in enumerate(nums):
            prefixSum += num
            rem = (prefixSum % k)
            if(rem not in remIndices):
                remIndices[rem] = rPtr
            lPtr = remIndices[rem]
            window = (rPtr - lPtr)
            if(window >= threshold):
                haveGoodSubArr = True
                break
        return haveGoodSubArr



