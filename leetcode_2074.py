Intuition and Approach
reverse-nodes-in-even-length-groups/description/
First group must always have an odd length : never even ( singleton el case )
Suppose we have length of a list
Disconnection is the hard part : the rest seems easy
Seperate method to easily debug reversing a SLL makes the problem easier ( avoid in-place manipulation )

Complexity
LetN:= length of the input list

Time complexity:
Time = O(N)

Space complexity:
Space = O(1) ( Explicit and Implicit )

Code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
2074. Reverse Nodes in Even Length Groups
URL := https://leetcode.com/problems
'''
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        finalHead = head
        listLen = self.getLength(head)
        step = 1
        prev = None
        while(listLen > 0 and head is not None):
            if(listLen - step >= 0):
                if(step % 2 == 0): #even case
                    self.evenGroupLogic(prev,head,step)
                    prev = head
                    head = head.next
                else:
                    for x in range(step):
                        prev = head
                        if(head is not None):
                            head = head.next
                listLen = listLen - step
                step += 1
            else:
                if(listLen % 2 == 0):
                    self.evenGroupLogic(prev,head,-1)
                head = None
        return finalHead

    # two paths : (A) the last group and (b) a legit step group
    def evenGroupLogic(self, prev:ListNode,head:ListNode, step:int) -> None:
        if(step == -1):
            prev.next = None
            revInfo = self.reverseGroup(head)
            revHead = revInfo[0]
            revTail = revInfo[1]
            prev.next = revHead
        else:
            leftPtr = head
            rightPtr = head
            # disconnect on left
            prev.next = None
            for x in range(step - 1):
                rightPtr = rightPtr.next
            # disconnect on the right
            formerRightNext = rightPtr.next
            rightPtr.next = None
            revInfo = self.reverseGroup(leftPtr)
            revHead = revInfo[0]
            revTail = revInfo[1]
            prev.next = revHead
            # get the tail of the SLL too!
            revTail.next = formerRightNext
            prev = revTail
            head = revTail.next

    # code up later ( iterative method to reverse )
    # assumes a SLL where last Node pointer equals None
    def reverseGroup(self, head:ListNode) -> List[ListNode]:
        if(head is None or head.next is None):
            return head
        prev = None
        cur = head
        nextTwo = cur.next
        while(cur is not None):
            cur.next = prev
            prev = cur
            cur = nextTwo
            if(cur is not None):
                nextTwo = cur.next
        revHead = prev
        revTail = head
        return [revHead,revTail]

    def getLength(self, head: Optional[ListNode]) -> int:
        listLen = 0
        while(head is not None):
            listLen += 1
            head = head.next
        return listLen

    
