'''
3325. Count Substrings With K-Frequency Characters I
URL := https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/description/

Categories : Sliding Window, Hashmap, Linear Scan

N = len(input)
Time = O(N)
Space = O(1) ( E ) ( I ) 
'''
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        countMatchStrings = 0
        n = len(s)
        sigma = 26
        freqMap = [0 for idx in range(sigma)]
        lPtr = 0
        BASE = 'a'
        for rPtr, val in enumerate(s):
            valPos = ord(val) - ord(BASE)
            nextFreq = freqMap[valPos] + 1
            freqMap[valPos] = nextFreq
            # Nested loop : close the sliding window :-) !
            while(nextFreq >= k and lPtr <= rPtr):
                numSuffixes = (n - rPtr)
                countMatchStrings += numSuffixes
                leftVal = s[lPtr]
                leftPos = ord(leftVal) - ord(BASE)
                nextFreq = freqMap[leftPos] - 1
                freqMap[leftPos] = nextFreq
                lPtr += 1
                nextFreq = freqMap[valPos]
        return countMatchStrings
