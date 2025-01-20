'''
URL := https://leetcode.com/problems/3sum-with-multiplicity/description/
923. 3Sum With Multiplicity

Clarification Questions
- can have 0 values
- can have repetition
- reasonably bounded inputs

Complexity
N = len(input)
T = O(pow(N,2))
S = O(N) ( E ) O(1) ( I ) 

Categories : Two Pointers, Counting, Hashmaps, Sorting, Number Theory, Math
30 ish mins on problem and solutioned -> on the end of a tougher medium here ( stinking edge cas scenario triples 0's )
'''

# most implicit import statement ever?
import math

class Solution:

    # 2 => 1 ( 2 * 1/2) : 3 => 3 ( 3 * (2)/2)
    def snn(self, x:int) -> int:
        ans = (int)(0.5 * x * (x-1))
        return ans

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        numThreePairs = 0
        MODULO = (int)(math.pow(10,9) + 7)
        valFreq = dict()
        for val in arr:
            if(val not in valFreq):
                valFreq[val] = 0
            valFreq[val] += 1
        records = []
        for val, freqVal in valFreq.items():
            record = [val,freqVal]
            records.append(record)
        records.sort(key = lambda x : (x[0],x[1]))
        print(records)
        # return -1
        n = len(records)
        # delta Adjust for frequency reasons
        deltaAdjust = 1
        for outerPtr, outerRecord in enumerate(records):
            outerVal = outerRecord[0]
            outerFreq = outerRecord[1]
            twoSumTarget = target - outerVal
            # ahhh we need the frequency of the outer value too
            if(twoSumTarget >= 0):
                leftPtr = outerPtr
                rightPtr = n-1
                while(leftPtr <= rightPtr):
                    leftVal = records[leftPtr][0]
                    rightVal = records[rightPtr][0]
                    leftFreq = records[leftPtr][1]
                    rightFreq = records[rightPtr][1]
                    curVal = leftVal + rightVal
                    if(curVal < twoSumTarget):
                        leftPtr += 1
                    elif(curVal > twoSumTarget):
                        rightPtr -= 1
                    elif(curVal == twoSumTarget):
                        # no TLE here
                        # some edge case here ( resolve it later ) 
                        curNumPairs = 0
                        if(leftVal == rightVal):
                            curNumPairs = (self.snn(leftFreq) * outerFreq)
                            if(leftVal == outerVal):
                                # this could be a real special case WOAH
                                # it's a triple case considered once only
                                # non-intuitive here
                                # 5 0 : 6+3+1
                                # 7 0 : 15+10+6+3+1 = 35
                                # curNumPairs = self.snn(leftFreq)
                                delta = leftFreq - 2
                                # SMH really special test case here BUT passed it!!
                                curNumPairs = (int)((1/6)*(delta * (delta+1)*(delta+2)))
                        else:
                            # say 1+5 = 6 : 1 appear 3 times, 6 2 times. 
                            # (1,6) (1,6) ... 3 times each :-)
                            if(leftVal == outerVal):
                                curNumPairs = ((self.snn(leftFreq) * rightFreq))
                            else:
                                curNumPairs = ((leftFreq * rightFreq) * outerFreq)
                        numThreePairs += curNumPairs
                        leftPtr += 1
        numThreePairs = numThreePairs % MODULO
        return numThreePairs
