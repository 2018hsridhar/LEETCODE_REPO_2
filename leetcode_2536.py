'''
URL := https://leetcode.com/problems/increment-submatrices-by-one/description/
2536. Increment Submatrices by One

Categories : Prefix Summation, Math, Counting, Enumeration, DP

Complexity
N = length(grid)
Time = O(pow(N,2))
Space = O(pow(N,2)) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        m = n
        n = n
        answer = [[0 for j in range(n)] for i in range(m)]
        gridAdd = [[0 for j in range(n)] for i in range(m)]
        gridSub = [[0 for j in range(n)] for i in range(m)]
        # 10^4 * 500 ops max ( for row, col ) expansion
        for query in queries:
            [r1,c1,r2,c2] = query
            for row in range(r1,r2+1,1):
                gridAdd[row][c2] += 1
                if(c1 - 1 >= 0):
                    gridSub[row][c1 - 1] += 1
        self.expandGrid(gridAdd)
        self.expandGrid(gridSub)
        for r in range(n):
            for c in range(n):
                answer[r][c] = gridAdd[r][c] - gridSub[r][c]
        return answer

    def expandGrid(self, grid:List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            runSum = 0
            for c in range(n-1,-1,-1):
                runSum += grid[r][c]
                grid[r][c] = runSum
        
