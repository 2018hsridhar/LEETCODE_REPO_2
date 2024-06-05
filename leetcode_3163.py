'''
3163. String Compression III
URL := https://leetcode.com/problems/string-compression-iii/

Complexity :
Let N := len(word)
T = O(N)
S = O(1) ( E & I ) 

'''
class Solution:
    def compressedString(self, word: str) -> str:
        compressedRes = ""
        n = len(word)
        i = 0
        curWindowLen = 1
        while(i < n):
            leftPos = i
            while(curWindowLen < 9 and i+1 < n):
                if(word[i] == word[i+1]):
                    curWindowLen += 1
                    i += 1
                else:
                    break
            # [start, stop - 1] type of thing going on
            curPrefix = word[leftPos:leftPos+curWindowLen]
            # .join() more performant than regular "+" string concatenation
            compressedRes = "".join([compressedRes, str(curWindowLen),curPrefix[0]])
            i += 1
            curWindowLen = 1
        # get last character if i == n-1 type of thing
        if(i < n-1):
            lastPrefix = word[i:]
            compressedRes = "".join([compressedRes, str(len(lastPrefix)),lastPrefix])
        return compressedRes
        
