'''
3185. Count Pairs That Form a Complete Day II
URL := https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/description/

Intuition and Approach : Arrays, Hashmap, Counting, Enumeration
Leverage modular 24 arithmetic. only 24 vals ( 0-23 ) permissible : hence, constant space.

Complexity
N := len(hrs)
T = O(N)
S = O(1) ( Explicit and Implicit ) 
'''
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        numberDayPairs = 0
        n = len(hours)
        hourFreq = dict()
        modulo = 24
        for hour in hours:
            rem = hour % modulo
            if(rem not in hourFreq):
                hourFreq[rem] = 0
            hourFreq[rem] += 1
        for lowerHour in range(0,13,1):
            if(lowerHour in hourFreq):
                numLower = hourFreq[lowerHour]
                if(lowerHour == 0 or lowerHour == 12):
                    numberDayPairs += self.snn(numLower)
                else:
                    upperHour = 24 - lowerHour
                    if(upperHour in hourFreq):
                        numUpper = hourFreq[upperHour]
                        numberDayPairs += (numLower * numUpper)
        return (int)(numberDayPairs)

    def snn(self, x:int) -> int:
        return x * (x-1) * 0.5
