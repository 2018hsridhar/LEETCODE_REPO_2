# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
URL := https://leetcode.com/problems/serialize-and-deserialize-bst/description/
449. Serialize and Deserialize BST

Complexity :
Time = O(N)
Space = O(N) ( EXP ) O(1) ( IMP ) 
'''

import re
# res = re.split(r'[;,\s]+', s)

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        rootString = ""
        if(root is not None):
            LEFT = '('
            RIGHT = ')'
            rootString += LEFT
            rootString += (str)(root.val)
            if(root.left is not None):
                rootString += self.serialize(root.left)
            if(root.right is not None):
                rootString += self.serialize(root.right)
            rootString += RIGHT
        return rootString

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        LEFT = '('
        RIGHT = ')'
        targetRoot = None
        decodeStack = []
        pattern = r"([\(\)])"  # Matches ',', ';', or '|' and captures them
        preTokens = re.split(pattern, data)
        tokens = [x for x in preTokens if len(x) >= 1]
        for curToken in tokens:
            if(curToken == LEFT):
                decodeStack.append(TreeNode())
            elif(curToken == RIGHT):
                # always a child
                child = decodeStack.pop()
                # we end up here anyways :-)
                targetRoot = child
                if(len(decodeStack) >= 1):
                    parent = decodeStack[-1]
                    if(parent.val < child.val):
                        parent.right = child
                    elif(parent.val > child.val):
                        parent.left = child
            else:
                curNode = decodeStack[-1]
                curNode.val = (int)(curToken)
        return targetRoot

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
