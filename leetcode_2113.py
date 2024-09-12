Intuition and Approach
We're dealing with modulus and cycle operations here

Complexity
Q:= -queries to execute
N:=len(input)
Each Query takes O(1) time ( mathematical operations only )

Time complexity:
O(Q)

Space complexity:
O(1) ( Explicit )
O(1) ( Implicit )

Code
'''
2113. Elements in Array After Removing and Replacing Elements
URL := https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/description/

'''
class Solution:
    # be careful with how the cycle was initiallys et up too -> is it pure modular arithmetic?
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        cycleLen = (2*n)
        # answers default initialized to value = -1
        answers = [-1 for i in range(len(queries))]
        for ansIndex,query in enumerate(queries):
            queryTime = query[0]
            queryIndex = query[1]
            queryRemainder = queryTime % cycleLen
            listLenAtQueryTime = -1
            if(queryRemainder <= n):
                listLenAtQueryTime = (n - queryRemainder)
                finalListIdx = listLenAtQueryTime - 1
                if(queryIndex <= finalListIdx):
                    # you have the correct list length : need decrement operation here
                    targetIndex = (queryIndex + queryRemainder)
                    answers[ansIndex] = nums[targetIndex]
            else:
                listLenAtQueryTime = (queryRemainder % n)
                finalListIdx = listLenAtQueryTime - 1
                if(queryIndex <= finalListIdx):
                    # putting values back : can read in ASC order
                    answers[ansIndex] = nums[queryIndex]
        return answers
