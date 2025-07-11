'''
URL := https://leetcode.com/problems/alien-dictionary/
269. Alien Dictionary

Conected components -> each component must be a DAG ( cycle free ) 
Any solution works ( can verify it later )
'''
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        order = ""
        if(len(words) == 0):
            order = words[0][0]
            return order
        alphabet = set()
        for word in words:
            for letter in word:
                if(letter not in alphabet):
                    alphabet.add(letter)
        sigma = len(alphabet)
        adjList = dict()
        inDeg = dict()
        for alpha in alphabet:
            adjList[alpha] = set()
            inDeg[alpha] = 0
        for index in range(len(words) - 1):
            wordOne = words[index]
            wordTwo = words[index+1]
            minLen = min(len(wordOne),len(wordTwo))
            orderBreak = False
            for pos in range(minLen):
                letOne = wordOne[pos]
                letTwo = wordTwo[pos]
                if(letOne == letTwo):
                    continue
                else:
                    orderBreak = True
                    if(letTwo not in adjList[letOne]):
                        adjList[letOne].add(letTwo)
                        inDeg[letTwo] += 1
                        break
                    else:
                        break
            if(orderBreak == False and len(wordOne) > len(wordTwo)):
                return ""
        # for each component ( inDegree = 0 )
        # do an exploration
        # verify all alphabet letters are hit at the end
        visitedCount = 0
        visited = set()
        # Are we double couting here ( exert caution )
        # only nodes initially with inDeg = 0
        frontier = set()
        for node, inCount in inDeg.items():
            if(inCount == 0):
                frontier.add(node)
        for node in frontier:
            queue = [node]
            while(len(queue) > 0):
                parent = queue[0]
                del queue[0]
                order += parent
                # be careful with ordering here!!!
                visited.add(parent)
                children = adjList[parent]
                for child in children:
                    inDeg[child] -= 1
                    if(inDeg[child] == 0):
                        queue.append(child)
        visitedCount = len(visited)
        if(visitedCount != sigma):
            order = ""
        return order
        
