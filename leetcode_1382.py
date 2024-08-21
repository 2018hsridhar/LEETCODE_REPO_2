# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/balance-a-binary-search-tree/description/
# 1382. Balance a Binary Search Tree
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        treeVals = self.getTreeVals(root)
        low = 0
        high = len(treeVals) - 1
        bstRoot = self.getBST(treeVals,low,high)
        return bstRoot

    # len = 5 : l = 0, h = 4, mid = 2
    # len = 6 : l = 0, h = 5, mid = 2 ( 0..1 and 3..5 : 2 and 3 nodes )
    def getBST(self, treeVals:List[int], low:int, high:int) -> TreeNode:
        parent = TreeNode()
        if(low == high):
            parent.val = treeVals[low]
        elif(low > high):
            parent = None
        elif(low < high):
            mid = math.floor((low + high ) / 2)
            parent.val = treeVals[mid]
            parent.left = self.getBST(treeVals,low,mid-1)
            parent.right = self.getBST(treeVals,mid+1,high)
        return parent
        
    def getTreeVals(self, root:TreeNode) -> List[int]:
        stack = []
        treeVals = []
        stack.append(root)
        while(len(stack) > 0):
            parNode = stack.pop()
            treeVals.append(parNode.val)
            if(parNode.left is not None):
                stack.append(parNode.left)
            if(parNode.right is not None):
                stack.append(parNode.right)
        treeVals.sort()
        return treeVals
