'''
URL = https://leetcode.com/problems/maximum-palindromes-after-operations/description/
3035. Maximum Palindromes After Operations

Complexity
Sigma = size(lang) = 26 = const
N = len(words)
W = len(longestWord)
T = O(NW) + O(WlgW) + O(N)
S = O(W) ( Exp ) O(1) ( Imp ) ( all const really )
'''
class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        maxNumPalindromes = 0
        freqMap = dict()
        wordLengths = [len(word) for word in words]
        wordLengths.sort()
        for word in words:
            for letter in word:
                if(letter not in freqMap):
                    freqMap[letter] = 0
                freqMap[letter] += 1
        evenCount = 0
        oddCount = 0
        for k,v in freqMap.items():
            if(v%2 == 1):
                v -= 1
                oddCount += 1
            evenCount += v
        for candidLen in wordLengths:
            # odd case : source an odd ( from oddCount, of evenCount no more odds )
            if(candidLen % 2 == 1):
                candidLen -= 1
                if(oddCount > 0):
                    oddCount -= 1
                elif(oddCount == 0):
                    if(evenCount >= 2):
                        evenCount -= 2
                        oddCount += 1
                    else:
                        break
            # now candidLen % 2 == 0): continue operation
            if(evenCount >= candidLen):
                evenCount -= candidLen
                maxNumPalindromes += 1
            else:
                break
        return maxNumPalindromes
        
