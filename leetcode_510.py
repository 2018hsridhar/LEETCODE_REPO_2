"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
'''
510. Inorder Successor in BST II
https://leetcode.com/problems/inorder-successor-in-bst-ii/description/

Rules Engine in the hiding
In-order : left -> root -> right
if there's a root -> bias to the root
if there's no root -> keep going up ( until you hit a value > you )
if you the root -> go right
'''
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        answer = None
        if(node.right is not None):
            answer = self.inorder_dfs(node.right)
        elif(node.right is None):
            curNode = node
            while(curNode is not None):
                curNode = curNode.parent
                if(curNode is not None and curNode.val > node.val):
                    break
            answer = curNode
        return answer
        
    def inorder_dfs(self, node:'Node') -> 'Optional[Node]':
        curNode = node
        while(True):
            if(curNode.left is not None):
                curNode = curNode.left
            else:
                break
        return curNode
                




