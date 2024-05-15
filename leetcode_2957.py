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
        minOpsNeeded = len(word)
        n = len(word)
        memo = [-1 for i in range(len(word))]
        # enumerate() -> returns iterator
        for i,curChar in reversed(list(enumerate(word))):
            # default of 0 ( single char case )
            curSubProblem = len(word)
            # check second char swap
            if(i+1 < n and i+2 < n):
                secondChar = word[i+2]
                # even if firstChar and curChar deviate, that doesn't matter
                if(abs(ord(secondChar) - ord(firstChar)) <= 1):
                    curSubProblem = min(curSubProblem, 1 + memo[i+2])
                else:
                    if(abs(ord(firstChar) - ord(curChar)) <= 1):
                        curSubProblem = min(curSubProblem, 1 + memo[i+2])
                    else:
                        curSubProblem = min(curSubProblem, 0 + memo[i+1])
            # check first char swap
            # mofo : `elif`` saves 3 characters over `else if`
            if(i+1 < n):
                firstChar = word[i+1]
                if(abs(ord(firstChar) - ord(curChar)) <= 1):
                    curSubProblem = min(curSubProblem, 1 + memo[i+1])
                else:
                    curSubProblem = min(curSubProblem, 0 + memo[i+1])
            elif ( i+1 >= n):
                # last character base case anyways
                curSubProblem = 0
            memo[i] = curSubProblem
        minOpsNeeded = memo[0]
        return minOpsNeeded
        
