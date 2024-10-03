'''
URL := https://leetcode.com/problems/implement-trie-ii-prefix-tree/description/
1804. Implement Trie II (Prefix Tree)
'''

class Node :

    def __init__(self):
        self.val = 0
        self.children = dict()
        self.wordCount = 0
        self.prefixCount = 0

    def __init__(self, val, children, wordCount, prefixCount):
        self.val = val
        self.children = children
        self.wordCount = wordCount
        self.prefixCount = prefixCount

class Trie:

    def __init__(self):
        children = dict()
        rootVal = ""
        self.root = Node(rootVal,children,0,0)

    def insert(self, word: str) -> None:
        # can't DFS on the insert ( gaaah )
        curPtr = self.root
        for letter in word:
            frontier = curPtr.children
            if(letter not in frontier):
                childNode = Node(letter, dict(),0,0)
                frontier[letter] = childNode
            child = frontier[letter]
            child.prefixCount += 1
            curPtr = child
        # last ptr : set frequency up
        curPtr.wordCount += 1

    # modularize a DFS elsewhere here :-) 
    def dfs(self, word:str) -> [Node,bool]:
        hitNode = True
        curPtr = self.root
        for letter in word:
            frontier = curPtr.children
            if(letter not in frontier):
                hitNode = False
                break
            child = frontier[letter]
            curPtr = child
        result = [curPtr,hitNode]
        return result

    def countWordsEqualTo(self, word: str) -> int:
        wordCount = 0
        [targetNode,hitWord] = self.dfs(word)
        if(hitWord):
            wordCount = targetNode.wordCount
        return wordCount

    def countWordsStartingWith(self, prefix: str) -> int:
        prefixCount = 0
        [target,hitPrefix] = self.dfs(prefix)
        if(hitPrefix):
            prefixCount = target.prefixCount
        return prefixCount

    # presuming the word is in the trie ( we should check this ) 
    # careful when it comes to counting though : remove last word
    def erase(self, word: str) -> None:
        [targetNode,haveTarget] = self.dfs(word)
        if(haveTarget):
            # can do erasure
            # erase if node value = 0 ( anywhere on the path ) 
            # if top is 0, the rest fall like dominos
            curPtr = self.root
            frontier = None
            for letter in word:
                frontier = curPtr.children
                child = frontier[letter]
                child.prefixCount -= 1
                if(child.prefixCount == 0):
                    del frontier[letter]
                    return
                curPtr = child
            # hit the last pointer ( not a root node case )
            # root node as "guardian" sentinel node
            if(curPtr.val != "" and frontier is not None):
                curPtr.wordCount -= 1
                curLetter = curPtr.val
                if(curPtr.wordCount == 0 and curPtr.prefixCount == 0):
                    del frontier[curLetter]

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
