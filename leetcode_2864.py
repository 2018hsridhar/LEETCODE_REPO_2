'''
URL := https://leetcode.com/problems/maximum-odd-binary-number/description/
2864. Maximum Odd Binary Number

'''
Intuition and Approach
See title

Complexity
Let N := #-characters in the input string

Time complexity:
O(N)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        oneCount = 0
        zeroCount = 0
        for char in s:
            if(char == '1'):
                oneCount += 1
            else:
                zeroCount += 1
        oneCount -= 1
        zeroPart = "0" * zeroCount
        onePart = "1" * oneCount
        resultStr = "".join([onePart, zeroPart,"1"])
        return resultStr
        
