'''
URL := https://leetcode.com/problems/score-of-parentheses/description/
856. Score of Parentheses
'''
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        sop = 0
        stk = []
        # not a range lop here
        for letter in s:
            # always a default for left -> right is trickier
            if(letter == '('):
                # alwasy append a 1 by default ( is a closing score )
                stk.append([1,0])
            elif(letter == ')'):
                # go bounds checking at least
                if(stk[-1][1] == 0): 
                    stk[-1][1] = 1
                if(len(stk) >= 2):
                    lastEl = stk[-1]
                    del stk[-1]
                    stk[-1][0] = 2
                    stk[-1][1] += lastEl[0] * lastEl[1]
                # really a base case : go adding please ( and restore stack to original state )
                # as if you are solving a new problem at least
                elif(len(stk) == 1):
                    sop += stk[0][0] * stk[0][1]
                    stk[-1][1] = 1
                    del stk[-1]
        return sop
