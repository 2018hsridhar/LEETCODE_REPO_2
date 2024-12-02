Python3 Linear Time, Constant Space Iterative Solution Leveraging Zipper Merge and Greedy Approach

Hari Sridhar
100 Days Badge 2022
29
0
a few seconds ago
Python3
Two Pointers
String
Intuition and Approach
Categories : Greedy, Single Pass, Linear Scan, Math, Character Comparison, Iterative
Leverage zipper merge ideas

Complexity
M := len(s1), N := len(s2), P := max(M,N)

Time complexity:
O(P)

Space complexity:
O(1) ( E and I )

Code
'''
URL := https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/description/
2825. Make String a Subsequence Using Cyclic Increments

Scenarios :
(A) "aa","a" -> T
(B) "zz","a" -> T
(C) "zz","b" -> F
(D) "az","ba" -> T
(E) "abc","cba" -> F
'''
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m = len(str1)
        n = len(str2)
        ptr1 = 0
        ptr2 = 0
        base = 'a'
        while(ptr1 < m and ptr2 < n):
            letOne = str1[ptr1]
            letTwo = str2[ptr2]
            nextOrdPos = (ord(letOne) - ord(base) + 1) % 26
            incrLet = chr(nextOrdPos + ord(base))
            if(letOne == letTwo or incrLet == letTwo):
                ptr2 += 1
            ptr1 += 1
        canMake = (ptr2 == n)
        return canMake
