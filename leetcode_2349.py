'''
2349. Design a Number Container System
URL := https://leetcode.com/problems/design-a-number-container-system/description/

Categories : Hashmap, Heap, One Pass

Map one : index -> number
Map two : number -> minHeap ( index ) 
on calls to find, iterative throug ha numbers heap. If min is in mapOne, it's valid. Else, keep evicting until
a. a valid min hit OR 
b. evict all entries -> ret -1

Complexity
N := #-values inserted ( can be case all indices own unique value worst case )
Time = O(N)
Space = O(N) ( E ) O(1) ( I ) 

'''

import heapq

class NumberContainers:

    def __init__(self):
        self.indexVals = dict()
        self.valueHeaps = dict()

    def change(self, index: int, number: int) -> None:
        # Update map one : index -> val 
        self.indexVals[index] = number
        # update map 2 : vals -> minHeaps
        if(number not in self.valueHeaps):
            self.valueHeaps[number] = []
        heapq.heappush(self.valueHeaps[number], index)

    def find(self, number: int) -> int:
        smallestIdx = -1
        if(number not in self.valueHeaps):
            return -1
        else:
            curMinHeap = self.valueHeaps[number]
            while(len(curMinHeap) > 0):
                curMinIdx = heapq.heappop(curMinHeap)
                curMinVal = self.indexVals[curMinIdx]
                if(curMinVal == number):
                    smallestIdx = curMinIdx
                    heapq.heappush(curMinHeap, curMinIdx)
                    self.valueHeaps[number] = curMinHeap
                    break
        return smallestIdx

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
