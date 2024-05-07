'''
URL := https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/description/
2521. Distinct Prime Factors of Product of Array

Complexity
Let N := len(nums)
Time = O(N*sqrt(N))
Space = O(1) ( E and I ) 

Category : Single Pass, Linear Scan, Number Theory, prime factorization theorem
Please remmeber : 2 is a prime number, and recall mathematical precision of numeric types.

Reduce number defined names in code
No full prod eval -> numeric overflow
'''
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primeFactorsHit = set()
        for val in nums:
            upperBound = int(ceil(sqrt(val))) + 1
            # Do we have to eval all factors? Or can we eval both sides of the coin instead?
            # 1,2,3,4,5,6,7,8,9,10 ( for a value like 1000 ) or bound but other side too ( 200 ) 
            for primeFactor in range(1,upperBound,1):
                # Can we honestly trip earlier too?
                if(val % primeFactor == 0):
                    otherFactor = int(val / primeFactor)
                    # print("prime factor = " + str(primeFactor) + " \t other factor = " + str(otherFactor))
                    if (self.isPrime(primeFactor) and primeFactor not in primeFactorsHit):
                        primeFactorsHit.add(primeFactor)
                    if (self.isPrime(otherFactor) and otherFactor not in primeFactorsHit):
                        primeFactorsHit.add(otherFactor)
        # Python tyty for len(collections) and using collections as a generisizer
        return len(primeFactorsHit)

    def isPrime(self, val:int) -> bool:
        primeStatus = True
        # negatives and 0 and 1 : never prime
        if(val <= 1):
            return False
        elif(val == 2):
            return True
        upperBound = int(ceil(sqrt(val))) + 1
        # divisible by 1 and itself only -> no other value
        # 2 is prime, so catch exception there too
        for factorUnderTest in range(2,upperBound, 1):
            if(val % factorUnderTest == 0):
                primeStatus = False
                break
        return primeStatus
