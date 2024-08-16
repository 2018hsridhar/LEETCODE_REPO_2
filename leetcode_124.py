# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solved already, but willing to solution yet again :-)
# URL := https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# 124. Binary Tree Maximum Path Sum
# Category : greedy, recursion
# Thougth you had to go traverse down to the leaf : I guess not?
class Solution:

    # Such a good built-in : why not default provisioned in the classes?
    def __init__(self):
        self.globalMax = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.internalHelper(root)
        return self.globalMax

    # root-left-right : is a stopping condition
    # think inductively
    def internalHelper(self, root: TreeNode) -> [int,int]:
        # leaf case ( as the base case )
        bestVal = []
        if(root.left is None and root.right is None):
            self.globalMax = max(self.globalMax, root.val)
            bestVal = root.val
        # SLL cases : have to go with that sum
        elif(root.left is not None and root.right is None):
            leftVal = root.val + self.internalHelper(root.left)        
            rightVal = root.val
            bestVal = max(leftVal,rightVal)
            self.globalMax = max(self.globalMax, bestVal)
        elif(root.left is None and root.right is not None):
            leftVal = root.val
            rightVal = root.val + self.internalHelper(root.right)
            bestVal = max(leftVal,rightVal)
            self.globalMax = max(self.globalMax, bestVal)
        # alternations
        elif(root.left is not None and root.right is not None):
            leftVal = self.internalHelper(root.left)        
            rightVal = self.internalHelper(root.right)
            pathRoot = root.val
            pathRootLeft = root.val + leftVal
            pathRootRight = root.val + rightVal
            pathRootLeftRight = root.val + leftVal + rightVal
            bestVal = max(pathRoot, max(pathRootLeft,pathRootRight))
            self.globalMax = max(self.globalMax, max(pathRootLeftRight, bestVal))
        return bestVal
