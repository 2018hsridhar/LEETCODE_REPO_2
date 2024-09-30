Intuition and Approach
See problem title
Category : Iterative, Logs, Binary Search, Textual Substitution

Complexity
N:=max radix length to hit

Time complexity:
O(N)

Space complexity:
O(1) ( Explicit and Implicit )

Code
'''
2802. Find The K-th Lucky Number
URL := https://leetcode.com/problems/find-the-k-th-lucky-number/

'''
class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        finalNum = 0
        # # offset 0 index
        k -= 1
        [radixLen,finalK] = self.getRadixLength(k)
        # print(self.getBinaryRep(190,10))
        binaryRep = self.getBinaryRep(finalK,radixLen)
        finalResult = []
        for char in binaryRep:
            if(char == '1'):
                finalResult.append('7')
            elif(char == '0'):
                finalResult.append('4')
            # close but not there
        finalNum = ("".join(finalResult))
        return finalNum
    
    def getRadixLength(self, k:int) -> List[int]:
        radixLen = 0
        step = 2
        while(k >= 0):
            nextK = k - step
            if(nextK < 0):
                break
            radixLen += 1
            step = step * 2
            k = nextK
        return [radixLen + 1,k]
    
    def getBinaryRep(self, k:int, radixLen:int) -> str:
        numCharsStr = 0
        binRep = []
        while(k > 1):
            rem = k % 2 
            binRep.append((str)(rem))
            k = (int)(k/2)
            numCharsStr += 1
        binRep.append((str)(k))
        binRep.reverse()
        numCharsStr += 1
        zeroPrefixLen = radixLen - numCharsStr
        zeroPrefix = "0" * zeroPrefixLen
        finalRep = zeroPrefix + "".join(binRep)
        return finalRep
