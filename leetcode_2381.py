'''
URL := https://leetcode.com/problems/shifting-letters-ii/description/
2381. Shifting Letters II

Definitely prefix sums : decompose the shifts
    One dir forward and one dir backwards
    Get the total shift direction too : compute the sums and then modulo later

Complexity
N = len(input)
T = O(N)
S = O(N) ( Explicit ) O(1) ( Implicit ) 
'''
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # go backwards
        finalStr = ""
        goForwards = [0 for idx in range(len(s))]
        goBackwards = [0 for idx in range(len(s))]
        for [start,end,shiftDir] in shifts:
            if(shiftDir == 1):
                goForwards[end] += 1
                if(start > 0):
                    goBackwards[start - 1] += 1
            elif(shiftDir == 0):
                goBackwards[end] += 1
                if(start > 0):
                    goForwards[start - 1] += 1
        # adjust forwards, backwards values again
        prefixSum = 0
        for idx in range(len(goForwards) - 1,-1,-1):
            prefixSum += goForwards[idx]
            goForwards[idx] = prefixSum
        prefixSum = 0
        for idx in range(len(goBackwards)-1,-1,-1):
            prefixSum += goBackwards[idx]
            goBackwards[idx] = prefixSum
        deltas = [(goForwards[idx] - goBackwards[idx]) for idx in range(len(s))]
        sigma = 26
        base = 'a'
        for index,delta in enumerate(deltas):
            adjDelta = ((delta % sigma) + sigma)%sigma
            curLet = s[index]
            baseValue = ord(curLet) - ord(base)
            bucketValue = (baseValue + adjDelta) % sigma
            adjChar = chr(ord('a') + bucketValue)
            finalStr += adjChar
        return finalStr
        



        
