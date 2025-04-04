# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
919. Complete Binary Tree Inserter
URL := https://leetcode.com/problems/complete-binary-tree-inserter/description/

Binary tree completenes - each level filled ( and nodes as left as possible ) 
1K nodes, reaosnable values, invariant of root = CBT, pow(10,4) calls max

Ahhh - > so get to the correct node ( it's not from start here )

'''
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.LOT = [root]
        lotQueue = []
        if(root.left is not None):
            lotQueue.append(root.left)
        if(root.right is not None):
            lotQueue.append(root.right)
        root.left = None
        root.right = None
        # SMH workaround -> use own insetion method 
        while(len(lotQueue) > 0):
            curNode = lotQueue[0]
            self.insert(curNode.val)
            del lotQueue[0]
            if(curNode.left is not None):
                lotQueue.append(curNode.left)
            if(curNode.right is not None):
                lotQueue.append(curNode.right)

    def insert(self, val: int) -> int:
        # EMP : safety/guardian code blocks
        mostRecentNode = None
        insertNode = TreeNode(val)
        while(len(self.LOT) > 0):
            mostRecentNode = self.LOT[0]
            if(mostRecentNode.left is not None and mostRecentNode.right is not None):
                del self.LOT[0]
            else:
                break
        if(mostRecentNode is not None):
            if(mostRecentNode.right is None):
                # a. insert to Left
                if(mostRecentNode.left is None):
                    mostRecentNode.left = insertNode
                # b. insert to Right
                else:
                    mostRecentNode.right = insertNode
        self.LOT.append(insertNode)
        parentVal =  mostRecentNode.val
        return parentVal

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
