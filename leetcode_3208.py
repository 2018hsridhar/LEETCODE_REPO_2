Python Linear Time, Space Solution Iterative Using Stack and Even-Odd Parity

Hari Sridhar
100 Days Badge 2022
29
0
a few seconds ago
Python3
Array
Sliding Window
Intuition and Approach
Categories : Stacks, Linear Pass, Single Scan, Sliding Window, Frequency, Counting, Enumeration

Complexity
N:=#−colors

Time complexity:
O(N)

Space complexity:
O(N)(E)O(1)(I)

Code
'''
3208. Alternating Groups II
URL := https://leetcode.com/problems/alternating-groups-ii/description/
'''
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        nag = 0
        valOne = 0
        valTwo = 1
        nag += self.helper(colors,valOne,valTwo,k)
        nag += self.helper(colors,valTwo,valOne,k)
        return nag

    # Flag-control based method - avoid code deduplication
    def helper(self, colors: List[int], valOne:int, valTwo:int, k:int) -> int:
        nag = 0
        stack = []
        n = len(colors)
        nag += self.getNagInRange(stack,colors,valOne,valTwo,k,n)
        # reset, last index checking
        lastIdx = k - 1
        # last iter steps last cycles
        nag += self.getNagInRange(stack,colors,valOne,valTwo,k,lastIdx)
        return nag
    
    def getNagInRange(self, stack: List[int], colors: List[int], valOne:int, valTwo:int,k:int,lastIdx:int) -> int:
        nag = 0
        for rPtr in range(lastIdx):
            val = colors[rPtr]
            if(len(stack) == 0 and val == valOne):
                stack.append(val)
            elif(len(stack) > 0):
                mostRecentEl = stack[-1]
                if(1 - val == mostRecentEl):
                    stack.append(val)
                    # check cycle length
                    if(val == valTwo and k % 2 == 0):
                        if(len(stack) >= k):
                            nag += 1
                    elif(val == valOne and k % 2 == 1):
                        if(len(stack) >= k):
                            nag += 1
                else:
                    stack.clear()
                    if(mostRecentEl == valOne):
                        # clear stack, append valOne ( 0,0 )
                        stack.append(val)
        return nag
