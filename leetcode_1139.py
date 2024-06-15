'''
URL := https://leetcode.com/problems/largest-1-bordered-square/description/
1139. Largest 1-Bordered Square

30 mins to solutioning
'''
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        largest = 0
        # compute number on top
        m = len(grid)
        n = len(grid[0])
        leftCount = [[0 for j in range(n)] for i in range(m)]
        rightCount = [[0 for j in range(n)] for i in range(m)]
        topCount = [[0 for j in range(n)] for i in range(m)]
        bottomCount = [[0 for j in range(n)] for i in range(m)]
        for c in range(n):
            countAbove = 0
            countBelow = 0
            for r in range(m):
                countAbove = (countAbove + 1) if (grid[r][c] == 1) else 0
                topCount[r][c] = countAbove
            for r in range(m - 1, -1, -1):
                countBelow = (countBelow + 1) if (grid[r][c] == 1) else 0
                bottomCount[r][c] = countBelow
        # compute number on left
        # compute number on right
        for r in range(m):
            countLeft = 0
            countRight = 0
            for c in range(n):
                countLeft = (countLeft + 1) if (grid[r][c] == 1) else 0
                leftCount[r][c] = countLeft
            for c in range(n-1,-1,-1):
                countRight = (countRight + 1) if (grid[r][c] == 1) else 0
                rightCount[r][c] = countRight
        # go through each square : get minimas of counts :-)
        # ensured inductively too
        for r1 in range(m):
            for c1 in range(n):
                i = 0
                while(True):
                    r2 = r1 + i
                    c2 = c1 + i
                    if(r2 < m and c2 < n):
                        eastCount = rightCount[r1][c1]
                        southCount = bottomCount[r1][c1]
                        northCount = topCount[r2][c2]
                        westCount = leftCount[r2][c2]
                        # numOnesBorder = min([eastCount,southCount,northCount,westCount])
                        numOnesIntersect = min([eastCount,southCount,northCount,westCount])
                        dimSize = (i+1)
                        if(numOnesIntersect >= dimSize):
                            largest = max(largest, dimSize)
                        i += 1
                    else:
                        break
        return (int)(pow(largest,2))
        
