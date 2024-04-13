'''
1593. Split a String Into the Max Number of Unique Substrings
URL := https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/

Backtracking with set : add and remove as we go
Dodge overlapping subproblems
default asnwer of 1 ( no splitting )

Len = 16 ( reasonably bounded )
Max uniqueness ( constraint problem )

At least PY doesn't force to much OOP with basic method definitions.

'''

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # confusion : self VS this keyword
        # Use of the `self` keyword too in lieu of `this` keyword -> self not as position param
        startIdx = 0
        uniqueTokens = set()
        # compilation : implicit packages issues abound?
        return max(1, self.helper(uniqueTokens, s, startIdx)) - 1

    def helper(self, uniqueTokens: set, s:str, readIdx:int) -> int:
        subProblemMaxLen = 1
        for i in range(readIdx, len(s), 1):
            curPrefix = s[readIdx:i+1]
            if(curPrefix not in uniqueTokens):
                uniqueTokens.add(curPrefix)
                subProblemMaxLen = max(subProblemMaxLen, 1 + self.helper(uniqueTokens,s,i+1))
                uniqueTokens.remove(curPrefix)
        return subProblemMaxLen
        








        
