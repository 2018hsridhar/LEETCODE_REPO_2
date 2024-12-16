'''
URL := https://leetcode.com/problems/smallest-number-in-infinite-set/description/
2336. Smallest Number in Infinite Set

Intuition and Approach :
Leverage a Priority Queue ( with order ) - tells us elements added back into the infinite set
PopSmallest() always a removal operation
Track a running currentMinimum and always focus here :
    Bound : [1,max times ( pop/addback )]
 
Complexity
O := #-operations total
N := #-popSmallest Operations
T = O(O)
S = O(N) ( Explicit ) O(1) ( Implicit )

Track the infinite set min : not the min of the heap ( huge difference ) 
infinite min is always heap size at one type of thing

'''
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        infiniteRootVal = 1
        self.seenSetValues = set()
        self.minValHeap = [infiniteRootVal]
        self.infiniteMin = 1

    def popSmallest(self) -> int:
        smallestEl = -1
        if(len(self.minValHeap) > 0):
            smallestEl = heapq.heappop(self.minValHeap)
            if(smallestEl in self.seenSetValues):
                self.seenSetValues.remove(smallestEl)
            if(len(self.minValHeap) == 0):
                nextSmallestEl = smallestEl + 1
                self.infiniteMin = self.infiniteMin + 1
                heapq.heappush(self.minValHeap, nextSmallestEl)
        return smallestEl

    def addBack(self, num: int) -> None:
        # edge case : if we add a value that is way way out!
        if(num not in self.seenSetValues):
            curMinHeapVal = self.minValHeap[0]
            if(num < self.infiniteMin):
                heapq.heappush(self.minValHeap,num)
                self.seenSetValues.add(num)
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
