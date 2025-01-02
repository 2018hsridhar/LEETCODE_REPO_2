'''
2098. Subsequence of Size K With the Largest Even Sum
URL := https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/description/

k is a known
odds : k is one odd -> must take largest odd
once even -> pairwise add ( eevn and odds ) 
Any order doable

Categories : Sort, Greedy, Linear Scans
T = NlgN
S = N ( Explicit ) 1 ( Implicit ) 
'''
class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        evens = []
        odds = []
        for x in nums:
            if(x % 2 == 0):
                evens.append(x)
            else:
                odds.append(x)
        evens.sort(key = lambda x : (-1 * x))
        odds.sort(key = lambda x : (-1 * x))
        bestLES = 0
        # oh wait - use an even, not an odd. Otherway around :-P
        if(k % 2 == 1):
            if(len(evens) > 0):
                bestLES += evens[0]
                k -= 1
                del evens[0]
            else:
                # unsolveable
                return -1
        e2 = [(evens[i] + evens[i+1]) for i in range(0,len(evens) - 1,2)]
        o2 = [(odds[i] + odds[i+1]) for i in range(0,len(odds) - 1,2)]
        ePtr = 0
        oPtr = 0
        while(k > 0 and ePtr < len(e2) and oPtr < len(o2)):
            eVal = e2[ePtr]
            oVal = o2[oPtr]
            if(eVal >= oVal):
                bestLES += eVal
                ePtr += 1
            else:
                bestLES += oVal
                oPtr += 1
            k -= 2
        while(k > 0 and ePtr < len(e2)):
            eVal = e2[ePtr]
            bestLES += eVal
            ePtr += 1
            k -= 2
        while(k > 0 and oPtr < len(o2)):
            oVal = o2[oPtr]
            bestLES += oVal
            oPtr += 1
            k -= 2
        # we can have a sum of 0, so chek if we did an actual deletion SMH
        if(k > 0):
            bestLES = -1
        return bestLES

        



        
