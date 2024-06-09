'''
2962. Count Subarrays Where Max Element Appears at Least K Times
URL := https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/

Category : Sliding Window, Frequency Counting, Hashmap, Two Pointers

Compelxity :
Let N := len(nums)
T = O(N)
S = O(N) ( E ) O(1) ( I )

Commit Log :
(A) LC problems helping to learn the standard library features of a programming language? 
(B) map() != dict()
(C) 30 mins solutioning -> was a bad bug
(D) HFT guy mentioned how LC really amkes you better at debugging skills when code isn't executing as epxected.

'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        csa = 0
        lPtr = 0
        rPtr = 0
        n = len(nums)
        numsFreq = dict()
        # get max el
        maxEl = self.getMaxEl(nums)
        while(rPtr < n):
            el = nums[rPtr]
            if(el not in numsFreq):
                numsFreq[el] = 0
            nextFreq = numsFreq[el] + 1
            numsFreq[el] = nextFreq
            # cond is exactly hit when nextFreq = k : acts as a guardian for the left in delta known
            if(el == maxEl and nextFreq == k):
                while(lPtr <= rPtr):
                    delta = (n - rPtr)
                    csa += delta
                    leftEl = nums[lPtr]
                    if(leftEl in numsFreq):
                        nextFreqLeft = numsFreq[leftEl] - 1
                        if(nextFreqLeft == 0):
                            del numsFreq[leftEl]
                        else:
                            numsFreq[leftEl] = nextFreqLeft
                        if(leftEl == maxEl and nextFreqLeft < k):
                            lPtr += 1
                            break
                    lPtr += 1
            rPtr += 1
        # done going to the right -> march on leftwards please
        while(lPtr < n and maxEl in numsFreq and numsFreq[maxEl] >= k):
            csa += 1
            leftEl = nums[lPtr]
            if(leftEl in numsFreq):
                nextFreq = numsFreq[leftEl] - 1
                if(nextFreq == 0):
                    del numsFreq[leftEl]
                else:
                    numsFreq[leftEl] = nextFreq
                if(leftEl == maxEl and nextFreq < k):
                    break
            lPtr += 1
        return csa
        
    # there's never two maxes : always one max in any given list of ordinal elements :-)
    def getMaxEl(self, nums:List[int]) -> int:
        curMax = nums[0]
        for val in nums:
            if(val > curMax):
                curMax = val
        return curMax
