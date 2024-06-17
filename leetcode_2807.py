# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
URL := https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
2807. Insert Greatest Common Divisors in Linked List

Easy problem ( not really a medium ) 

Constraints -> minimal #-nodes in SLL and node vals all positive(Z) only
'''
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        while(curNode.next != None):
            nextNode = curNode.next
            gcdNode = ListNode((int)(math.gcd(curNode.val, nextNode.val)),nextNode)
            curNode.next = gcdNode
            curNode = nextNode
        return head

        
