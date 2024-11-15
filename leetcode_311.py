Solution O(MN) Time and Space Leveraging Hashmaps and algebraic properties of addition

Hari Sridhar
100 Days Badge 2022
29
0
a few seconds ago
Python3
Array
Hash Table
Matrix
Intuition
Approach
Complexity
Time complexity:
Space complexity:
Code
'''
URL := https://leetcode.com/problems/sparse-matrix-multiplication/description/
311. Sparse Matrix Multiplication

'''
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        n = len(mat2[0])
        finalMat = [[0 for c in range(n)] for r in range(m)]
        repOne = self.buildRepresentation(mat1)
        repTwo = self.buildRepresentation(mat2)
        for rowOne, recordsOne in repOne.items():
            for [colOne,valOne] in recordsOne:
                if(colOne in repTwo):
                    recordsTwo = repTwo[colOne]
                    for [colTwo,valTwo] in recordsTwo:
                        delta = valOne * valTwo
                        finalMat[rowOne][colTwo] += delta
        return finalMat

    def buildRepresentation(self, mat: List[List[int]]) -> dict:
        rep = dict()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if(r not in rep):
                    rep[r] = []
                val = mat[r][c]
                record = [c,val]
                rep[r].append(record)
        return rep
        
