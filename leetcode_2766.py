'''
URL := https://leetcode.com/problems/relocate-marbles/description/
2766. Relocate Marbles

Category : Single Pass, Linear Scan, Sets, Enumeration

Complexity
Let M := #-moves
Let N := len(nums)
Time := O(N) + O(M)
Space := O(M+N) ( E ) O(1) ( I ) 

Compiler NameNotDefined errors

15 minutes

'''
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        curPosSet = set(nums)
        # `zip` stops at the shorter list
        for moveOne,moveTwo in zip(moveFrom,moveTo):
            # print("MoveOne = " + str(moveOne) + " \t moveTwo = " + str(moveTwo))
            # WTF a .discard(...) method
            curPosSet.discard(moveOne)
            curPosSet.add(moveTwo)
        # print(curPosSet)
        # print(type(curPosSet))
        finalPositions = list(curPosSet)
        # woah you can't return directly from a call to the `.sort()` method in Python3
        # you must call .sort() on it : perhaps it's return of a function call is actuall empty!
        finalPositions.sort()
        return finalPositions
        
