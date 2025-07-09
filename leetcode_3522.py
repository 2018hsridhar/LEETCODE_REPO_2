'''
URL := https://leetcode.com/problems/calculate-score-after-performing-instructions/description/
3522. Calculate Score After Performing Instructions

Emulates instruction sets in computer architectures ( the pointers ) and a running process.

Complexity
N = len(inst)
T = O(N)
S = O(1) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        runScore = 0
        instIndex = 0
        numInst = len(instructions)
        visitedInst = set()
        ADD = "add"
        JUMP = "jump"
        while(True and instIndex >= 0 and instIndex < numInst and instIndex not in visitedInst):
            inst = instructions[instIndex]
            visitedInst.add(instIndex)
            value = values[instIndex]
            if(inst == ADD):
                runScore += value
                instIndex += 1
            elif(inst == JUMP):
                instIndex += value
        return runScore
