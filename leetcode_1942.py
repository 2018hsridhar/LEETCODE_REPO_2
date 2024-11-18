'''
URL := https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/
1942. The Number of the Smallest Unoccupied Chair

Compelxity
Time = O(NlgN)
S = O(N) ( Explicit ) O(1) ( Implicit ) 

Categories : Sort, Ordering, Heaps, Priority Queues, Greedy
'''

import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        finalChairNumber = -1
        records = [[time[0],time[1],idx] for idx,time in enumerate(times)]
        records.sort(key = lambda x : (x[0],x[1],x[2]))
        # who is current sitting ( this will be a heap ) 
        availChairs = [0]
        currentSeaters = []
        for rPtr in range(len(records)):
            record = records[rPtr]
            [sTime,eTime,personId] = record
            # [1] Evict current seaters : free up available seats
            while(len(currentSeaters) > 0):
                earliestToLeave = heapq.heappop(currentSeaters)
                (eTime_early,seat_early) = earliestToLeave
                # person X leaves, person Y arrives ( at the same time ) 
                if(eTime_early > sTime):
                    heapq.heappush(currentSeaters,earliestToLeave)
                    break
                heapq.heappush(availChairs,seat_early)
            # [2] Get best seat from most up-to-date seat list
            bestSeat = heapq.heappop(availChairs)
            if(len(availChairs) == 0):
                heapq.heappush(availChairs,bestSeat + 1)
            # [2.1] Refresh heap of current seaters
            nextSeater = (eTime,bestSeat)
            heapq.heappush(currentSeaters,nextSeater)
            # [3] Check personId = targetFriend : if so, early terminate
            if(personId == targetFriend):
                finalChairNumber = bestSeat
                break
        return finalChairNumber
        
