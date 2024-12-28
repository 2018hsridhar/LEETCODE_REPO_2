'''
1983. Widest Pair of Indices With Equal Range Sum
https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/description/

Complexity
N = len(input)
T = O(N)
S = O(N) ( Explicit ) O(1) ( Implicit 0 

Solutioned 10-15 minutes :-)
'''
class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        prefixSum = 0
        prefixIndices = dict()
        largestDistance = 0
        if(len(nums1) == 1):
            return (int)(nums1[0] == nums2[0])
        for rightIdx in range(len(nums1)):
            n1 = nums1[rightIdx]
            n2 = nums2[rightIdx]
            delta = n1 - n2
            prefixSum += delta
            if(prefixSum not in prefixIndices):
                prefixIndices[prefixSum] = rightIdx
            target = prefixSum
            if(target in prefixIndices):
                leftIdx = prefixIndices[target]
                curDistance = rightIdx - leftIdx
                largestDistance = max(largestDistance, curDistance)
            if(target == 0):
                curDistance = rightIdx + 1
                largestDistance = max(largestDistance, curDistance)
        return largestDistance

        
