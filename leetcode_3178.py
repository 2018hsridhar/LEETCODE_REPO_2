Intuition & Approach
See problem comments

Complexity
Time complexity:
O(1)

Space complexity:
O(1)

Code
'''
Modular arithmetic cycle handling can we do in O(1) time here
n = 3 : 
{0,1,2,3,4} yields back to 0
so {0,1,2,3} for total cycles each time ( for n = 3 )
_,_,_
k - x : really x + 1 steps ( of time elapsing here ) 

_,_,_,_,_
{0,1,2,3,4,5,6,7,8} forlength of n = 5 ( 4 + 4 + 1 )
Can we take k - 1 ( modu lar arithm ) 

_,_
{0,1,2} ( len = 2 ) 

3178. Find the Child Who Has the Ball After K Seconds
URL := https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/solutions/5824860/python3-o-1-time-space-complexity-solution-leveraging-modular-arithmetic/

'''
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        modulo = (n - 1) * 2
        targetIdx = k % modulo
        lastIdx = n-1
        if(targetIdx >= lastIdx):
            targetIdx = lastIdx - (targetIdx - lastIdx)
        return targetIdx
        
