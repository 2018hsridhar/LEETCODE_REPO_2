'''
URL := https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/description/
3085. Minimum Deletions to Make String K-Special

Can get each let -> freq and then freq of freq, or duplicate(freqs ) too
26 letters max : reasonable bound to sigma

Complexity Analysis
Sigma = 26 ( size of langauge)
T = O(1) ( it's all sigma ) 
S = O(1) ( explicit ) O(1) ( implicit ) 

'''
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        minDel = float('inf')
        freqStore = dict()
        for let in word:
            if(let not in freqStore):
                freqStore[let] = 0
            freqStore[let] += 1
        records = []
        for let,letFreq in freqStore.items():
            record = [let,letFreq]
            records.append(record)    
        records.sort(key = lambda x : (x[1],x[0]))
        for [curLet,lowerFreq] in records:
            upperFreq = lowerFreq + k
            numFreqToDel = 0
            for rec in records:
                otherFreq = rec[1]
                if(otherFreq > upperFreq):
                    numFreqToDel += abs(otherFreq - upperFreq)
                elif(otherFreq < lowerFreq):
                    numFreqToDel += otherFreq
            minDel = min(minDel, numFreqToDel)
        return minDel
    
