'''
3228. Maximum Number of Operations to Move Ones to the End
URL := https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/

Complexity
Time = O(N)
Space = O(N) ( E ) O(1) ( I ) 
'''
class Solution:
    def maxOperations(self, s: str) -> int:
        oneRunSum = 0
        uniqSums = set()
        for letter in s:
            if(letter == '1'):
                oneRunSum += 1
            elif(letter == '0'):
                uniqSums.add(oneRunSum)
        maxNumOps = sum(list(uniqSums))
        return maxNumOps
        
