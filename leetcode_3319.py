# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
URL := https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/description/
3319. K-th Largest Perfect Subtree Size in Binary Tree

Categories : Recursion, DP, BFS, DFS, Counting & Enumeration

Let N := #-nodes in the binary tree
Let H := height of the binary tree : log2(N) average (N) worst case
Time = O(N)
Space = O(N) ( E ) O(H ) ( I ) 

PBT := perfect binary subtree
2K nodes max decent constraints to the problem @ hand
Have to get everyone's sizes

15 mins to solutioning
'''
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        kthSize = -1
        candidates = []
        self.dfs(root,candidates)
        # sort non-decreasing order
        candidates.sort(key = lambda x : -1 * x)
        print(candidates)
        if(k-1 < len(candidates)):
            kthSize = candidates[k-1]
        return kthSize

    # return : size of tree, and max level of a leaf, and if it is a perfect tree : 0 = no, 1 = yes
    def dfs(self,root:TreeNode,candidates:List[int]) -> List[int]:
        # base case : leaf condition
        targetRecord = [0,0,0]
        if(root is None):
            return targetRecord
        treeSize = 1
        if(root.left is None and root.right is None):
            candidates.append(1)
            return [1,1,1]
        elif(root.left is not None and root.right is not None):
            recordLeft = self.dfs(root.left,candidates)
            recordRight = self.dfs(root.right,candidates)
            # both are perfect binary subtrees
            targetRecord = [0,0,0]
            if(recordLeft[2] == 1 and recordRight[2] == 1):
                leafDepthLeft = recordLeft[1]
                leafDepthRight = recordRight[1]
                if(leafDepthLeft == leafDepthRight):
                    treeSize = recordLeft[0] + recordRight[0] + 1
                    candidates.append(treeSize)
                    targetRecord = [treeSize,1 + leafDepthLeft,1]
        else: # single child case : no validity ( perfection ) going upwards too
            # no validity upwards too :-(
            recordLeft = self.dfs(root.left,candidates)
            recordRight = self.dfs(root.right,candidates)
        return targetRecord


    


        
