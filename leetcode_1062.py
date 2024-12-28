'''
1062. Longest Repeating Substring
URL := https://leetcode.com/problems/longest-repeating-substring/

It's a Trie insertion question - or a brute force enumeration solution - in the hiding 

'''

class Node:
    # root node depth = 0 ok
    def __init__(self):
        self.letter = ''
        self.freq = 0
        self.depth = 0
        self.children = dict()

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        maxDepth = [0]
        root = Node()
        depth = 0
        for i in range(len(s)):
            self.insert(root,s,i,maxDepth, depth)
        ans = maxDepth[0]
        return ans

    # It's not frequency, it's length ( get depth of each node too ) !!!
    # the longest repeating substr
    def insert(self,root, s:str, i:int, maxDepth:List[int], depth:int) -> None:
        if(i < len(s)):
            curLetter = s[i]
            if(curLetter not in root.children):
                root.children[curLetter] = Node()
            childNode = root.children[curLetter]
            childNode.depth = depth + 1
            nextFreq = childNode.freq + 1
            childNode.freq = nextFreq
            if(nextFreq >= 2):
                maxDepth[0] = max(maxDepth[0],childNode.depth)
            self.insert(childNode,s,i+1,maxDepth, depth + 1)
        
