'''
3397. Maximum Number of Distinct Elements After Operations
URL := https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/description/

Complexity
N = len(input)
T O(NlgN)
S O(1) ( Explicit )
S O(1) ( Implicit ) 
'''
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        maxNumDistinct = 0
        nums.sort()
        idealMin = nums[0] - k
        for num in nums:
            if(num - k <= idealMin and idealMin <= num + k):
                idealMin = idealMin + 1
                maxNumDistinct += 1
            elif(idealMin < num - k) :
                # ahhh collision case
                idealMin = num - k + 1
                maxNumDistinct += 1
        return maxNumDistinct

        
