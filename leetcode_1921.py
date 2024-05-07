'''
URL := https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/
1921. Eliminate Maximum Number of Monsters

'''
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Really appreciating the zip(...) functionality for list comprehension in Python 3 code
        # List comprehension enables code conciseness
        calculations = [int(ceil(pairing[0]/pairing[1])) for pairing in zip(dist, speed)]
        calculations.sort()
        numTurnsNeeded = 1
        for ptr in range(len(calculations)):
            if(numTurnsNeeded <= calculations[ptr]):
                numTurnsNeeded += 1
            else:
                break
        # we hit last index -> this defacto will win ( given earlier guarantee ) 
        return numTurnsNeeded - 1
