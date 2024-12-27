'''
URL := https://leetcode.com/problems/number-of-same-end-substrings/description/
2955. Number of Same-End Substrings
'''
class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        letterFreqs = dict()
        sigma = 26
        prefixSum = [[0 for idx in range(len(s))] for j in range(sigma)]
        # should we deep copy this or prefix sum things instead? 
        for col,letter in enumerate(s):
            prefixSum[ord(letter) - ord('a')][col] += 1
            for row in range(len(prefixSum)):
                if(col - 1 >= 0):
                    prefixSum[row][col] += prefixSum[row][col - 1]
        q = len(queries)
        # pre-initialize arrays for faster compute?
        answers = [0 for idx in range(q)]
        # 26 letters max only -> can we determine range quickly
        # src : value of a, to right or equal
        # dst : value of a, as close on the left or equal
        # a at index positions : 4,6,10,15,18 -> we need a count, not the index positions here
        # oh wait prefix sums makes this easy SMH sigma bounded
        for idx, query in enumerate(queries):
            [src,dst] = query
            ans = 0
            for ordLetter in range(sigma):
                countDst = prefixSum[ordLetter][dst]
                actualCount = countDst
                if(src - 1 >= 0):
                    countSrc = prefixSum[ordLetter][src - 1]
                    actualCount -= countSrc
                ans += (int)(actualCount * ( actualCount + 1) * 0.5)
            answers[idx] = ans
        return answers
