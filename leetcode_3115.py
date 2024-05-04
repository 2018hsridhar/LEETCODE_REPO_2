'''
URL := https://leetcode.com/problems/maximum-prime-difference/description/
3115. Maximum Prime Difference

Quick acceptance

Category : Linear Scan, Single Pass, Numerical
The primes can also differentiate

Complexity
Let N := len(nums)
T := O(N*sqrt(N))
S := O(1) ( E & I )
'''
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        mpd = 0
        leftIdx = -1
        rightMostIdx = -1
        for i in range(len(nums)):
            primeStatus = self.isPrime(nums[i])
            # print("For i = " + str(i) + " isPrime = " + str(primeStatus))
            if(primeStatus):
                rightMostIdx = i
                if(leftIdx == -1):
                    leftIdx = i
                mpd = max(mpd, rightMostIdx - leftIdx)
        return mpd

    # Wow 1 is not Prime, yet, 2 is prime.
    def isPrime(self, val:int) -> bool:
        primeStatus = True
        if(val == 1):
            return False
        # make sure to handle implicit nonInt->int conv
        # is an import needed or not?
        factorMax = math.floor(sqrt(val))
        # Triple arg syntax range function
        for factor in range(2,factorMax + 1,1):
            if val % factor == 0:
                primeStatus = False
        return primeStatus
        
