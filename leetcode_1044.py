'''
1044. Longest Duplicate Substring
URl := https://leetcode.com/problems/longest-duplicate-substring/description/?difficulty=HARD

Avoid sliding window : recreate O(S) space each time with prefix array idea
Hashmap + binary searching solution

Complexity
S = len(S)
T = O(lg(S)*S)
Space = O(S) ( Exp ) O(1) ( Imp ) 
It's any duplicate string ( agnostic frequency ) !
'''
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        longestLen = -1
        longestStr = ""
        low = 0
        n = len(s)
        high = n - 1
        while(low <= high):
            mid = (int)(0.5 * (low + high))
            freqMap = dict()
            foundDuplicate = False
            duplicateStr = ""
            for leftPtr in range(0,n-mid+1,1):
                subStr = s[leftPtr:leftPtr + mid]
                if(subStr not in freqMap):
                    freqMap[subStr] = 1
                else:
                    foundDuplicate = True
                    duplicateStr = subStr
                    del freqMap
                    break
            if(foundDuplicate and mid >= longestLen):
                longestLen = mid
                longestStr = duplicateStr
                low = mid + 1
            else:
                high = mid - 1
        return longestStr
        
