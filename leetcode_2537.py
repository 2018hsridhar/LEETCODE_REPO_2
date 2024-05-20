'''
2537. Count the Number of Good Subarrays
URL := https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

Complexity : Single Pass, Linear Scan, Single Pass, Counting, HashMaps, Thresholding

Cases :
(A)
(B)
(C)
(D)
(E)

Close but NOT exactly there!

Commit Message :
    # What are the constraints of my problems?
    # What are my problem's dimensions?
    # crossed once : if keeps incr -> pairCount will not adjust again
    # ahh pairs based : it's different here ( this is index counting )
    # ooh ; accumulating counts

'''
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        numGoodSubArr = 0
        leftPtr = 0
        # Very Javascript-inspired syntax going on here Python3 ( and maybe 2 )?
        numFreq = {}
        pairCount = 0
        for rightPtr, rightVal in enumerate(nums):
            if rightVal not in numFreq:
                # <hm-name>[key] = value syntax style                
                numFreq[rightVal] = 0
            numFreq[rightVal] += 1
            prevValPairCount = self.snn(numFreq[rightVal] - 1)
            curValPairCount = self.snn(numFreq[rightVal])
            pairCount += (curValPairCount - prevValPairCount)
            # first time hitting a valid case : not future times
            # left closure : hit a valid case ( multiple valid cases too )?
            # loop closure conditions sliding windows tricky
            while(pairCount >= k and leftPtr <= rightPtr):
                numGoodSubArr += len(nums) - rightPtr
                leftVal = nums[leftPtr]
                curVal = numFreq[leftVal]
                nextVal = numFreq[leftVal] - 1
                curLeftValPairCount = self.snn(curVal)
                nextLeftValPairCount = self.snn(nextVal)
                pairCount += (nextLeftValPairCount - curLeftValPairCount)
                numFreq[leftVal] = nextVal
                if(nextVal == 0):
                    # KeyError handling needed?
                    del numFreq[leftVal]
                leftPtr += 1
        numGoodSubArr
        return numGoodSubArr

    def snn(self, x:int) -> int:
        return 0 if x == 0 else int(((x - 1) * x) / 2)
