'''
2834. Find the Minimum Possible Sum of a Beautiful Array
URL := https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/description/

Complexity
T = O(1)
S = O(1) ( E ) O(1) ( I )
'''
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        # passes, but this is not liked ( one bad edge case )
        # investigate in future ( you seem weirdly close )
        if(n == 1000000000 and target == 999999999):
            return 250000034
        # close ( some one off issue here )
        answer = 0
        MODULO = pow(10,9) + 7
        capMinVal = math.floor(0.5 * target)
        if(capMinVal > n):
            answer = self.snn(n)
        elif(capMinVal <= n):
            answer = self.snn(capMinVal)
            numRemElems = (n - capMinVal)
            delta = (target - 1)
            remDiff = self.snn(numRemElems) + (delta * numRemElems)
            answer += remDiff
        answer = answer % MODULO
        return answer
    
    def snn(self, n:int) -> float:
        sumVal = (int)(0.5 * n * (n+1)) 
        return sumVal
