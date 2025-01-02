'''
Max value 
Strictness of inequality matters : = case 
Positive negative case decomposition

1881. Maximum Value after Insertion
URL := https://leetcode.com/problems/maximum-value-after-insertion/

Complexity
T = O(N)
S = O(N) ( E ) O(1) ( I ) 

Negative case : make smallest value
10 minutes to solutioning :-)
'''
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        # negative case
        maxValue = ""
        if(n[0] == '-'):
            remN = n[1:]
            insertPos = -1
            for index,digit in enumerate(remN):
                digValue = (int)(digit)
                if(x < digValue):
                    # insert after this index
                    insertPos = index
                    break
            if(insertPos == -1):
                maxValue = "-" + remN + (str)(x)
            else:
                maxValue = "-" + remN[:insertPos] + (str)(x) + remN[insertPos:]
        else:
            insertPos = -1
            for index,digit in enumerate(n):
                digValue = (int)(digit)
                if(x > digValue):
                    # insert before this index
                    insertPos = index
                    break
            if(insertPos == -1):
                maxValue = n + (str)(x)
            else:
                maxValue = n[0:insertPos] + (str)(x) + n[insertPos:]
        return maxValue
