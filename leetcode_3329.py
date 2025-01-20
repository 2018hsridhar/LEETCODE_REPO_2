'''
3329. Count Substrings With K-Frequency Characters II
URL := https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/description/

Complexity
N = len(s)
T = O(S)
S = O(1) ( Exp ) O(1) ( Imp ) 

Categories : Hashmaps, Sliding Windows, Linear Scans

Idea : 
> aba.... ( once a letter appeears twice, each letter concat = valid str )
> how to slide left though?
> For a given left character, find earliest right character window too ( type of thing )?
    abc....a
      ^    _ first 2x appearances
    Close and still hit : abc...a ( -b-c-a ) ( hit at 2x ) -> dispatched

Did TC ask if we need to MODULO ans?
'''
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        numValidStrings = 0
        leftPtr = 0
        rightPtr = 0
        letterFreq = dict()
        for rightPtr, rightLetter in enumerate(s):
            if(rightLetter not in letterFreq):
                letterFreq[rightLetter] = 0
            curFreq = letterFreq[rightLetter]
            nextFreq = curFreq + 1
            letterFreq[rightLetter] = nextFreq
            rightFreq = letterFreq[rightLetter]
            # don't remove, but allow for the 0 case at least
            # at least one character k times occur
            while(leftPtr <= rightPtr and rightFreq == k):
                curWindow = len(s) - rightPtr
                numValidStrings += curWindow
                leftLetter = s[leftPtr]
                letterFreq[leftLetter] -= 1
                rightFreq = letterFreq[rightLetter]
                leftPtr += 1
        return numValidStrings
