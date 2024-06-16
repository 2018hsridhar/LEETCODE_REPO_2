'''
718. Maximum Length of Repeated Subarray
URL := https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/

Category : Strings, HashMaps, Enumeration, Nested For Loops

Complexity
Let N := len(max array)
T = O(N^2)
S = O(N^2) ( E ) O(1) ( I ) 

Hit a TLE ( it is a working solution though ! )
Accepted ( but hilariously slow ) -> stinking string appends library thing 
Probably should do DP solution instead!

'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        maxLengthRep = 0
        myArrayKeys = set()
        # nums1 iterate and populate set
        seperator = "-"
        for lPtr in range(len(nums1)):
            curKey = ""
            for rPtr in range(lPtr,len(nums1), 1):
                curKey += (str(nums1[rPtr]) + seperator)
                if(curKey not in myArrayKeys):
                    myArrayKeys.add(curKey)
        # nums2 : iterate, check set, and check lengths
        for lPtr in range(len(nums2)):
            curKey = ""
            seperatorCount = -1
            for rPtr in range(lPtr,len(nums2), 1):
                curKey += (str(nums2[rPtr]) + seperator)
                seperatorCount += 1
                if(curKey in myArrayKeys):
                    actualLen = seperatorCount + 1
                    maxLengthRep = max(maxLengthRep, actualLen)
        return (int)(maxLengthRep)
        
