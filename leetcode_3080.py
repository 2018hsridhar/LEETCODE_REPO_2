'''
URL := https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/description/
3080. Mark Elements on Array by Performing Queries

Intuition and Approach : Heaps, Priority Queues, Sorting, Sets, Enumeration

Complexity
N := len(nums)
T = O(N)
S = O(N) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        m = len(queries)
        n = len(nums)
        answer = [-1 for idx in range(m)]
        minHeap = []
        unmarkedElSum = sum(nums)
        visitedIndices = set()
        for idx, val in enumerate(nums):
            record = [val,idx]
            heapq.heappush(minHeap, record)
        for ansIndex, [index,k] in enumerate(queries):
            if(index not in visitedIndices):
                visitedIndices.add(index)
                unmarkedElSum -= nums[index]
            while(len(minHeap) > 0 and k > 0):
                [minEl,minIndex] = heapq.heappop(minHeap)
                if(minIndex not in visitedIndices):
                    visitedIndices.add(minIndex)
                    k -= 1
                    unmarkedElSum -= minEl
            answer[ansIndex] = unmarkedElSum
        return answer

        
