Complexity
Let N:= length of the input list

Time complexity:
O(N)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
class Solution:
    def subsequenceCount(self, nums: List[int]) -> int:
        n = len(nums)
        evenOddCount = [[0 for i in range(n)],[0 for i in range(n)]]
        evenIdx = 0
        oddIdx = 1
        numberRunEven = 0
        numberRunOdd = 0
        subSeqCount = 0
        modulo = pow(10,9) + 7
        for readPtr in range(len(nums) - 1, -1,-1):
            curOddSeqCount = 0
            curEvenSeqCount = 0
            num = nums[readPtr]
            if(num % 2 == 1):
                curOddSeqCount += 1
                curEvenSeqCount += numberRunOdd
                curOddSeqCount += numberRunEven
            elif(num % 2 == 0):
                curEvenSeqCount += 1
                curEvenSeqCount += numberRunEven
                curOddSeqCount += numberRunOdd
            evenOddCount[evenIdx][readPtr] = curEvenSeqCount
            evenOddCount[oddIdx][readPtr] = curOddSeqCount
            evenOddCount[evenIdx][readPtr] %= modulo
            evenOddCount[oddIdx][readPtr] %= modulo
            numberRunEven += evenOddCount[evenIdx][readPtr]
            numberRunOdd += evenOddCount[oddIdx][readPtr]
            subSeqCount += evenOddCount[oddIdx][readPtr]
        return subSeqCount % modulo
        
