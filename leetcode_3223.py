Intuition and Approach
See problem title

Complexity
N := len(input)

Time complexity:
T=O(N)

Space complexity:
S=O(1)(E)
O(1)(I)

Code
'''
URL := https://leetcode.com/problems/minimum-length-of-string-after-operations/description/
3223. Minimum Length of String After Operations

Freq chars <= 2 : no edit doable
freqs char >= 3 : keep subtracting 2 till no longer possible

3 -> 1
4 -> 2 -> FIN
5 -> 3 -> 1 -> FIN
6 -> 4 -> 2 -> FIn

Even-Odd parity handling : odd -> 1 and even -> 2 terminal states
freq = 1 or freq = 2 = done
Even freq => 2 and odd freq => 1 
But solution for the frequencies
'''
class Solution:
    def minimumLength(self, s: str) -> int:
        targetMin = 0
        freqCount = dict()
        for char in s:
            if(char not in freqCount):
                freqCount[char] = 0
            freqCount[char] += 1
        for letter,letterFreq in freqCount.items():
            delta = 1
            if (letterFreq % 2 == 0):
                delta = 2
            targetMin += delta
        return targetMin
