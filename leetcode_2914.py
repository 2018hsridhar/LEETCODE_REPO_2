'''
URL := https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/
2914. Minimum Number of Changes to Make Binary String Beautiful

Complexity :
Let N := len(s)
Time := O(N)
Space := O(1) ( E & I ) 

15 minutes to incredibly elegant code

'''
class Solution:
    def minChanges(self, s: str) -> int:
        numChanges = 0
        for idx in range(0,len(s),2):
            numChanges += int(abs(int(s[idx]) - int(s[idx+1])))
        return numChanges
