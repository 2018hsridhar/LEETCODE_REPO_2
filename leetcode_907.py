Intuition and Approach
Category : Array, Stack, Monotonic Stack, BUDP ( Bottom-up Dynamic Programming ), Iterative
See problem title

Complexity
Let N:=length(input)

Time complexity:
O(N)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
'''
907. Sum of Subarray Minimums
URL := https://leetcode.com/problems/sum-of-subarray-minimums/description/
'''
import math 

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = pow(10,9) + 7
        monoStack = []
        n = len(arr)
        ptr = len(arr) - 1
        memo = [-1 for idx in range(len(arr))]
        # monostack can never be 0 ( except for the base case ) 
        while(ptr >= 0):
            val = arr[ptr]
            record = [val,ptr]
            sumMinsFromIdx = 0
            nextPtr = ptr
            if(len(monoStack) == 0):
                monoStack.append(record)
                sumMinsFromIdx = val
            else:
                while(len(monoStack) > 0):
                    topRecord = monoStack[-1]
                    topVal = topRecord[0]
                    topPtr = topRecord[1]
                    # must obey monotonicity property
                    if(val > topVal):
                        break
                    elif(val <= topVal):
                        monoStack.pop()
                        nextPtr = topPtr
                        record[1] = nextPtr
            # broke out of stack
            record = [val, nextPtr]
            monoStack.append(record)
            followerPtr = nextPtr + 1
            window = (nextPtr - ptr + 1)
            sumMinsFromIdx = (val * window)
            if(followerPtr < n):
                sumMinsFromIdx += memo[followerPtr]
            memo[ptr] = sumMinsFromIdx
            ptr -= 1
        targetSum = sum(memo)  % modulo
        return targetSum
