# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
2816. Double a Number Represented as a Linked List
URL := https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/

Double operation -> can have  carry in range of [0,9] but not larger ( 9*9 = 81 c 8, 8*8 = )
Huh for addition and multiplication, carry value persists an upper bound.

Complexity
Let N := #-nodes in the SLL
TIME := O(N)
SPACE := O(1) ( E ) O(1) ( I ) -> bruh can we do this in place TBH?

99999 -> max bounded anyways
81 + 8 = 89 carry 8 type of deal going on here
Doubling -> carry one max too

Guarantee one node prefix full SLL, at least.
'''
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = self.doubleExec(head)
        # which faster : != or the > comparison?
        if(carry != 0):
            # new keyword even here?
            newHead = ListNode(carry, head)
            head = newHead
        return head

    def doubleExec(self, head: Optional[ListNode]) -> int:
        if(head == None):
            return 0
        carryCurStep = 0
        # minimize volume of multiple branching instructions in code.
        if(head.next != None):
            carryCurStep = self.doubleExec(head.next)
        head.val = (head.val * 2) + carryCurStep
        carryNextStep = int(head.val / 10)
        head.val = int(head.val % 10)
        return carryNextStep
