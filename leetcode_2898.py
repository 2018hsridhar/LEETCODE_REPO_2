'''
2898. Maximum Linear Stock Score
URL := https://leetcode.com/problems/maximum-linear-stock-score/description/

Complexity
N = len(input)
T = O(N)
S = O(1) ( E and I ) 
'''
class Solution:
    def maxScore(self, prices: List[int]) -> int:
        bestScore = 0
        freqMap = dict()
        for index,price in enumerate(prices):
            delta = price - index
            if(delta not in freqMap):
                freqMap[delta] = 0
            freqMap[delta] += price
            bestScore = max(bestScore, freqMap[delta])
        return bestScore

        
