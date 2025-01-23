'''
URL := https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/
2302. Count Subarrays With Score Less Than K

Complexity
N = len(input)
Time = O(NlgN)
Space = O(N) ( E ) O(1) ( I ) 

Intuition 
- Leverage binary search and prefix sums
'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        subArrayCount = 0
        n = len(nums)
        prefixSums = [0 for ix in range(n)]
        runSum = 0
        for index,num in enumerate(nums):
            runSum += num
            prefixSums[index] = runSum
        # Meat of the algorithm
        # Current position = an index -> how far back left can we go each time?
        for index,num in enumerate(nums):
            low = 0
            high = index
            numValidSubArrays = 0
            while(low <= high):
                # let mid be out leftmost index value
                mid = (int)((low+high)/2)
                subArraySum = prefixSums[index]
                if(mid-1 >= 0):
                    prefixSumLeft = prefixSums[mid-1]
                    subArraySum -= prefixSumLeft
                window = (index - mid) + 1
                subArrProd = subArraySum * window
                if(subArrProd >= k):
                    low = mid + 1
                elif(subArrProd < k):
                    high = mid - 1
                    numValidSubArrays = max(numValidSubArrays, window)
            subArrayCount += numValidSubArrays
        return subArrayCount


