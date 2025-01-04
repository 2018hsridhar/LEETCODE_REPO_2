'''
URL = https://leetcode.com/problems/count-the-number-of-fair-pairs/description/
2563. Count the Number of Fair Pairs

Complexity
Let N := length(input)
Time = O(NlgN)
Space = O(1) ( E and I ) 

It's a binary search question in the hiding
lower - nums(j) <= nums(i)
nums(i) <= upper - nums(j)
For each nums(i) - in sorted order - find the other number ( or value closest to it at least ) 


[0,0,1,2,3,4,523,243234,3902,239043] and so on 
             ^
             lower - 523(n_j) = soome value ( treat number as n_j)
             find n_i such that n_i >= said bound ( the leftmost one ) 



'''
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        # Avoid double count cases ( handle this later ) ?
        numPairs = 0
        for idx, num in enumerate(nums):
            lowerBound = lower - num
            upperBound = upper - num
            leftLowerCase = self.bSearchLower(nums,lowerBound)
            rightUpperCase = self.bSearchUpper(nums,upperBound)
            if(leftLowerCase != -1 and rightUpperCase != -1):
                # SMH this was the bug ( wrong var names dude ) 
                lowerInt = [0,rightUpperCase]
                upperInt = [leftLowerCase, n-1]
                ideal = self.merge(lowerInt,upperInt)
                adjLeft = max(ideal[0],idx + 1)
                ideal[0] = adjLeft
                if(ideal[0] <= ideal[1]):
                    window = ideal[1] - ideal[0] + 1
                    numPairs += window
        return numPairs    

    def merge(self, intOne:List[int], intTwo:List[int]) -> List[int]:
        leftBound = max(intOne[0],intTwo[0])
        rightBound = min(intOne[1],intTwo[1])
        interval = [leftBound,rightBound]
        return interval

    # n_j >= (lower - n_i) : how many valuies
    def bSearchLower(self, nums:List[int], target) -> int:
        targetIndex = float('inf')
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = (int)(0.5 * (low + high))
            candid = nums[mid]
            if(candid < target):
                low = mid + 1
            elif(candid >= target):
                targetIndex = min(targetIndex,mid)
                high = mid - 1
        if(targetIndex == float('inf')):
            targetIndex = -1
        return targetIndex

    # n_j <= (upper - n_i) : how many valuies
    def bSearchUpper(self, nums:List[int], target) -> int:
        targetIndex = -1
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = (int)(0.5 * (low + high))
            candid = nums[mid]
            if(candid > target):
                high = mid - 1
            elif(candid <= target):
                targetIndex = max(targetIndex,mid)
                low = mid + 1
        return targetIndex
