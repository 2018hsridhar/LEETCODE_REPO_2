'''
URL := https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/description/
2155. All Divisions With the Highest Score of a Binary Array

Category : Single Pass, Linear, Counting, Iterative

Complexity :
Let N := len(nums)
T := O(N)
S := O(1) ( E & I ) 

15 mins to solutioning
'''
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        maxScoreIndxs = []
        curMaxDivisionScore = 0
        # sum(..) probably underneath optimized
        countOneRight = sum(nums)
        countZeroLeft = 0
        # woah can divide last index too
        # for index,val in enumerate(nums):
        for index in range(len(nums) + 1):
            divisionScore = countZeroLeft + countOneRight
            if(divisionScore > curMaxDivisionScore):
                curMaxDivisionScore = divisionScore
                maxScoreIndxs = []
                # maxScoreIndxs.clear()
                # is append(...) easier to read versus add(...)?
                maxScoreIndxs.append(index)
            elif(divisionScore == curMaxDivisionScore):
                maxScoreIndxs.append(index)
            if(index < len(nums)):
                val = nums[index]
                if val == 0:
                    countZeroLeft += 1
                elif val == 1:
                    countOneRight -= 1
        return maxScoreIndxs

        
