'''
2090. K Radius Subarray Averages
URL := https://leetcode.com/problems/k-radius-subarray-averages/description/

Category : Sliding Window, Linear Scan, Single Pass

Complexity :
Let N := len(nums)
T = O(N)
S = O(N) ( E ) O(1) ( I ) 

Note : k = 0 is permissible
15 mins
'''
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Base case handling ( no divBy0 err ) 
        # if(k == 0):
            # return nums
        myAverages = [-1 for i in range(len(nums))]
        runningSum = 0
        windowSize = 2*k + 1
        for rightIndex in range(len(nums)):
            runningSum += nums[rightIndex]
            if(0 <= (rightIndex - k - k) and rightIndex < len(nums)):
                # decrease the left -> right will increase on the next step
                leftBound = rightIndex - k - k
                centerIndex = rightIndex - k
                truncSum = runningSum if (k == 0) else int(runningSum / windowSize )
                myAverages[centerIndex] = truncSum
                runningSum -= nums[leftBound]
        return myAverages
