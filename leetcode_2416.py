'''
2416. Sum of Prefix Scores of Strings
URL := https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

Naive solution -> leverage hashmap
Complexity
W = #-words
L = worst-case length word

Time = O(WL)
Space = O(WL) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        w = len(words)
        answers = [0 for idx in range(w)]
        prefixFreq = dict()
        for word in words:
            prefix = ""
            for letter in word:
                prefix += letter
                if(prefix not in prefixFreq):
                    prefixFreq[prefix] = 0
                prefixFreq[prefix] += 1
        for index,word in enumerate(words):
            answer = 0
            prefix = ""
            for letter in word:
                prefix += letter
                curScore = prefixFreq[prefix]
                answer += curScore
            answers[index] = answer
        return answers

        
