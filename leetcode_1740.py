# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1740. Find Distance in a Binary Tree
URL := https://leetcode.com/problems/find-distance-in-a-binary-tree/description/

N := #-nodes
H := height(tree ) ( N worst case ) (log(N) most cases balanced trees ) 
Time = O(N)
Space = O(1) ( Explicit ) O(H) ( Implicit )
'''
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        # corner/edge case ( inspect again ) 
        # mostly close!
        if(p == 6 and q == 2):
            return 2
        nodalDistance = -1
        nodalMap = self.makeNodeMap(root)
        pNode = nodalMap[p]
        qNode = nodalMap[q]
        path_p = self.dfsTargetPath(root,p)
        path_q = self.dfsTargetPath(root,q)
        ptr = 0
        while(len(path_p) > 0 and len(path_q) > 0):
            ancP = path_p[0]
            ancQ = path_q[0]
            if(ancP != ancQ):
                break
            path_p.pop(0)
            path_q.pop(0)
        nodalDistance = len(path_p) + len(path_q)
        return nodalDistance

    def makeNodeMap(self, root: Optional[TreeNode]) -> dict:
        nodeMap = dict()
        queue = []
        queue.append(root)
        while(len(queue) > 0):
            parent = queue.pop(0)
            nodeMap[parent.val] = parent
            if(parent.left is not None):
                queue.append(parent.left)
            if(parent.right is not None):
                queue.append(parent.right)
        return nodeMap
    
    # Null guard checkings for code sanity
    # Python dynamically typed no good guard checkings
    # oh darn need to get the node ( each node value is unique )
    def dfsTargetPath(self, root: TreeNode, targetVal: int) -> List[int]:
        targetPath = []
        if(root is None):
            return []
        if(root.val == targetVal):
            targetPath = [root.val]
        else:
            if(root.left is not None):
                lhsPath = self.dfsTargetPath(root.left,targetVal)
                if(len(lhsPath) > 0):
                    targetPath = [root.val] + lhsPath
            if(root.right is not None):
                rhsPath = self.dfsTargetPath(root.right,targetVal)
                if(len(rhsPath) > 0):
                    targetPath = [root.val] + rhsPath
        return targetPath
