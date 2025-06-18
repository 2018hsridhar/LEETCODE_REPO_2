'''
140. Word Break II
URL := https://leetcode.com/problems/word-break-ii/description/

Categories : BUDP, Backtracking, Recursion, String Matching, Two Pointres
Or better - use a set ( word Dict ) and convert ( check set membership ) 
Constraints are very tiny : s, words, and word dictionary + all unique
15 minute and 100% beaten first submission OMFG
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        DELIM = " "
        sentences = []
        n = len(s)
        dictionary = set(wordDict)
        memo = dict()
        for leftPtr in range(n-1,-1,-1):
            parentProblem = []
            for rightPtr in range(leftPtr+1,n+1,1):
                prefix = s[leftPtr:rightPtr]
                if(prefix in dictionary):
                    if(rightPtr < n and rightPtr in memo):
                        childProblem = memo[rightPtr]
                        for childSentence in childProblem:
                            parentSentence = [prefix]
                            for childToken in childSentence:
                                parentSentence.append(childToken)
                            parentProblem.append(parentSentence)
                    elif(rightPtr == n):
                        parentSentence = [prefix]
                        parentProblem.append(parentSentence)
            memo[leftPtr] = parentProblem
        sentences = [DELIM.join(sentenceList) for sentenceList in memo[0]]
        return sentences
