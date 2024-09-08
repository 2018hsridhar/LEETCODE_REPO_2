'''
URL := https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/solutions/5757369/python3-o-n-time-o-n-space-solution-checking-parity-of-each-consecutive-element-with-greedy-choice/
3216. Lexicographically Smallest String After a Swap
'''
Complexity
Let N:= length of the input string

Time complexity:

O(N)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
class Solution:

    def meetsParityReq(self,curEl:int, nextEl:int) -> bool:
        return ((curEl % 2 == 1 and nextEl % 2 == 1) or (curEl % 2 == 0 and nextEl % 2 == 0))

    def getSmallestString(self, s: str) -> str:
        smallestStr = []
        curPtr = 0
        while(curPtr < len(s) - 1):
            curEl = (s[curPtr])
            nextEl = (s[curPtr + 1])
            curVal = (int)(curEl)
            nextVal = (int)(nextEl)
            if(curVal > nextVal and self.meetsParityReq(curVal,nextVal)):
                smallestStr.append(nextEl)
                smallestStr.append(curEl)
                curPtr += 2
                break
            smallestStr.append(curEl)
            curPtr += 1
        while(curPtr < len(s)):
            smallestStr.append(s[curPtr])
            curPtr += 1
        return "".join(smallestStr)$$O(N)$$ ( Explicit )
