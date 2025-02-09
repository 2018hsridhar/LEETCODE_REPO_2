# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1602. Find Nearest Right Node in Binary Tree
URL := https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/description/

Complexity
N := #-nodes
T = O(N)
S = O(N) ( Exp ) O(1) ( Imp ) 

Categories : Tree, Recursion, Level Order Traversal, Records
No need for caching/precomputation here
'''
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        lot = []
        startLevel = 0
        rootRecord = [root,startLevel]
        lot.append(rootRecord)
        # woooh 'None' over 'null' syntax in Python3 :-) !!!
        nearestRight = None
        while(len(lot) > 0):
            curRecord = lot[0]
            curNode = curRecord[0]
            curLevel = curRecord[1]
            nextLevel = curLevel + 1
            del lot[0]
            # meaning we have a node to the right
            if(len(lot) >= 1):
                rightCandid = lot[0]
                rightNode = rightCandid[0]
                rightLevel = rightCandid[1]
                if(curNode == u):
                    if(rightLevel == curLevel):
                        nearestRight = rightNode
                    # None as default value
                    break
            if(curNode.left is not None):
                leftRecord = [curNode.left,nextLevel]
                lot.append(leftRecord)
            if(curNode.right is not None):
                rightRecord = [curNode.right,nextLevel]
                lot.append(rightRecord)
        return nearestRight
