# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
URL = https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/
2476. Closest Nodes Queries in a Binary Search Tree
Algo is right but TLE sadly :-(
Unsure how to do this faster if start from root node always

Complexity
Let N := #-nodes in the BST
Let H := height of the BST : log_2(N) balance and (N) skewed
Let Q := #-queries
Time = O(Q*H)
Space = O(1) ( EXP ) O(H) ( 1 ) 
'''
class Solution:

    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        sortedArr = []
        self.createSortedArr(root,sortedArr)
        closestAnswers = []
        for query in queries:
            leftVal = self.bSearchLeft(sortedArr,query)
            rightVal = self.bSearchRight(sortedArr,query)
            answers = [leftVal, rightVal]
            closestAnswers.append(answers)
        return closestAnswers

    def createSortedArr(self, root:Optional[TreeNode], sortArr:List[int]) -> None:
        if(root.left is not None):
            self.createSortedArr(root.left,sortArr)
        sortArr.append(root.val)
        if(root.right is not None):
            self.createSortedArr(root.right,sortArr)

    def bSearchLeft(self, arr:List[int], query:int) -> int:
        low = 0
        high = len(arr) - 1
        leftVal = -1
        while(low <= high):
            mid = (int)((0.5)*(low + high))
            val = arr[mid]
            if(val <= query):
                low = mid + 1
                leftVal = max(leftVal, val)
            elif(val > query):
                high = mid - 1
        return leftVal

    def bSearchRight(self, arr:List[int], query:int) -> int:
        low = 0
        high = len(arr) - 1
        rightVal = float('inf')
        while(low <= high):
            mid = (int)((0.5)*(low + high))
            val = arr[mid]
            if(val < query):
                low = mid + 1
            elif(val >= query):
                rightVal = min(rightVal,val)
                high = mid - 1
        if(rightVal == float('inf')):
            rightVal = -1
        return rightVal
