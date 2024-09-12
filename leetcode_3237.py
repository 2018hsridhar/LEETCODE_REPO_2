Intuition and Approach
We only pop up the elements in the queries, and if a query is duplicated, we focus and target the most recent query element.
Can we go through our queries in reverse, and note the position of the first time an element shows in the reverse order ( the most recent element )?
Queries :
[3,3,2,1,2,3,1,1,3] <- in this order => [3,1,2] equivalent ( dedupe our data ordering )

Complexity
Let N:= len (windows)
Let Q:= len(queries)

Time complexity:
O(Q)+O(N)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
'''
3237. Alt and Tab Simulation
URL := https://leetcode.com/problems/alt-and-tab-simulation/description/

'''
class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        simRes = []
        queries.reverse()
        distinctQueryEls = set()
        targetRev = []
        for query in queries:
            if query not in distinctQueryEls:
                distinctQueryEls.add(query)
                targetRev.append(query)
        notInQueryWindow = []
        for num in windows:
            if num not in distinctQueryEls:
                notInQueryWindow.append(num)
        simRes = targetRev + notInQueryWindow
        return simRes
