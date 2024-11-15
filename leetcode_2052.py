Bottom-up Dynamic Programming Quadratic Time ( number of words ) approach in Python3

Hari Sridhar
100 Days Badge 2022
29
0
a few seconds ago
C++
Python3
Array
Dynamic Programming
Intuition, Category, and Appraoch
Category : Definitely Dynamic Programming, Recursion, Exploring State Space

Complexity
S:=len(sentence)(#−characters)
W:=#−words
K:=agiven

Time complexity:
O(pow(W,2))

Space complexity:
O(W)(Explicit)O(1)(Implicit)

Code
'''
URL := https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/description/
2052. Minimum Cost to Separate Sentence Into Rows
'''
class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        # single space seperation, no spaces start and end
        # insert line breaks : no split word, change word order, etc.,
        # in a given row, each word space split. 
        # len @ most k each word : guarnateed splits!
        minCost = float("inf")
        tokens = sentence.split()
        n = len(tokens)
        memo = [-1 for idx in range(len(tokens))]
        for idx in range(n-1,-1,-1):
            print("Idx = " + str(idx))
            j = idx
            curCost = 0
            windowSize = k
            bestProblemCost = float('inf')
            curLen = 0
            # it's length of the row ( num characters in row )
            # "i love" =  6 characters
            while(j < n):
                curLen += len(tokens[j])
                # print(curLen)
                windowSize -= len(tokens[j])
                if(windowSize < 0):
                    break
                elif(windowSize >= 0):
                    curCost = pow((k - curLen),2)
                    curSubProblemCost = curCost
                    if(j+1 < n):
                        curSubProblemCost += memo[j+1]
                        # ignore last row cost - cut costs there
                        curSubProblemCost -= memo[-1]
                        bestProblemCost = min(bestProblemCost,curSubProblemCost)
                    else:
                        bestProblemCost = 0
                    # for space character append
                    windowSize -= 1
                    curLen += 1
                j += 1
            memo[idx] = bestProblemCost
        minCost = memo[0]
        return minCost
