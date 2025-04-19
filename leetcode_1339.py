# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1339. Maximum Product of Splitted Binary Tree
URL := https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/

Complexity :
N = #-nodes in tree
H = height of tree : log_2(N) balanced (N) skew
Time = O(N)
Space = O(1) ( Exp ) O(H) ( Implicit ) 
'''
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.populateSums(root)
        maxVal = [0]
        totalSum = root.val
        self.getMaxSum(root, maxVal, totalSum)
        MODULO = (int)(pow(10,9) + 7)
        maxProd = maxVal[0] % MODULO
        return maxProd

    def getMaxSum(self, root, maxVal, totalSum):
        if(root.left is not None):
            self.getMaxSum(root.left,maxVal,totalSum)
        if(root.right is not None):
            self.getMaxSum(root.right, maxVal,totalSum)
        treeOne = root.val
        treeTwo = (totalSum - root.val)
        curNodeProd = (treeOne * treeTwo)
        maxVal[0] = max(maxVal[0], curNodeProd)

    def populateSums(self, root: Optional[TreeNode]) -> int:
        lstSum = 0
        rstSum = 0
        if(root.left is not None):
            lstSum = self.populateSums(root.left)
        if(root.right is not None):
            rstSum = self.populateSums(root.right)
        rootSum = lstSum + rstSum + root.val
        root.val = rootSum
        return rootSum
