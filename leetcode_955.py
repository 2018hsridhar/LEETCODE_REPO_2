Python3 Approach Induction Left->Right Greedy Sorted and Track Continuous Prefixes

2018hsridhar
100 Days Badge 2022
28
0
in a few seconds
Python3
Array
String
Greedy
Intuition
Approach
Complexity
Time complexity:
Space complexity:
Code
'''
URL := https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description/
955. Delete Columns to Make Sorted II

Complexity
Let S := #-strings, N := len(longest string)
Each string is of same length!!!
Time = O(SN)
Space = O(1) ( E ) O(1) ( I ) 

Approach : Greedy, Sorting, Lexicographic ordering
Induction and proceed left -> right only ( think of first col / single col case ) 

15 mins to solutioning
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        firstWord = strs[0]
        n = len(firstWord)
        s = len(strs)
        numDelColumns = 0
        # if cur column is sorted, escape out earlier
        prefixes = ["" for x in range(len(strs))]
        for column in range(n):
            ptr = 0
            colSortStatus = True
            prefixCol = []
            for ptr in range(s - 1):
                curWord = strs[ptr]
                nextWord = strs[ptr + 1]
                curLet = curWord[column]
                nextLet = nextWord[column]
                curVal = prefixes[ptr] + curLet
                nextVal = prefixes[ptr+1] + nextLet
                if(curVal > nextVal):
                    colSortStatus = False
                    break
            if(colSortStatus):
                for ptr in range(s):
                    curWord = strs[ptr]
                    letter = curWord[column]
                    prefixes[ptr] += letter
            elif(colSortStatus == False):
                numDelColumns += 1
        return numDelColumns
                



