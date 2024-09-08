Intution and Approach
Wait sort nonDecr order using abs values can have a negative el as a HEAD of SLL
unless that mockHEAD value is itself a mock we can use? Change that mock head later
Spli;t into two seperate SLLs
TBH, Reverse seems so much easier
Pass 1 : construct two seperate SLL
Pass 2 : rev the negative SLL
Pass 3 : connect the two SLLz

Complexity
Let N:= the number of elements in the SLL

Time complexity:
O(N)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
URL := https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/description/
2046. Sort Linked List Already Sorted Using Absolute Values
'''
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedSLL = None
        posNode = ListNode()
        negNode = ListNode()
        posHead = posNode
        negHead = negNode
        cur = head
        while(cur is not None):
            nextNode = cur.next
            if(cur.val < 0):
                negNode.next = cur
                negNode = negNode.next
            elif(cur.val >= 0):
                posNode.next = cur
                posNode = posNode.next
            cur.next = None
            cur = nextNode
        posHead = posHead.next
        negHead = negHead.next
        negRev = self.reverse(negHead)
        if(negRev is None):
            return posHead
        tailNegRev = negRev
        while(tailNegRev.next is not None):
            tailNegRev = tailNegRev.next
        tailNegRev.next = posHead
        sortedSLL = negRev
        return sortedSLL

    # do not reverse an empty list or singleton list
    # return tail of reversed node
    def reverse(self, head: Optional[ListNode]) -> ListNode:
        if(head is None or head.next is None):
            return head
        cur = head
        nxt = cur.next
        prev = None
        while(nxt is not None):
            nxtTwo = nxt.next
            cur.next = prev
            nxt.next = cur
            prev = cur
            cur = nxt
            nxt = nxtTwo
        return cur
    
