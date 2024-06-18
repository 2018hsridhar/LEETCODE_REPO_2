'''
URL := https://leetcode.com/problems/frequency-tracker/description/
2671. Frequency Tracker

Complexity
Let N := #-values added
Let F := #-unique freqs ( make it to N @ worst )
Time = #-calls under execution
Space := O(N) ( E ) O(1) ( I ) 

15 mins to solutioning here
    -> please clean up this code though. It can be reformulated!
'''
class FrequencyTracker:

    def __init__(self):
        self.countVals = dict()
        self.countFreqs = dict()

    def add(self, number: int) -> None:
        if(number not in self.countVals):
            self.countVals[number] = 0
        curFreq = self.countVals[number]
        nextFreq = curFreq + 1
        self.countVals[number] = nextFreq
        if(curFreq > 0 and curFreq in self.countFreqs):
            if(self.countFreqs[curFreq] == 1):
                del self.countFreqs[curFreq]
            else:
                self.countFreqs[curFreq] -= 1
        if(nextFreq not in self.countFreqs):
            self.countFreqs[nextFreq] = 0
        self.countFreqs[nextFreq] += 1
        
    def deleteOne(self, number: int) -> None:
        if(number in self.countVals):
            # [1] Update the value count
            curFreqNum = self.countVals[number]
            nextFreqNum = (curFreqNum - 1)
            if(nextFreqNum == 0):
                del self.countVals[number]
            else:
                self.countVals[number] = nextFreqNum
            # [2] Update the frequency counts
            if(curFreqNum in self.countFreqs):
                if(self.countFreqs[curFreqNum] == 1):
                    del self.countFreqs[curFreqNum]
                else:
                    self.countFreqs[curFreqNum] -= 1
            if(nextFreqNum not in self.countFreqs):
                self.countFreqs[nextFreqNum] = 0
            self.countFreqs[nextFreqNum] += 1

    def hasFrequency(self, frequency: int) -> bool:
        # print(self.countFreqs)
        return (frequency in self.countFreqs)

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
