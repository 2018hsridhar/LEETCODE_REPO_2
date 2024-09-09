Intuition and Approach :
What if list lengths were the same, but the shorter list had leading zeros as mock placeholder values
Leverage the mock zeros, and execute addition operation as is, but recursively ( from the bottom-up )
If the final carry over value > 0, add said value as a new node
Complexity
Time complexity:
Let M:=len(l1),N:=len(l2),O:=max(M,N)
Performance = O(O)

Space complexity:
Space
O(O) ( E )
O(O) ( Implicit call stack )

Code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
URL := https://leetcode.com/problems/add-two-numbers-ii/description/
445. Add Two Numbers II

'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lenOne = self.getListLength(l1)
        lenTwo = self.getListLength(l2)
        maxLen = max(lenOne,lenTwo)
        delta = abs(lenOne - lenTwo)
        # equality case : ignore code path :-)
        if(lenOne < lenTwo):
            l1 = self.populateLeadingZeros(l1,delta)
        elif(lenOne > lenTwo):
            l2 = self.populateLeadingZeros(l2,delta)
        l3 = None
        l3 = self.populateLeadingZeros(l3,maxLen)
        finalCarry = self.addNumbers(l1,l2,l3)
        targetList = l3
        if(finalCarry > 0):
            carryNode = ListNode(finalCarry)
            carryNode.next = l3
            targetList = carryNode
        return targetList

    # can modify in place why create a new list
    # well creation of new list is cleaner -> but gaaah this ain't javascript
    # return a (node,carry) operation? effort much?
    def addNumbers(self, listOne: ListNode, listTwo:ListNode, listThree: ListNode) -> int:
        carry = 0
        if(listOne.next is None and listTwo.next is None):
            sum = listOne.val + listTwo.val
            listThree.val = (sum % 10 )
            carry = floor(sum / 10)
        else:
            carryOver = self.addNumbers(listOne.next,listTwo.next, listThree.next)
            sum = listOne.val + listTwo.val + carryOver
            listThree.val = (sum % 10 )
            carry = floor(sum / 10)
        return carry

    def populateLeadingZeros(self, inputList: Optional[ListNode], steps: int) -> ListNode:
        head = inputList
        for x in range(steps):
            zeroNode = ListNode(0)
            zeroNode.next = head
            head = zeroNode
        return head

    def getListLength(self, head: Optional[ListNode]) -> int:
        listLength = 0
        while(head is not None):
            head = head.next
            listLength += 1
        return listLength
        
