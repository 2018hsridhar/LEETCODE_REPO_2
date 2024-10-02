Intuition and Approach
See problem title
Greedy, Sorting, Linear Scan, Consecutive Number Range Analysis

Complexity
Let N:=length(input)

Time complexity:
O(NlogN)

Space complexity:
O(1) ( explicit and implicit )

Code
'''
https://leetcode.com/problems/append-k-integers-with-minimal-sum/
2195. Append K Integers With Minimal Sum
'''
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        minSum = 0
        nums.sort()
        index = 0
        n = len(nums)
        prevEl = 0
        while(index < n):
            curEl = nums[index]
            delta = abs(curEl - prevEl)
            # colon style conditional logic exprs.
            if(delta <= 1):
                # handle duplicates
                prevEl = curEl
                index += 1
            elif(delta > 1):
                rangeWindow = (curEl - prevEl - 1)
                nextK = k - rangeWindow
                if(nextK > 0):
                    k = nextK
                    index += 1
                    minSum += self.snn(curEl - 1) - self.snn(prevEl)
                    prevEl = curEl
                elif(nextK <= 0):
                    maximalEl = prevEl + k
                    if(nextK == 0):
                        maximalEl = curEl - 1
                    minSum += self.snn(maximalEl) - self.snn(prevEl)
                    k = 0
                    break
        # last El case 
        if(k > 0):
            lastEl = nums[-1]
            maximalEl = lastEl + k
            minSum += self.snn(maximalEl) - self.snn(lastEl)
        return (int)(minSum)

    def snn(self, x:int) -> int:
        return 0.5 * x * (x+1)
