'''
URL := https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
1111. Maximum Nesting Depth of Two Valid Parentheses Strings

Complexity
Let N := len(seq)
T := O(N)
S := O(N) ( E ) O(1) ( I ) 

Edge Cases :
(A)
(B)
(C)
(D)
(E)

'''
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        mdas = []
        curState = 0
        seqStk = []
        # int object no len() method
        for val in seq:
            if(val == '('):
                seqStk.append(val)
                mdas.append(curState)
            else:
                # woah a `del` operator :-)
                mdas.append(1 - curState)
                del seqStk[-1]
            curState = 1 - curState
        return mdas
     
