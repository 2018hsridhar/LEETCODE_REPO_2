'''
URL := https://leetcode.com/problems/count-anagrams/description/
2514. Count Anagrams

Problem type : combinatorial, 
COMPLEXITY
W = #-WORDS
L = LENGTH(LONGEST_WORD)
TIME = O(W*L)
SPACE = O(1) ( E ) O(1) ( I ) 
'''

# Leverage MATHEMATICAL libraries.
'''
Case 1 : "b okzojaporykbmq tybq jjuowpp" => PASSING
Case 2 : "b okzojaporykbmq tybq zrztwlolvcyumcsq jjuowpp" => FAILING
Case 3 : "tybq zrztwlolvcyumcsq jjuowpp" => FAILING


value coudl be getting too huge
'''
import math

class Solution:
    def countAnagrams(self, s: str) -> int:
        SPACE = ' '
        tokens = s.split(SPACE)
        MODULO = pow(10,9) + 7
        runProd = 1
        for token in tokens:
            numDistinctCounts = self.getDistinctCount(token, MODULO)
            runProd = runProd * ( numDistinctCounts % MODULO )
            # runProd = runProd % MODULO
        anagramCount = runProd % MODULO
        return (int)(anagramCount)
    
    # too : 3 unique combinations : 6 C 2
    # It will pass, but it's a weird trick
    # Or ... can we divide later? Hmmm
    def getDistinctCount(self, token: str, MOD: int) -> int:
        freq = Counter(token)
        n = len(token)
        numerator = math.factorial(n) % MOD

        # Compute denominator under modulo using modular inverses
        denom = 1
        for f in freq.values():
            denom = (denom * math.factorial(f)) % MOD

        # Use modular inverse for division
        denom_inv = pow(denom, MOD - 2, MOD)
        distinctCount = (numerator * denom_inv) % MOD
        return distinctCount
