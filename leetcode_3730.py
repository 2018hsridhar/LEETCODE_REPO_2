'''
3730. Maximum Calories Burnt from Jumps
URL := https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

Complexity
Let H := len(heights) : #-routine blocks
Time = O(HlgH)
Space = O(1) ( E ) O(1) ( I ) 

[1,7,9]
0->9->1->7->DONE
[2,4,5] 
0->5->2->4 ( DONE ) 
'''
import math

class Solution:
    def maxCaloriesBurnt(self, heights: List[int]) -> int:
        heights.sort()
        myCaloriesBurnt = prev = cur = 0
        jumpUp = True
        leftPtr = 0
        rightPtr = len(heights) - 1
        while leftPtr <= rightPtr:
            cur = heights[rightPtr] if jumpUp else heights[leftPtr]
            if(jumpUp):
                rightPtr -= 1
            else:
                cur = heights[leftPtr]
                leftPtr += 1
            diff = cur - prev
            delta = diff * diff
            myCaloriesBurnt += delta
            prev = cur
            jumpUp = not jumpUp
        return (int)(myCaloriesBurnt)
        
