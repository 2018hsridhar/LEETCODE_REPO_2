'''
2924. Find Champion II
URL := https://leetcode.com/problems/find-champion-ii/description/

Category : DAG, Graph Theory, Enumeration, Counting

Complexity :
Let V := #-verts, E := #-edges
Time := O(E)
Space := O(V) ( EXP ) O(1) ( IMP ) 

Solutioning : 20 minutes
'''
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        countInDeg = dict()
        for i in range(0,n,1):
            countInDeg[i] = 0
        for [src,dst] in edges:
            countInDeg[dst] += 1
        # for key, val in countInDeg:
        # https://realpython.com/iterate-through-dictionary-python/#using-built-in-functions-to-implicitly-iterate-through-dictionaries
        # filter() function - dodge conditionals and loops. Generalize the more functions.
        # print(countInDeg)
        # function callable and iteratable ( list ) 
        # filteredItr = filter(self.meetsInDegZero,countInDeg)
        # <class 'int'>
        filteredItr = filter(lambda x: x[1] == 0,countInDeg.items())
        # list from filtered object
        zeroInDeg = list(filteredItr)
        return zeroInDeg[0][0] if (len(zeroInDeg) == 1) else -1

    # Filter expression bool eval driven
    # def meetsInDegZero(self, kvPair:List[int]) -> bool:
        # return (kvPair[1] == 0)
        
