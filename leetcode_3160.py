Complexity
N = limit ( #-balls)
Q = #-queries

Time complexity:
O(Q)

Space complexity:
O(N)(E)O(1)(I)

Code
'''
URL := https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/
3160. Find the Number of Distinct Colors Among the Balls
'''
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # x = ball, y = color
        colorsToBalls = dict()
        ballToColors = dict()
        result = [0 for idx in range(len(queries))]
        for idx, [x,y] in enumerate(queries):
            # [x,y] = query
            # 1. remove old color ( if ball x alreayd added ) 
            if(x in ballToColors):
                oldColor = ballToColors[x]
                oldColorSet = colorsToBalls[oldColor]
                oldColorSet.remove(x)
                if(len(oldColorSet) == 0):
                    del colorsToBalls[oldColor]
            # 1. Add new color
            if(y not in colorsToBalls):
                colorsToBalls[y] = set()
            colorsToBalls[y].add(x)
            # 3. Update B2C - ball to color - map
            ballToColors[x] = y
            numDistinctColors = len(colorsToBalls)
            result[idx] = numDistinctColors
        return result

        
        


        
