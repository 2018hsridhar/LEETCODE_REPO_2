# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
2792. Count Nodes That Are Great Enough
URL := https://leetcode.com/problems/count-nodes-that-are-great-enough/

Complexity
N = #-nodes
H = height tree
T = O(NK)
S = O(K) ( Exp ) O(1) ( Imp ) 

'''
class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        countNodes = [0]
        _ = self.dfs(root,k, countNodes)
        numNodes = countNodes[0]
        return numNodes

    # Return minimum lists as we go up!
    def dfs(self, root: Optional[TreeNode], k:int, nodeCount:List[int]) -> List[int]:
        kLeft = []
        kRight = []
        if(root.left is not None):
            kLeft = self.dfs(root.left,k,nodeCount)
        if(root.right is not None):
            kRight = self.dfs(root.right,k,nodeCount)
        ptrOne = 0
        ptrTwo = 0
        kUpper = []
        # it's a zipper merge
        while(ptrOne < len(kLeft) and ptrTwo < len(kRight)):
            valOne = kLeft[ptrOne]
            valTwo = kRight[ptrTwo]
            if(valOne < valTwo):
                kUpper.append(valOne)
                ptrOne += 1
            else:
                kUpper.append(valTwo)
                ptrTwo += 1
        while(ptrOne < len(kLeft)):
            valOne = kLeft[ptrOne]
            kUpper.append(valOne)
            ptrOne += 1
        while(ptrTwo < len(kRight)):
            valTwo = kRight[ptrTwo]
            kUpper.append(valTwo)
            ptrTwo += 1
        kUpper = kUpper[0:k]
        if(len(kUpper) == k):
            maxVal = kUpper[-1]
            if(root.val > maxVal):
                nodeCount[0] += 1
        kUpper.append(root.val)
        kUpper.sort()
        return kUpper





        
