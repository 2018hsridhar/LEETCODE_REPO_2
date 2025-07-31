# Definition for BigArray.
# class BigArray:
#     def at(self, index: long) -> int:
#         pass
#     def size(self) -> long:
#         pass
'''
2936. Number of Equal Numbers Blocks
URL := https://leetcode.com/problems/number-of-equal-numbers-blocks/description/

N = #-elements in big array
T = O(lgN)
S = O(1) ( E ) O(H) ( IMplicit ) 
H = log2(N)

'''
class Solution(object):
    def countBlocks(self, nums: Optional['BigArray']) -> int:
        low = 0
        high = nums.size() - 1
        totalLen = nums.size()
        blockCount = self.helper(nums,low,high,totalLen)
        return blockCount

    # Closing in ( an adjust needed ) 
    def helper(self, nums: Optional['BigArray'], low:int, high:int, totalLen:int) -> int:
        blockCount = 0
        if(low >= 0 and high < totalLen and low <= high):
            lowVal = nums.at(low)
            highVal = nums.at(high)
            if(lowVal == highVal):
                blockCount = 1
            elif(lowVal != highVal):
                mid = (int)((low + high)/2.0)
                blockCount += self.helper(nums,low,mid,totalLen)
                blockCount += self.helper(nums,mid+1,high,totalLen)
                if(mid + 1 <= high):
                    midLeft = nums.at(mid)
                    midRight = nums.at(mid + 1)
                    if(midLeft == midRight):
                        blockCount -= 1
        else:
            return 0
        return blockCount



        
