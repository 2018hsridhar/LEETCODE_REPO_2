'''
URL := https://leetcode.com/problems/the-kth-factor-of-n/description/
1492. The kth Factor of n
'''
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        kth = -1
        # Set up range start and incr step val
        # range(...) is sadly exclusive
        factorCount = 0
        for i in range(1,n+1,1):
            if n % i == 0:
                factorCount += 1
                if(factorCount == k):
                    kth = i
                    break
        return kth
        
