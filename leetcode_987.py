# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
987. Vertical Order Traversal of a Binary Tree
URL := https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

Categories : Map, DFS/BFS, Recursion, Top-Down
N = #-nodes
H = tree height ( balanced = log_2, skewed = n )
T = O(N)
S = O(1) ( Imp ) ( if not recursive ) O(N) ( Exp ) ( map ) 
'''
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        row = 0
        col = 0
        vertMap = dict()
        self.dfs(root,row,col,vertMap)
        traversal = []
        for col in sorted(vertMap.keys()):
            records = vertMap[col]
            records.sort(key = lambda x : (x[0],x[1]))
            column = [x[1] for x in records]
            traversal.append(column)
        return traversal

    def dfs(self, root,row,col,vertMap) -> None:
        if(col not in vertMap):
            vertMap[col] = list()
        record = [row,root.val]
        vertMap[col].append(record)
        nextRow = row + 1
        leftCol = col - 1
        rightCol = col + 1
        if(root.left is not None):
            self.dfs(root.left,nextRow,leftCol,vertMap)
        if(root.right is not None):
            self.dfs(root.right,nextRow,rightCol,vertMap)
