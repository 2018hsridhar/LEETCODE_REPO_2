Python3 Linear Time, Constant Space, Iterative Solution Leveraging Two Pointers and in-place swp op

Hari Sridhar
100 Days Badge 2022
29
0
a few seconds ago
Python3
Two Pointers
String
Intuition and Approach
Encountered this problem before, working with character arrays directly ( algoexpert.io ) ?

Categories : Linear Scans, Single ( or Double ) Passes, Two Pointers
Number of passes : one, two, three -> 3*n = n

Complexity
N := len(input) ( #-characters)

Time complexity:
O(N)

Space complexity:
O(1) ( E and I )

Code
'''
URL := https://leetcode.com/problems/reverse-words-in-a-string-ii/description/
186. Reverse Words in a String II
'''
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        lPtr = 0
        rPtr = len(s) - 1
        while(lPtr < rPtr):
            self.swap(s,lPtr,rPtr)
            lPtr += 1
            rPtr -= 1
        # Second pass
        lPtr = 0
        rPtr = 0
        delimeter = " "
        for rPtr in range(len(s)):
            if(s[rPtr] == delimeter):
                self.reverseWord(s,lPtr,rPtr - 1)
                lPtr = rPtr + 1
            rPtr += 1
        # handle last word
        # No leading/trailing spaces guarantee
        self.reverseWord(s,lPtr,len(s)-1)
        
    def reverseWord(self, s:List[str], left:int,right:int) -> None:
        while(left < right):
            self.swap(s,left,right)
            left += 1
            right -= 1

    def swap(self, s: List[str], left:int, right:int) -> None:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp



        
