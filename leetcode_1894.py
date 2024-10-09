Intuition and Approach
The problem strikes me as a modular arithmetic problem ( avoid repeat iterations/cycles in input processing )
Categories : Counting, Summations, Modular Arithmetic

Complexity
Let N:=length(input)

Time complexity:
O(N)

Space complexity:
O(1) ( Explicit and Implicit )

Code
'''
URL := https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/
1894. Find the Student that Will Replace the Chalk

'''
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        indexReplacer = -1
        chalkSum = sum(chalk)
        rem = (k % chalkSum)
        k = rem
        n = len(chalk)
        for studentIndex, chalkVal  in enumerate(chalk):
            if(k < chalkVal ):
                indexReplacer = studentIndex
                break
            else:
                k = k - chalkVal
            studentIndex += 1
        return indexReplacer
