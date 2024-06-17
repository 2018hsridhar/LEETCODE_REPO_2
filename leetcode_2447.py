'''
URL := https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/
2447. Number of Subarrays With GCD Equal to K

There's no "real good" fast way to execute this algorithm.
Constraints small enough to brute force and calculate based on the Euclidean algorithm anyways
'''
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        numSubArr = 0
        for lPtr, curGCD in enumerate(nums):
            # start from the beginning and ask here
            numSubArr += int(curGCD == k)
            for rPtr in range(lPtr + 1, len(nums), 1):
                curGCD = math.gcd(curGCD, nums[rPtr])
                numSubArr += int(curGCD == k)
        return numSubArr
        
