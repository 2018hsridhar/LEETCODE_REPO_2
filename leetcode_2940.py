'''
2940. Find Building Where Alice and Bob Can Meet
URL := https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/description/

Approach : Sorting, Monotonic Stack, Greedy, Heap, Priority Queue
15 minutes spent on the problem here
Almost solutioned :-)

'''

import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # 1. Build the queries differently - sorted order with ++ wrapper metadata 
        # close : 949/953 -> some subtle bug -> go remediate it!
        leftmostBuildings = [-1 for idx in range(len(queries))]
        modifQueries = []
        for index,query in enumerate(queries):
            left = query[0]
            right = query[1]
            lesser = min(query[0],query[1])
            greater = max(query[0],query[1])
            heightOne = heights[lesser]
            heightTwo = heights[greater]
            maxHeight = max(heightOne,heightTwo)
            # tricking the input in some cases
            if((heightOne == heightTwo and left != right) or heights[lesser] > heights[greater]):
                maxHeight = maxHeight + 1
            record = [lesser,greater,index,maxHeight]
            modifQueries.append(record)
        modifQueries.sort(key = lambda x : (x[1],-1 * x[2],x[0],x[3]))
        queryHeap = []
        # close, but don't psuh sorted records -> it's complex
        # it's queuing into that heap SMHHH
        # 2. Meat of the algo => monotonic stack
        # While we go through indexes, check how many we supersede
        # For each query, we ask ourself which building for both heights came latest
        # E.g. {4,5} -> 7 versus {6,5} => it's 7
        # can be same building
        # it may be just a heap -> not even a monoStack is fully needed here
        recordPtr = 0
        for heightIndex,height in enumerate(heights):
            while(recordPtr < len(modifQueries)):
                curRecord = modifQueries[recordPtr]
                if(curRecord[1] <= heightIndex):
                    otherRec = [curRecord[3],curRecord[2],curRecord[0],curRecord[1]]
                    heapq.heappush(queryHeap,otherRec)
                    recordPtr += 1
                else:
                    break
            # Dumb same building case -> NOP effectively
            # oh - movement iff H(I) < H(J) AND I < J : j can stay in current position too!
            # take note of that
            # a and b - same building - done
            # a and b - diff buildings of same height - both have to move elsewhere
            # ohhh!
            while(len(queryHeap) > 0):
                bestRec = queryHeap[0]
                if(bestRec[3] <= heightIndex):
                    if(bestRec[0] <= height):
                        # if both are different heights, operate -> else, carry on
                        # left = bestRec[2]
                        # right = bestRec[3]
                        # heightOne = heights[bestRec[2]]
                        # heightTwo = heights[bestRec[3]]
                        # SMH dumb edge case scnearios come back later
                        # if(heightOne != heightTwo or (heightOne == heightTwo and left == right)):
                        queryIdx = bestRec[1]
                        leftmostBuildings[queryIdx] = heightIndex
                        heapq.heappop(queryHeap)
                        # else:
                            # break
                    else:
                        break
                else:
                    break
        return leftmostBuildings
        
