'''
URL := https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
1864. Minimum Number of Swaps to Make the Binary String Alternating

Complexity
T = O(N)
S = O(1) ( Explicit )
S = O(1) ( Implicit ) 
'''
class Solution:
    def minSwaps(self, s: str) -> int:
        minSwps = float('inf')
        # Why is writing good method names a skill?
        caseOneCounts = self.getCaseCount(s,'0')
        caseTwoCounts = self.getCaseCount(s,'1')
        if(caseOneCounts[0] == caseOneCounts[1]):
            minSwps = min(minSwps,caseOneCounts[0])
        if(caseTwoCounts[0] == caseTwoCounts[1]):
            minSwps = min(minSwps,caseTwoCounts[0])
        if(minSwps == float('inf')):
            minSwps = -1
        return minSwps
        
    def getCaseCount(self, binaryStr:str, trgtLet:str) -> List[int]:
        zeroCount = 0
        oneCount = 0
        for letter in binaryStr:
            if(letter != trgtLet):
                if(letter == '0'):
                    zeroCount += 1
                elif(letter == '1'):
                    oneCount += 1
            if(trgtLet == '0'):
                trgtLet = '1'
            elif(trgtLet == '1'):
                trgtLet = '0'
        caseAns = [zeroCount, oneCount]
        return caseAns
