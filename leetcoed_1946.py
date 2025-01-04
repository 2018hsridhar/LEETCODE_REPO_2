'''
1946. Largest Number After Mutating Substring
URL := https://leetcode.com/problems/largest-number-after-mutating-substring/

Linear Pass, Single Scan, Greedy, always change to larger digital whenver we can 
Greedy -> whenever we encounter the first increase, we start from there and we KEEP increasing ( until we can not 0 
E.g. 132 -> incr(1), 3 = stop
Hmm ... 3 = 3 : identity -> proceed onwards
If we start with equals case : wait till we hit first >. Always first > case
'''
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num)
        maxNum = ""
        hitIndex = -1
        for index,letter in enumerate(num):
            digVal = (int)(letter)
            toChange = (int)(change[digVal])
            if(toChange > digVal):
                hitIndex = index
                break
        if(hitIndex == -1):
            return num
        prefix = num[0:hitIndex]
        maxNum += prefix
        curIndex = hitIndex
        suffixIndex = -1
        while(curIndex < n):
            letter = num[curIndex]
            digVal = (int)(letter)
            toChange = (int)(change[digVal])
            if(toChange < digVal):
                suffixIndex = curIndex
                break
            else:
                maxNum += (str)(toChange)
            curIndex += 1
        if(suffixIndex != -1):
            suffix = num[suffixIndex:]
            maxNum += suffix
        return maxNum
