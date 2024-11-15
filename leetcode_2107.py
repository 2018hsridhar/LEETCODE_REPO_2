Python3 Sliding Window Linear Time and Linear Space Solution Using Hashmaps

Hari Sridhar
100 Days Badge 2022
29
0
a few seconds ago
C++
Python3
Array
Hash Table
1+
Intuition and Approach
Categories : Sliding Window, HashMap, Single Pass, Linear Scan

Complexity
N:=len(input)

Time complexity:
O(N)

Space complexity:
O(N)(E)O(1)(I)

Code
'''
2107. Number of Unique Flavors After Sharing K Candies
URL := https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/description/
Give k consecutive candies, but be greedy - keep as many as needed
Given some range of k to share - max number you keep is? 
'''
class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        maxNumUniqFlavors = 0
        # Global space : all candies
        globalSpace = dict()
        for candy in candies:
            if(candy not in globalSpace):
                globalSpace[candy] = 0
            globalSpace[candy] += 1
        # using a list/queue -> better ideas? hmm?
        window = []
        for rPtr, val in enumerate(candies):
            # 1. The accumulation phase of a window
                # a. append next val
            if(len(window) < k):
                window.append(val)
                nextVal = globalSpace[val] - 1
                globalSpace[val] = nextVal
                if(nextVal == 0):
                    del globalSpace[val]
                # special case
                if(len(window) == k):
                    curNumFlavors = len(globalSpace.keys())        
                    maxNumUniqFlavors = max(maxNumUniqFlavors, curNumFlavors)
            # 2. The actual window analysis phase
            elif(len(window) == k):
                # a. append next val
                window.append(val)
                nextVal = globalSpace[val] - 1
                globalSpace[val] = nextVal
                if(nextVal == 0):
                    del globalSpace[val]
                # b. remove first val
                firstEl = window.pop(0)
                if(firstEl not in globalSpace):
                    globalSpace[firstEl] = 0
                globalSpace[firstEl] += 1
                # c. analytics phase
                curNumFlavors = len(globalSpace.keys())        
                maxNumUniqFlavors = max(maxNumUniqFlavors, curNumFlavors)
        return maxNumUniqFlavors
        
