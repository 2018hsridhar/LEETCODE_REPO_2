'''
516. Longest Palindromic Subsequence
URL := https://leetcode.com/problems/longest-palindromic-subsequence/description/

Categories : TDDP/BUDP, Recursion, Explore Possibilities

Complexity
N = len(input)
T = O(pow(N,2))
S = O(pow(N,2)) ( E ) O(N) ( I ) 

Close but almost there ( one off err here )
Huh twas the other condition here :-O !
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = dict()
        for idx in range(len(s)):
            memo[idx] = dict()
        start = 0
        end = len(s) - 1
        llp = self.helper(s,start,end,memo)
        return llp

    def helper(self, s:str, start:int, end:int, memo:dict) -> int:
        llp = 0
        # definitely a 0 here
        if(start > end):
            return 0
        if(start in memo and end in memo[start]):
            llp = memo[start][end]
        else:
            if(start == end):
                if(s[start] == s[end]):
                    llp = 1
                else:
                    llp = 0
            else:
                caseOne = self.helper(s,start,end-1,memo)
                caseTwo = self.helper(s,start+1,end,memo)
                caseThree = self.helper(s,start+1,end-1,memo)
                # formulation as a `stateSpace` :-)
                stateSpace = [llp,caseOne,caseTwo,caseThree]
                if(s[start] == s[end]):
                    specialCase = caseThree + 2
                    stateSpace.append(specialCase)
                llp = max(stateSpace)
        curDict = memo[start]
        curDict[end] = llp
        return llp
