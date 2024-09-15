'''
URL := https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/description/
3125. Maximum Number That Makes Result of Bitwise AND Zero

'''
Intuition and Approach
Leverage the fact that we care when the MSB - most significant bit - goes to 0. E.g. given a value such as n = 7 ( bitwise expression of 111 ), we want top hit a target value of x = 3 ( 011 ). Since n = 7 has a radix of 3, we evaluate to value of 4 ( 100 ) and subtract one. Set up pre-algebra esque equations using log(base2) of our value and then power expressions for the most optimal x

Complexity
Time complexity:
O(1)

Space complexity:
O(1) ( Explicit and Implicit )

Code
import math

class Solution:
    def maxNumber(self, n: int) -> int:
        return (pow(2,math.floor(math.log2(n))) - 1)
