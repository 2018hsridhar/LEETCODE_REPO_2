'''
URL := https://leetcode.com/problems/next-greater-node-in-linked-list/description/
1019. Next Greater Node In Linked List

Wait a second -> it is a stack -> but exert caution.
Store ( value, index ) -> not just the value -> index helps with future writes too!
Wait a second ... indices really needed?

15 mins to solutioning

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val += val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        listLen = self.getLength(head)
        nextLargestValues = [0 for i in range(listLen)]
        curNodalStack = []
        index = 0
        while(head != None):
            curVal = head.val
            if(len(curNodalStack) == 0):
                curNodalStack.append([curVal, index])
            else:
                while(len(curNodalStack) > 0):
                    topTuple = curNodalStack.pop()
                    topVal = topTuple[0]
                    topIdx = topTuple[1]
                    if(curVal > topVal):
                        nextLargestValues[topIdx] = curVal
                    else:
                        curNodalStack.append(topTuple)
                        break
                curNodalStack.append([curVal,index])
            head = head.next
            index = index + 1
        for noGreaterVal in curNodalStack:
            noGVal = noGreaterVal[0]
            noGIdx = noGreaterVal[1]
            nextLargestValues[noGIdx] = 0
        return nextLargestValues
        
    def getLength(self, head: Optional[ListNode]) -> int:
        curLen = 0
        while(head != None):
            curLen += 1
            head = head.next
        return curLen
