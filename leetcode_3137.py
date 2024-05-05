'''
3137. Minimum Number of Operations to Make Word K-Periodic
URL := https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/description/

https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
Woah there's a lot of values to unpack here; we need to unpack dictionaries and abstractions in python3
'''
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        minOps = n
        periodicHits = dict()
        # int(possiblyFloat) more indicative of an explicit conversion ( versus floor(float))
        numberPrefixesToMake = int(n / k)
        for leftPtr in range(0,n-k+1,1):
            # Double equals numeric comparison in Py3
            if(leftPtr % k == 0):
                curPrefix = word[leftPtr:leftPtr + k]
                if curPrefix not in periodicHits:
                    periodicHits[curPrefix] = 0
                periodicHits[curPrefix] += 1
                minOps = min(minOps, numberPrefixesToMake - periodicHits[curPrefix] )
        return minOps
