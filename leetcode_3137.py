'''
3137. Minimum Number of Operations to Make Word K-Periodic
URL := https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/description/

https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops

'''
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        minOps = n
        periodicHits = dict()
        for leftPtr in range(len(word)):
            # Double equals numeric comparison in Py3
            if(leftPtr % k == 0):
                rightPtr = leftPtr + k
                if(rightPtr <= n):
                    curPrefix = word[leftPtr:rightPtr]
                    if curPrefix not in periodicHits:
                        periodicHits[curPrefix] = 0
                    periodicHits[curPrefix] += 1
        numberPrefixesToMake = floor(n / k)
        # woah there's a lot of values to unpack here; we need to unpack dictionaries and abstractions in python3
        for prefix, prefixIdxHits in periodicHits.items():
            minOps = min(minOps, numberPrefixesToMake - prefixIdxHits )
        return minOps
        
