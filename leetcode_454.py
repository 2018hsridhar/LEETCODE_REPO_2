'''
URL := https://leetcode.com/problems/4sum-ii/description/
454. 4Sum II

Category : Dimension Reduction, Linear Scan Passes, Additive Operations, Enumeration

Complexity
Let N := len(worst vector)
T = O(N-sq)
S = O(N) ( E ) O(1) ( I ) 

Woah a memory limit issue ( not a time limit issue )
How to handle the memory limit?

'''
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        targetVal = 0
        tempOneMap = self.addMerge(nums1, nums2)
        tempTwoMap = self.addMerge(nums3, nums4)
        # finalMap = self.addMerge(tempOne,tempTwo)
        # tupleCount = finalList.count(targetVal)
        tupleCount = self.mapAddMerge(tempOneMap, tempTwoMap, targetVal)
        return tupleCount

    # huh dict keyword -> no need to parameterize it much :-)

    def mapAddMerge(self, nums1: dict, nums2: dict, targetVal:int) -> int:
        targetCount = 0
        for k1, v1 in nums1.items():
            for k2, v2 in nums2.items():
                targetCount += (v1 * v2) if(k1+k2 == 0) else 0
        return targetCount

    # https://stackoverflow.com/questions/3633140/nested-for-loops-using-list-comprehension
    def addMerge(self, nums1: List[int], nums2: List[int]) -> dict():
        resDict = {}
        for a in nums1:
            for b in nums2:
                newKey = a + b
                if newKey not in resDict:
                    resDict[newKey] = 0
                resDict[newKey] += 1
        return resDict
        # return [(a+b) for a in nums1 for b in nums2]
        
