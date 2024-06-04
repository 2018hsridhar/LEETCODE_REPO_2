'''
2337. Move Pieces to Obtain a String
URL := https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/

Commit Message Log :
(A) Fun problem with ordering of a language guarantee
(B) letterPositions = list() ( appreciative of initialization style ) 
(C)

Complexity :
Let N := len(start)
Time = O(N)
Space = O(N) ( E ) O(1) ( I )
'''
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        changeStatus = True
        startPos = self.buildLetterPositions(start)
        targetPos = self.buildLetterPositions(target)
        if(len(startPos) != len(targetPos)):
            changeStatus = False
        else:
            for index in range(len(startPos)):
                spPair = startPos[index]
                tpPair = targetPos[index]
                spLet = spPair[0]
                tpLet = tpPair[0]
                spPos = spPair[1]
                tpPos = tpPair[1]
                if(spLet != tpLet):
                    changeStatus = False
                elif(spLet == 'L' and spPos < tpPos):
                    changeStatus = False
                elif(spLet == 'R' and spPos > tpPos):
                    changeStatus = False
        return changeStatus
        
    def buildLetterPositions(self, target:str) -> List[int]:
        letterPositions = list()
        for index, letter in enumerate(target):
            if(letter != '_'):
                letterPositions.append([letter,index])
        return letterPositions
