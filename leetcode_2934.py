'''
2934. Minimum Operations to Maximize Last Elements in Arrays
'''
Python3 Linear Time, Const Space Solution

Hari Sridhar
100 Days Badge 2022
29
0
a few seconds ago
Python3
Array
Enumeration
Intuition and Approach
Basic enumeration and checking constraints in our loops

Complexity
N := len(input)

Time complexity:
O(N)

Space complexity:
O(1) ( Explicit and Implicit )

Code
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        maxOne = nums1[-1]
        maxTwo = nums2[-1]
        opsCaseOne = self.eval(nums1,nums2,maxOne,maxTwo)
        opsCaseTwo = 1 + self.eval(nums1,nums2,maxTwo,maxOne)
        minOps = min(opsCaseOne,opsCaseTwo)
        if(minOps == float('inf')):
            minOps = -1
        return minOps

    def eval(self, nums1: List[int], nums2:List[int], maxOne:int, maxTwo:int) -> int:
        n = len(nums1)
        minOps = 0
        for lPtr in range(n-2,-1,-1):
            rPtr = lPtr
            lVal = nums1[lPtr]
            rVal = nums2[rPtr]
            if(lVal > maxOne or rVal > maxTwo):
                if(lVal <= maxTwo and rVal <= maxOne):
                    minOps += 1
                else:
                    minOps = float('inf')
                    break
        return minOps
