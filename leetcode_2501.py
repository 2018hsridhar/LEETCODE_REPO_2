Intuition and Approach
Akin to many hashtable/hashmap chaining problems from the past
[2,2,4,4,8,8,16,16] -> PASS

Complexity
Time complexity:
O(NlgN)

Space complexity:
O(N)(E)O(1)(I)

Code
'''
URL := https://leetcode.com/problems/longest-square-streak-in-an-array/description/
2501. Longest Square Streak in an Array
'''
import math

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        longestStreak = 0

        nums.sort()

        freqMap = dict()
        for num in nums:
            if(num not in freqMap):
                freqMap[num] = 0
            freqMap[num] += 1

        for num in nums:
            curVal = num
            curRunLen = 1
            # NameError common
            while(True):
                freqMap[curVal] -= 1
                nextSquare = curVal**2
                if(nextSquare in freqMap):
                    curRunLen += 1
                    curVal = nextSquare
                else:
                    break
            longestStreak = max(longestStreak, curRunLen)
        if(longestStreak == 1):
            longestStreak = -1
        return longestStreak
