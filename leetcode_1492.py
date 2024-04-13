'''
URL := https://leetcode.com/problems/the-kth-factor-of-n/description/
1492. The kth Factor of n

Yes have a O(sqrt(n)) solution with tradeoff of space though :-(
'''
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        kth = -1
        # Set up range start and incr step val
        # range(...) is sadly exclusive
        factorCount = 0
        # for i in range(1,n+1,1):
        # type conversions can be lossy too
        # can get factor count -> but how to get list in the other way?
        # cut of decimals -> closer to floor functionality
        cap = int(sqrt(n))
        for i in range(1,cap+1,1):
            if n % i == 0:
                factorCount += 1
                if(factorCount == k):
                    kth = i
                    break
        # Do not double count the cap value
        # print(factorCount)
        # symmetric : set for hit factors
        for i in range(cap,0,-1):
            rem = int(n/i)
            if(rem != i):
                if n % i == 0:
                    factorCount += 1
                    if(factorCount == k):
                        kth = rem
                        break
        return kth
        
