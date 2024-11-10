Combine normal dfs/bfs with level order traversal and hashmaps :-)

Hari Sridhar
100 Days Badge 2022
29
0
a few seconds ago
Python3
Hash Table
Tree
Depth-First Search
3+
Intuition
Approach
Complexity
N := #-nodes in the tree
H := height of the tree

Time complexity:
O(N)

Space complexity:
O(N)(E)O(H)(I)

Code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
314. Binary Tree Vertical Order Traversal

'''
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeToCol = dict()
        levels = dict()
        startCol = 0
        self.dfsTraverse(nodeToCol,root,startCol,levels)
        targetTraversal = self.levelOrderTraverse(nodeToCol,levels,root)
        return targetTraversal

    def levelOrderTraverse(self, nodeToCol:dict, levels:dict, root:TreeNode) -> List[List[int]]:
        if(root is None):
            return []
        targetTraversal = []
        queue = [root]
        minLevel = float('inf')
        maxLevel = float('-inf')
        while(len(queue) > 0):
            curNode = queue.pop(0)
            nodeCol = nodeToCol[curNode]
            minLevel = min(minLevel,nodeCol)
            maxLevel = max(maxLevel,nodeCol)
            levels[nodeCol].append(curNode.val)
            if(curNode.left is not None):
                queue.append(curNode.left)
            if(curNode.right is not None):
                queue.append(curNode.right)
        targetTraversal = []           
        for level in range(minLevel,maxLevel+1,1):
            targetLevel = levels[level]
            targetTraversal.append(targetLevel)
        return targetTraversal



    def dfsTraverse(self, nodeMap:dict(), root:TreeNode, col:int,levels:dict()) -> None:
        if(root is None):
            return
        # always create empty set here :-)
        levels[col] = []
        nodeMap[root] = col
        if(root.left is not None):
            self.dfsTraverse(nodeMap,root.left,col-1,levels)
        if(root.right is not None):
            self.dfsTraverse(nodeMap,root.right,col+1,levels)
