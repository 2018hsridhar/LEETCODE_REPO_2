'''
URL = https://leetcode.com/problems/synonymous-sentences/
1258. Synonymous Sentences

Complexity ( not intuitive ) 
Let N := len(tokens) in text.
Let F := frequency of synonyms in the input string.
Let P := #-synonym pairings.

Problem consraints are very tiny ( 10 synonyms at worst )
Can leverage hashmaps and call it a day
A good TC can get away with leveraging inefficient algorithms for small constraint scenarios.
'''


# not that many synonyms TBH
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        sentences = []
        adjList = self.makeAdjList(synonyms)
        visited = set()
        groupMap = dict()
        for [src,dst] in synonyms:
            # pass by value ( or by reference )? please check
            orderList = []
            if(src not in visited):
                self.dfs(visited, src,adjList,orderList, groupMap)
            orderList.sort()

            secondOrderList = []
            if(dst not in visited):
                self.dfs(visited, dst,adjList,orderList, groupMap)
            secondOrderList.sort()
        # print(groupMap)
        # sorted lexicographically ( generate as we go )
        DELIM = " "
        tokens = text.split(DELIM)
        ptr = 0
        childTokens = []
        self.genSentences(tokens, ptr, groupMap,sentences,childTokens)
        return sentences

    def genSentences(self, tokens, ptr, groupMap,sentences,childTokens):
        SPACE = " "
        n = len(tokens)
        childPtr = ptr + 1
        if(ptr < n):
            curToken = tokens[ptr]
            if(curToken in groupMap):
                syns = groupMap[curToken]
                for syn in syns:
                    copyList = []
                    for cToken in childTokens:
                        copyList.append(cToken)
                    copyList.append(syn)
                    self.genSentences(tokens,childPtr, groupMap,sentences,copyList)
            else:
                childTokens.append(curToken)
                self.genSentences(tokens,childPtr, groupMap,sentences,childTokens)
        elif(ptr == n):
            childSent = SPACE.join(childTokens)
            sentences.append(childSent)



    def dfs(self, visited:set, src:str, adjList:dict, orderList:List[str], groupMap:dict):
        children = adjList[src]
        orderList.append(src)
        groupMap[src] = orderList
        visited.add(src)
        for child in children:
            if(child not in visited):
                self.dfs(visited,child,adjList,orderList,groupMap)

    def makeAdjList(self, synonyms: List[List[str]]) -> dict:
        adjList = dict()
        for [src,dst] in synonyms:
            if(src not in adjList):
                adjList[src] = set()
            if(dst not in adjList):
                adjList[dst] = set()
            adjList[src].add(dst)
            adjList[dst].add(src)
        return adjList

