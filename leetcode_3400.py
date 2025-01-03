'''
3400. Maximum Number of Matching Indices After Right Shifts
URL := https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/description/
3K els max -> simulate and call it a day :-)

T = O(pow(N,2))
S = O(1) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def maximumMatchingIndices(self, nums1: List[int], nums2: List[int]) -> int:
        maxMatchingIndex = 0
        k = len(nums2)
        offset = 0
        for iterations in range(len(nums2)):
            curNumMaxMatch = 0
            for indexOne in range(len(nums1)):
                adjIndexTwo = (indexOne + offset) % k
                valOne = nums1[indexOne]
                valTwo = nums2[adjIndexTwo]
                if(valOne == valTwo):
                    curNumMaxMatch += 1
            maxMatchingIndex = max(maxMatchingIndex, curNumMaxMatch)
            offset += 1
        return maxMatchingIndex
