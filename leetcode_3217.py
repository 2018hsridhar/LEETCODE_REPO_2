Intuition & Approach
Conversion to a set later
Leverage usage of a sentinel node

Complexity
Let H:= number of elements in the SLL
Let N:= number of unique els in nums

Time complexity:
O(N)+O(H)

Space complexity:
O(H) ( EXP )
O(1) ( IMP ) ( Iterative only )

Code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
3217. Delete Nodes From Linked List Present in Array
URL := https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/

'''
class Solution:
    # Nodal disconnection is the harer part
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        uniqNums = set(nums)
        mockHead = ListNode()
        actualHead = mockHead
        cur = head
        prev = None
        while(cur is not None):
            prev = cur
            if(cur.val in uniqNums):
                cur = cur.next
                prev.next = None
            else:
                mockHead.next = cur
                cur = cur.next
                mockHead = mockHead.next
                prev.next = None
        actualHead = actualHead.next
        return actualHead
