'''
1564. Put Boxes Into the Warehouse I
URL := https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

Complexity
Let W := #-of warehouses
T = O(WlgW)
S = O(1) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        maxBoxesInsertable = 0
        boxes.sort(key = lambda x : (-1 * x ))
        boxPtr = 0
        housePtr = 0
        while(housePtr < len(warehouse) and boxPtr < len(boxes)):
            curHouse = warehouse[housePtr]
            curBox = boxes[boxPtr]
            if(curHouse >= curBox):
                housePtr += 1
                boxPtr += 1
                maxBoxesInsertable += 1
            elif(curHouse < curBox):
                boxPtr += 1
        return maxBoxesInsertable
