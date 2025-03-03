Intuition and Aproach
Leverage prefix tries and dictionaries for tries. Utilize iterative, single pointer approach to upsert - insert new Trie nodes or update existing Trie nodes. Store information in each node : current tree height, children, the array ids of a prefix, and the letter value.

Complexity
W=len(longesttoken)
M=len(arr1)
N=len(arr2)
X=MAX(M,N)

Time complexity:
O(WM)+O(WN)=O(W∗X)

Space complexity:
O(XW)

Code
'''
URL := https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/
3043. Find the Length of the Longest Common Prefix

Approach and Intuition -> prefix trie ( it's a trie ) 
Two runners - ID=1 and ID= 2 - execute to populate trie nodes

'''
class Node:
    def __init__(self):
        self.val = ""
        self.children = dict()
        self.idSet = set()

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        rootNode = Node()
        arrayIdOne = 1
        arrayIdTwo = 2
        startHeight = 1
        maxHeight = [0]
        for tokenOne in arr1:
            self.insertIntoTrie((str)(tokenOne), arrayIdOne,rootNode, startHeight, maxHeight)
        for tokenTwo in arr2:
            self.insertIntoTrie((str)(tokenTwo), arrayIdTwo,rootNode, startHeight, maxHeight)
        lcp = maxHeight[0]
        return lcp
    
    # can BFS later ( or return max height at the end )
    # Avoid recursion -> helper method -> internal only
    def insertIntoTrie(self, token: str, arrayID:int, curNode, curHeight:int, maxHeight:List[int]):
        for letter in token:
            if(letter not in curNode.children):
                createdNode = Node()
                createdNode.val = letter
                createdNode.height = curHeight
                curNode.children[letter] = createdNode
            childNode = curNode.children[letter]
            childNode.idSet.add(arrayID)
            if(len(childNode.idSet) == 2):
                maxHeight[0] = max(maxHeight[0], curHeight)
            curHeight = curHeight + 1
            curNode = childNode


        
