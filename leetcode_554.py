'''
554. Brick Wall
URL := https://leetcode.com/problems/brick-wall/description/

Complexity
N = #-rows of bricks
T = O(N)
S = O(N) ( Exp ) O(1) ( Imp ) 

Approach : Hashmaps, Frequency Counting, Iteration
'''
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        numBrickRows = len(wall)
        lastCol = sum(wall[0])
        # A bound is known : presume we cross all bricks
        minNumCrossBricks = numBrickRows
        positionFreq = dict()
        for brickRow in wall:
            brickRightPos = 0
            for brick in brickRow:
                brickRightPos += brick
                if(brickRightPos not in positionFreq):
                    positionFreq[brickRightPos] = 0
                positionFreq[brickRightPos] += 1
        del positionFreq[lastCol]
        for column, colFreq in positionFreq.items():
            numCrossedBricks = numBrickRows - colFreq
            minNumCrossBricks = min(minNumCrossBricks, numCrossedBricks)
        return minNumCrossBricks
        
