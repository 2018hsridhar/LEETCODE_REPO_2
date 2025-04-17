'''
3412. Find Mirror Score of a String
URL := https://leetcode.com/problems/find-mirror-score-of-a-string/description/

Complexity
T = O(N)
S = O(1) ( E ) O(1) ( I ) 
'''
class Solution:
    def calculateScore(self, s: str) -> int:
        totalScore = 0
        # when alphabet is revrsed
        MIRROR = 25
        BASE = 'a'
        letterIndices = dict()
        for iIndex,letter in enumerate(s):
            # [1] check if mirror letter exists
            ordVal = ord(letter) - ord(BASE)
            mirVal = MIRROR - ordVal
            mirLetter = chr(mirVal + ord(BASE))
            markedLetter = False
            if(mirLetter in letterIndices):
                if(len(letterIndices[mirLetter]) > 0):
                    jIndex = letterIndices[mirLetter][-1]
                    del letterIndices[mirLetter][-1]
                    dist = abs(iIndex - jIndex)
                    totalScore += dist
                    markedLetter = True
            # [2] Append letter
            if(markedLetter == False):
                if(letter not in letterIndices):
                    letterIndices[letter] = []
                letterIndices[letter].append(iIndex)
        return totalScore
