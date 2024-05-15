'''
2957. Remove Adjacent Almost-Equal Characters
URL := https://leetcode.com/problems/remove-adjacent-almost-equal-characters/description/

Category : BUDP, Naive Recursion, Linear Scan, Memory FootPrint

Complexity :
Let N := len(word)
T := O(N)
S := O(N) ( E ) O(1) ( I ) 

Cases :
(A) "a"     -> 0
(B) "aaaaa" -> 2
(C) "ababa" -> 2
(D) "acaca" -> 0

It is minimization here

'''
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # don't get to max -> save on bits/memFtPrint
        minOpsNeeded = len(s)
        n = len(s)
        memo = [-1 for i in range(len(word))]
        for i,curChar in list(reversed(enumerate(s))):
            # default of 0 ( single char case )
            curSubProblem = 0
            if(i+1 < n):
                # check first char swap
                firstChar = word[i+1]
                if(abs(ord(firstChar) - ord(curChar)) <= 1):
                    curSubProblem = min(curSubProblem, 1 + memo[i+1])
                else:
                    curSubProblem = min(curSubProblem, memo[i+1])
                if(i+2 < n):
                # check second char swap
                    secondChar = word[i+2]
                    if(abs(ord(secondChar) - ord(firstChar)) <= 1):
                        curSubProblem = min(curSubProblem, 1 + memo[i+2])
                    else:
                        curSubProblem = min(curSubProblem, 1 + memo[i+1])
            memo[i] = curSubProblem
        minOpsNeeded = memo[0]
        return minOpsNeeded
        
