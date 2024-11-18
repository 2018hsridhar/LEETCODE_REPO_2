Union Find Approach Set Membership of Similar Pairs and Then Zip through both sentences

Hari Sridhar
100 Days Badge 2022
29
0
a minute ago
Python3
Array
Hash Table
String
3+
Intuition
Approach
Complexity
Time complexity:
Space complexity:
Code
'''
737. Sentence Similarity II
URL := https://leetcode.com/problems/sentence-similarity-ii/description/

Similarity scoring : words x_i, y_i
Similarity criteria : 
a. Same length : # of tokens
b. Similarity criteria meets 
Words always self similar
Similarity is a transitive property

Complexity
A := #-tokens ( S1 ) 
B := #-tokens ( S2 ) 
T = O(A)
S = O(A+B) ( E ) O(1) ( I ) 

Seems DFS/BFS esque -> or union find -> update HM keys ( 2K max of keys ) 
'''
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        similarStatus = True
        pairId = dict()
        uuid = 0
        # almost works, but gaaah set membership testing SMH
        # Closer, but might be missing out elsewhere
        # SMh union find
        for [src,dst] in similarPairs:
            if(src not in pairId and dst not in pairId):
                pairId[src] = uuid
                pairId[dst] = uuid
                uuid += 1
            elif(src in pairId and dst not in pairId):
                pairId[dst] = pairId[src]
            elif(src not in pairId and dst in pairId):
                pairId[src] = pairId[dst]
            else:
                srcVal = pairId[src]
                dstVal = pairId[dst]
                for k, v in pairId.items():
                    if(v == srcVal):
                        pairId[k] = dstVal
        if(len(sentence1) == len(sentence2)):
            for first,second in zip(sentence1,sentence2):
                if(first != second):
                    if(first not in pairId or second not in pairId):
                        similarStatus = False
                        break
                    idOne = pairId[first]
                    idTwo = pairId[second]
                    if(idOne != idTwo):
                        similarStatus = False
                        break
        else:
            similarStatus = False
        return similarStatus
