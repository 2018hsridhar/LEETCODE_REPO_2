# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
URL := https://leetcode.com/problems/add-two-numbers-ii/
445. Add Two Numbers II

Idea : prefix add <0> nodes to the front of the smaller list
Recursively compute node values
and if a carry is left at the end -> go append a final node

Complexity
Let N := #-nodes in our SLL
T = O(N)
S = O(N) ( E ) O(1) ( I ) 

return types : < int, ListNode > -> how to return both as a package though?
Get to thsi problem later and please just go to sleep now hari :-) 
'''


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m = self.getSize(l1)
        n = self.getSize(l2)
        delta = abs(m - n)
        if(m < n):
            # name is not defined error
            self.appendZeroPrefix(l1,delta)
        else:
            self.appendZeroPrefix(l2,delta)
        # Create an empty list ( L3 ) -> hey it's all zero-ed out here
        iCurr = ListNode(0)
        for i in range(m-1):
            iNext = ListNode(0)
            iCurr.next = iNext
            iCurr = iNext
        lastFwdCarry = self.recurseCompute(l1,l2,iCurr)
        iFinal = iCurr
        if(lastFwdCarry > 0):
            iFinal = ListNode(0)
            iFinal.next = iCurr
        return iFinal

    # Optional[Type] based system in parameter passing.
    def recurseCompute(self, l1: Optional[ListNode], l2: Optional[ListNode], lTerm: Optional[ListNode]) -> int:
        fwdCarry = 0
        if(l1 != None and l2 != None and l1.next != None and l2.next != None):
            fwdCarry = self.recurseCompute(l1.next,l2.next, lTerm.next)
        curSum = l1.val + l2.val + fwdCarry
        if(curSum >= 10):
            curSum %= 10
            fwdCarry = curSum / 10
        lTerm.val = curSum
        return fwdCarry
    
    def appendZeroPrefix(self, mySLL: Optional[ListNode], delta: int) -> None:
        curr = ListNode(0)
        firstNode = curr
        for i in range(delta):
            next = ListNode(0)
            curr.next = next
        curr.next = mySLL
        return firstNode

# no use of `new` keyword in python weirdly
    def getSize(self, l1: Optional[ListNode]) -> int:
        listSize = 0
        while l1 != None:
            listSize += 1
            l1 = l1.next
        return listSize
        




        
