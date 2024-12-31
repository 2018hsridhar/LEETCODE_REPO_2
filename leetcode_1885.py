'''
1885. Count Pairs in Two Arrays
URL := https://leetcode.com/problems/count-pairs-in-two-arrays/

N = len(input)
T = O(nlgn)
S = O(n) ( explicit ) O(1) ( implicit ) 
'''
class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        deltas = [(nums1[idx] - nums2[idx]) for idx in range(n)]
        deltas.sort()
        print(deltas)
        numSatisfyPairs = 0
        for index,delta in enumerate(deltas):
            if(delta <= 0):
                targetIndex = -1
                bestVal = abs(delta) + 1
                low = 0
                high = n - 1
                while(low <= high):
                    mid = (int)(0.5 * (low + high))
                    candid = deltas[mid]
                    if(candid >= bestVal):
                        targetIndex = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                if(targetIndex != -1):
                    remLen = (n - targetIndex)
                    numSatisfyPairs += remLen
            elif(delta > 0):
                remLen = (n - 1 - index)
                numSatisfyPairs += remLen
        return numSatisfyPairs
        
