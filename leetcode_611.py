'''
611. Valid Triangle Number
URL := https://leetcode.com/problems/valid-triangle-number/description/

Complexity :
Let N := len(nums)
Time = O(N^2lgN)
Space = O(1) ( E & I ) 
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        numTriplets = 0
        nums.sort()
        n = len(nums)
        for i in range(0,len(nums),1):
            for j in range(i+1,len(nums),1):
                sideOne = nums[i]
                sideTwo = nums[j]
                # no value at this j either
                minToMeet = sideOne + sideTwo - 1
                # we must be equal to this value, at worst ( 2 + 3 > 4, but is = 5 )
                sideThreeRightIndex = self.bSearchRightIndex(nums,minToMeet)
                if(sideThreeRightIndex != -1 and sideThreeRightIndex != 1000000):
                    tripletIndexDelta = sideThreeRightIndex - j
                    if(tripletIndexDelta >= 0):
                        numTriplets += tripletIndexDelta
        return numTriplets
        
    def bSearchRightIndex(self, nums: List[int], minToMeet:int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        leftMostIdxHit = 1000000
        leftMostVal = -1
        while(low <= high):
            # gaaah no explicit int conversion
            mid = int((low + high) / 2)
            midVal = nums[mid]
            # ok we are to high of a value : 2 + 3 < 7 type of thing -> please decrease now
            if(midVal > minToMeet):
                high = mid - 1
            # we hit out value -> but, can we go ugh, more left ?
            elif(midVal == minToMeet):
                # print("Hit mid at idx = " + str(leftMostIdxHit))
                low = mid + 1
                # gaaah no math package .min() here
                if(midVal > leftMostVal):
                    leftMostVal = midVal
                    leftMostIdxHit = mid
                # is actually the right most in this case
                elif(midVal == leftMostVal):
                    leftMostVal = midVal
                    leftMostIdxHit = max(mid, leftMostIdxHit)
            elif(midVal < minToMeet):
                # hey we are still less, but ... we need to consider going up
                if(midVal >= leftMostVal):
                    leftMostVal = midVal
                    leftMostIdxHit = mid
                low = mid + 1
        # Return outside function body? gaaah
        return leftMostIdxHit
