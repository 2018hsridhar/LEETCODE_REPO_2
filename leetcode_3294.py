Intuition and Approach :
Two Pointers, Linear Scan, Arrays
Leverage pythonic slice concatenation to return target result

Approach
Complexity
N:=length(inputlist)

Time complexity:
O(N)

Space complexity:
O(N)(E)O(1)(I)

Code
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
'''
URL := https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/description/
3294. Convert Doubly Linked List to Array II
'''
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        prevPtr = node.prev
        nextPtr = node.next
        suffix = []
        prefix = []
        while(nextPtr is not None):
            suffix.append(nextPtr.val)
            nextPtr = nextPtr.next
        while(prevPtr is not None):
            prefix.append(prevPtr.val)
            prevPtr = prevPtr.prev
        prefix.reverse()
        arrayForm = prefix + [node.val] + suffix
        return arrayForm
        
