'''
1958. Check if Move is Legal
URL := https://leetcode.com/problems/check-if-move-is-legal/description/

Gameplay :
1. Choose free cell change it to color your'eplaying
2. good line : 3+ cells ( including endpoints ) with one shared color ( endpoints ) and middle opposite colors
Check move legality : endpoint criteria must be met!
Color the cell with selection and enumeration

8x8 game
Time = O(1) ( const ) ( dims small and known ) 
Space = O(1) ( E ) O(1) ( I ) 

15 mins again is this even what I should be doing??
'''
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m = 8
        n = 8
        meetsCriteria = False
        board[rMove][cMove] = color
        colorMap = {
            'W':'B',
            'B':'W',
        }
        oColor = colorMap[color]
        # check vertical => go top
        meetsCriteria = meetsCriteria or self.checkVertical(board, rMove, cMove, oColor)
        meetsCriteria = meetsCriteria or self.checkHoz(board, rMove, cMove, oColor)
        meetsCriteria = meetsCriteria or self.checkUpperDiag(board, rMove, cMove, oColor)
        meetsCriteria = meetsCriteria or self.checkLowerDiag(board, rMove, cMove, oColor)
        return meetsCriteria

    def checkLowerDiag(self, board, rMove, cMove, oColor):
        meetsMoveCriteria = False
        runSum = 0
        rCur = rMove - 1
        cCur = cMove - 1
        THRESH = 8
        initColor = board[rMove][cMove]
        # go upper left
        while(rCur >= 0 and cCur >= 0):
            if(board[rCur][cCur] == oColor):
                rCur -= 1
                cCur -= 1
                runSum += 1
            else:
                if(board[rCur][cCur] == initColor and runSum >= 1):
                    meetsMoveCriteria = True
                break

        # go bottom right
        rCur = rMove + 1
        cCur = cMove + 1
        runSum = 0
        while(rCur < THRESH and cCur < THRESH):
            if(board[rCur][cCur] == oColor):
                rCur += 1
                cCur += 1
                runSum += 1
            else:
                if(board[rCur][cCur] == initColor and runSum >= 1):
                    meetsMoveCriteria = True
                break
        return meetsMoveCriteria

    def checkUpperDiag(self, board, rMove, cMove, oColor):
        meetsMoveCriteria = False
        initColor = board[rMove][cMove]
        runSum = 0
        rCur = rMove - 1
        cCur = cMove + 1
        THRESH = 8
        # go upper right
        while(rCur >= 0 and cCur < THRESH):
            if(board[rCur][cCur] == oColor):
                rCur -= 1
                cCur += 1
                runSum += 1
            else:
                if(board[rCur][cCur] == initColor and runSum >= 1):
                    meetsMoveCriteria = True
                break

        # go bottom left
        runSum = 0
        rCur = rMove + 1
        cCur = cMove - 1
        while(rCur < THRESH and cCur >= 0):
            if(board[rCur][cCur] == oColor):
                rCur += 1
                cCur -= 1
                runSum += 1
            else:
                if(board[rCur][cCur] == initColor and runSum >= 1):
                    meetsMoveCriteria = True
                break
        return meetsMoveCriteria

    def checkHoz(self, board, rMove, cMove, oColor) -> bool:
        meetsMoveCriteria = False
        initColor = board[rMove][cMove]
        runSum = 0
        m = 8
        n = 8
        for c in range(cMove-1,-1,-1):
            if(board[rMove][c] == oColor):
                runSum += 1
            else:
                if(board[rMove][c] == initColor and runSum >= 1):
                    meetsMoveCriteria = True
                break
        runSum = 0
        for c in range(cMove+1,m,1):
            if(board[rMove][c] == oColor):
                runSum += 1
            else:
                if(board[rMove][c] == initColor and runSum >= 1):
                    meetsMoveCriteria = True
                break
        return meetsMoveCriteria

    # What a terse, concise to express language
    # minimal static typing for parameter passing :-) !
    def checkVertical(self, board, rMove, cMove, oColor) -> bool:
        meetsMoveCriteria = False
        initColor = board[rMove][cMove]
        runSum = 0
        m = 8
        n = 8
        for r in range(rMove-1,-1,-1):
            if(board[r][cMove] == oColor):
                runSum += 1
            else:
                if(board[r][cMove] == initColor and runSum >= 1):
                    meetsMoveCriteria = True
                break
        runSum = 0
        for r in range(rMove+1,m,1):
            if(board[r][cMove] == oColor):
                runSum += 1
            else:
                if(board[r][cMove] == initColor and runSum >= 1):
                    meetsMoveCriteria = True
                break
        return meetsMoveCriteria






        
