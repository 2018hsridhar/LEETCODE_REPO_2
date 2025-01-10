'''
URL := https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/description/
2772. Apply Operations to Make All Array Elements Equal to Zero

Target complexity analysis
Let N := length(input list)
Time = O(N)
Space = O(1)  (E) O(1) ( I ) 

Intuition and Approach :
1. We must traverse the array left to right. If we have an element > 0 in the first index ( 0 ), we must decrement it by exactly it's value
2. Apply those decrements rightbound ( by size of k )
3. If a condition breaks for a given element, then bail out

Can we think in terms of sliding windows as well ( for incr/decr operations )?

'''
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        canMakeAllZero = True
        n = len(nums)
        posDeltas = [0 for idx in range(n)]
        runSum = 0
        index = 0
        leftBound = len(nums) - k
        while(index <= leftBound):
            num = nums[index]
            runSum -= posDeltas[index]
            valDiff = num - runSum
            if(valDiff >= 0):
                if(index + k < n):
                    posDeltas[index + k] = valDiff
                runSum += valDiff
            elif(valDiff < 0):
                canMakeAllZero = False
                break
            index += 1
        # check rest can go to zero ( special case here )
        # evolve run Sum here?
        while(index < len(nums)):
            runSum -= posDeltas[index]
            curNum = nums[index]
            if(curNum - runSum != 0):
                canMakeAllZero = False
            index += 1
        return canMakeAllZero
        
