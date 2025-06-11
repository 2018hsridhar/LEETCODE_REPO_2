# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
URL := https://leetcode.com/problems/two-sum-bsts/description/
1214. Two Sum BSTs
'''
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        statusOne = self.exploreNodes(root1,root2,target)
        statusTwo = self.exploreNodes(root2,root1,target)
        finalStatus = (statusOne or statusTwo)
        return finalStatus        

    def exploreNodes(self, parent,root,target):
        foundTwoSum = False
        targetDelta = target - parent.val
        if(self.dfs(root,targetDelta)):
            foundTwoSum = True
        else:
            if(parent.left is not None):
                foundTwoSum = foundTwoSum or self.exploreNodes(parent.left,root,target)
            if(parent.right is not None):
                foundTwoSum = foundTwoSum or self.exploreNodes(parent.right,root,target)
        return foundTwoSum

    def dfs(self,root,target):
        foundStatus = False
        if(root is not None):
            if(root.val == target):
                foundStatus = True
            else:
                if(root.left is not None):
                    foundStatus = foundStatus or self.dfs(root.left,target)
                if(root.right is not None):
                    foundStatus = foundStatus or self.dfs(root.right,target)
        return foundStatus
