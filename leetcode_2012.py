Python linear time linear space solution counting enumeration running max and running min

2018hsridhar
100 Days Badge 2022
28
0
in a few seconds
C++
Python3
Array
Intuition and Approach
Counting, Running Summations, Iteration, Array, Single Pass Linear Scans

Complexity
N:= input length

Time complexity:
O(N)

Space complexity:
O(N)(E)O(1)(I)

Code
'''
URL := https://leetcode.com/problems/sum-of-beauty-in-the-array/description/
2012. Sum of Beauty in the Array
'''
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        beautyScore = [2 for idx in range(len(nums))]
        beautyScore[0] = 0
        beautyScore[-1] = 0
        self.goThroughArrayLeft(nums, beautyScore)
        self.goThroughArrayRight(nums, beautyScore)
        # [3] get final score
        finalScore = sum(beautyScore)
        return finalScore

    def goThroughArrayLeft(self, nums:List[int], beautyScore:List[int]) -> None:
        runMaxLeft = nums[0]
        for idx in range(1,len(nums)-1,1):
            curNum = nums[idx]
            if(runMaxLeft >= curNum):
                leftVal = nums[idx-1]
                rightVal = nums[idx+1]
                if(leftVal < curNum and curNum < rightVal):
                    beautyScore[idx] = 1
                else:
                    beautyScore[idx] = 0
            runMaxLeft = max(runMaxLeft,curNum)

    def goThroughArrayRight(self, nums:List[int], beautyScore:List[int]) -> None:
        runMinRight = nums[-1]
        for idx in range(len(nums)-2,0,-1):
            curNum = nums[idx]
            if(curNum >= runMinRight):
                leftVal = nums[idx-1]
                rightVal = nums[idx+1]
                if(leftVal < curNum and curNum < rightVal):
                    beautyScore[idx] = 1
                else:
                    beautyScore[idx] = 0
            runMinRight = min(runMinRight,curNum)
