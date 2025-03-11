'''
3179. Find the N-th Value After K Seconds
URL := https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/description/

Intuition & Approach : Combinatorics, Pascal's Triangle, Bernoulli

Complexity
N = largest value ( eval factorial products a few times ) 
T = O(N) 
S = O(1) ( Explicit ) ( Implicit ) 

Seems correct save for muldo arithmetic
It's correct but a precision loss somewhere
'''
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MODULO = (pow(10,9) + 7)
        # values are getting stupidly huge -> exert caution here
        # wow the library function works ( I guess we'll just leverage that instead )
        ans = (int)(comb((n + k) - 1,k) % MODULO)
        return (ans)
