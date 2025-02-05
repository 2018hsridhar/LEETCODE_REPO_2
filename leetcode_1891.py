'''
URL := https://leetcode.com/problems/cutting-ribbons/description/
1891. Cutting Ribbons

Complexity
N = len(input)
H = max considerable length
T = O(N*log(H))
S = O(1) ( Explicit ) (1) ( Implicit )

15 mins solutioned
'''
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        maxLen = 0
        ribbons.sort()
        n = len(ribbons)
        low = 1
        high = pow(10,5)
        while(low <= high):
            mid = (int)((0.5)*(low+high))
            curRibbonCount = 0
            for ribbon in ribbons:
                numRibbons = (int)((ribbon / mid))
                curRibbonCount += numRibbons
            if(curRibbonCount >= k):
                low = mid + 1
                maxLen = max(maxLen,mid)
            elif(curRibbonCount < k):
                high = mid - 1
        ans = (int)(maxLen)
        return ans

        
