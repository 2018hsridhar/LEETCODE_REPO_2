'''
2064. Minimized Maximum of Products Distributed to Any Store
URL := https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/

Complexity
Let N := #-bins
Time := O(NlgN)
Space := O(N) ( E ) O(1) ( I )

Category : Heaps, Priority Queue, Sorting ( In-Place ), Iterative, Simulation

'''
import heapq

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
        # better to just make an empty heap and use heappush(...) and heappop(...) methods from the `heappq` module
        # Python3 makes working with minHeaps and maxHeaps a PITA
        # always use final state -> not init state
        # final state ( first ) init state ( second ) 
        heap = []
        for val in quantities:
            heapq.heappush(heap, [val * -1, val * -1, 1])
        # heapq.heapify(quantities) # for a maxheap!!
        # woah we heapify the list -> interesting
        # nextFrequency -> pidgeonhole principle -> for our binning strategy
        step = len(quantities)
        while(step < n):
            # pop from maxheap
            curTuple = heapq.heappop(heap)
            maxVal = -1 * curTuple[1]
            curFreq = curTuple[2]
            nextFreq = curFreq + 1
            nextVal = maxVal / nextFreq
            if(maxVal % nextFreq != 0):
                # take ceil -> the worst value
                heapq.heappush(heap, [-1 * int(ceil(nextVal)), -1 * maxVal, nextFreq])
            else:
                heapq.heappush(heap, [-1 * int(nextVal), -1 * maxVal, nextFreq])
            step += 1
        minMaxEl = heapq.heappop(heap)
        minMax = minMaxEl[0] * -1
        return int(minMax)
        
