Intution and Approach :
Problem structure is similar to that of A->B->C longest chains
Get the barcods with highest frequencies, and sort by their frequencies
Create multiple SLLs and return the output

Complexity
Let N:= #-of barcodes

Time complexity:
O(N)

Space complexity:
O(N) ( E )
O(1) ( I )

Code
'''
URL := https://leetcode.com/problems/distant-barcodes/description/
1054. Distant Barcodes
'''
import math 

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        maxFreq = 1
        codeFreq = dict()
        for code in barcodes:
            if code not in codeFreq:
                codeFreq[code] = 0
            nextFreq = codeFreq[code] + 1
            maxFreq = max(maxFreq,nextFreq)
            codeFreq[code] = nextFreq
        sourceRecords = []
        for val,freq in codeFreq.items():
            record = [val,freq]
            sourceRecords.append(record)
        sourceRecords.sort(key = lambda x : (-1 * x[1],x[0]))
        listsToAppend = [[] for x in range(maxFreq)]
        readPtr = 0
        writePtr = 0
        numLists = len(listsToAppend)
        for readPtr, sourceRecord in enumerate(sourceRecords):
            valToWrite = sourceRecord[0]
            valFreq = sourceRecord[1]
            for iters in range(valFreq):
                listsToAppend[writePtr].append(valToWrite)
                writePtr = (writePtr + 1 ) % numLists
        flattened_list = [item for sublist in listsToAppend for item in sublist]
        return flattened_list
