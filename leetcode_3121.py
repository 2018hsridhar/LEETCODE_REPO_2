'''
3121. Count the Number of Special Characters II
URL := https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/

Categories : Frequency, Counting, Hashmaps
Every lowercase occur : before first uppercase occur -> track latest vs earliest index

Complexity
N = len(word)
Sigma = 52 = a constant : [a-zA-Z]
T = O(N)
S = O(1) ( Exp ) O(1) ( Imp )
'''
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        numSpecialChars = 0
        sigma = 26
        lowerBase = 'a'
        upperBase = 'A'
        noVal = -1
        lowerMap = [noVal for idx in range(sigma)]
        upperMap = [noVal for idx in range(sigma)]
        for index,letter in enumerate(word):
            pos = ord(letter)
            if(letter.islower()):
                pos -= ord(lowerBase)
                lowerMap[pos] = index
            elif(letter.isupper()):
                pos -= ord(upperBase)
                if(upperMap[pos] == noVal):
                    upperMap[pos] = index
        for lowerIdx,upperIdx in zip(lowerMap,upperMap):
            if(lowerIdx != noVal and upperIdx != noVal):
                numSpecialChars += (int)(lowerIdx < upperIdx)
        return numSpecialChars
