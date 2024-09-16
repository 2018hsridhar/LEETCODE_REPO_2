URL := https://leetcode.com/problems/neighboring-bitwise-xor/description/
2683. Neighboring Bitwise XOR

Intuition and Approach
The base array must start with either a one or a zero, so let's test out just two combinations :
(A) Case of first el = 1
(B) Case of first el = 0
And see if we can recreate the derived array from said base

Complexity
Let N:= length of the input list

Time complexity:
O(N)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        oneStatus = self.checkStatus(1,derived)
        zeroStatus = self.checkStatus(0,derived)
        return (oneStatus or zeroStatus)
    
    def checkStatus(self, runXor: int, derived: List[int]) -> bool:
        base = [runXor]
        for index in range(len(derived)-1):
            operand = derived[index]
            nextVal = runXor ^ operand
            base.append(nextVal)
            runXor = nextVal
        finalEl = base[-1]
        firstEl = base[0]
        meetsDerived = ((firstEl ^ finalEl) == derived[-1])
        return meetsDerived
