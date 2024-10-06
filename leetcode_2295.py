Intuition and Approach
See title

Complexity
Let O := operations
Let V := #-values to store

Time complexity:
O(O)

Space complexity:
O(V) ( Explicit )
O(1) ( Implicit )

Code
'''
'''

class Node :

    def __init__(self,val,nextNode):
        self.val = val
        self.next = nextNode

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexMap = dict()
        for index,num in enumerate(nums):
            newNode = Node(index,None)
            if(num not in indexMap):
                # not in tail map as well
                indexMap[num] = newNode
            else:
                curList = indexMap[num]
        # dst will not exist in nums ( take note ) 
        # src will exist for sure!
        for [src,dst] in operations:
            indexListSrc = indexMap[src]
            indexMap[dst] = indexListSrc
            del indexMap[src]

        finalArr = [-1 for idx in range(len(nums))]
        for writeVal,writeIndexList in indexMap.items():
            nodePtr = writeIndexList
            while(nodePtr != None):
                writeIdx = nodePtr.val
                finalArr[writeIdx] = writeVal
                nodePtr = nodePtr.next

        return finalArr            


        
