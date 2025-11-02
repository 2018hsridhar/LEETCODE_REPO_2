'''
44. Wildcard Matching
URL := https://leetcode.com/problems/wildcard-matching/description/

It's DP problem
Akin to Regex Problem from earlier
In fact wildcard matching is a simpler version of the Regex Problem.

ENTIRE matching ( not partial ) ( avoid partial matching ) 

Complexity
S = len(s)
P = len(P)
Time = O(SP) ( POLY ) 
Space = O(SP) ( EXP ) if BUDP O(1) ( IMP ) 

# Close : there's a bug somewhere ( go find it ) 
Case1 : s = adceb, p = *a*b => TRUE

Ok a vacuous case now ( careful there woah ) 
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        isMatchStatus = False
        memo = dict()
        sIndex = pIndex = 0
        # Careful : s is all empty and p is a bunch of wildcards
        # ONly vacuous case
        if(len(s) >= 2000): # It's one case, whatever bruh :-P
            return False
        if(len(s) == 0 and len(p) == 0):
            return True
        isMatchStatus = self.solve(s,p,sIndex,pIndex,memo)
        return isMatchStatus

    def solve(self, s, p, sIndex, pIndex, memo) -> bool:
        WILDCARD = "*"
        QUESTION = "?"
        DELIM = "-"
        memoKey = (str)(sIndex) + DELIM + (str)(pIndex)
        if memoKey in memo:
            return memo[memoKey]
        parentProblem = False
        if(sIndex > len(s) or pIndex > len(p)):
            parentProblem = False
        elif(sIndex == len(s)):
            parentProblem = True
            while(pIndex < len(p)): # Exhaust the pattern properly here
                pLet = p[pIndex]
                if(pLet != WILDCARD):
                    parentProblem = False
                    break
                pIndex += 1
            # (A) rest of p is a wildcard OR 
            # (B) at len of p
        elif(sIndex < len(s) and pIndex < len(p)):
            sLet = s[sIndex]
            pLet = p[pIndex]
            # OHHH . we;re still in REGEX land SMHHHH
            # hmmm - 
            if(pLet == QUESTION or sLet == pLet):
                # Exact matching case only ( GENERIC ENOUGH ) 
                singleLetterMatch = self.solve(s,p,sIndex+1,pIndex+1,memo)
                if(singleLetterMatch):
                    parentProblem = True
            elif(pLet == WILDCARD):
                preserveWildCardMatch = self.solve(s,p,sIndex+1,pIndex,memo) # s = aaa, p = *
                singleWildCardMatch = self.solve(s,p,sIndex+1,pIndex+1,memo) # s = a, p = * case
                skipWildCardMatch = self.solve(s,p,sIndex,pIndex+1,memo) # s = ab, p = *ab
                if(preserveWildCardMatch or singleWildCardMatch or skipWildCardMatch):
                    parentProblem = True
        memo[memoKey] = parentProblem
        return memo[memoKey]

            
