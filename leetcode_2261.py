'''
2261. K Divisible Elements Subarrays
URL := https://leetcode.com/problems/k-divisible-elements-subarrays/description/

Complexity
Let N := #-elements
T = O(N^2)
S = O(N^2)

Category : String, Set, Counting, Enumeration.

Commit log : 
(A) Be careful on `NameError`
(B) Even with the temporary error creation, it seems like the `.join()` method is more Pythonic3 and more readable ( especially given the delimeter )
(C) Readability of range loops : do we need extra indexing args that are already known?
(D)

'''
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        countMetCriteria = 0
        distinctSubArrays = set()
        n = len(nums)
        subArrString = ""
        for leftPtr in range(0,len(nums),1):
            numDivElements = 0
            for rightPtr in range(leftPtr,len(nums), 1):
                if(nums[rightPtr] % p == 0):
                    numDivElements += 1
                if(numDivElements <= k):
                    # got away with pseudo delimeter at the end :-)
                    subArrString = "".join([subArrString,str(nums[rightPtr]), "-"])
                    if(subArrString not in distinctSubArrays):
                        distinctSubArrays.add(subArrString)
                        countMetCriteria += 1
                else:
                    break
            subArrString = ""
        return countMetCriteria
        
