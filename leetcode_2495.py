'''
2495. Number of Subarrays Having Even Product
URL := https://leetcode.com/problems/number-of-subarrays-having-even-product/description/

Diagramatics :
# number with even product
Check parities of each index

[O,E,O,E,O,E]
 ^ --------> 
[O,O,O,E,E,O,O,E,E]
 ^      --------->
[E,O,E,O,E,E,E,O,E,E,O,E,E]
 ^     -------       -----
Careful on countings -> hitting other parities
Index position harder : some counting mechanism helps better
Split cases differently : O and E

O*O = O
O*E = E*O = E*E = Evens ( have a 2 ) 
Right -> left : greedy -> first even value
Even el ( nonTrivial ) oddEl ( first Even Value ) 

Categories : Linear Scan, Greedy, Single Pass, Sliding Windows

Target Complexity Analysis
N = len(input)
T = O(N)
S = O(1) ( E ) O(1) ( I ) 
'''
class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        numEvenProdSubArr = 0
        n = len(nums)
        FLAG_VALUE = float('inf')
        earliestEvenIndex = FLAG_VALUE
        curNumSubArr = 0
        for index in range(len(nums) - 1, -1, -1):
            curVal = nums[index]
            # Odd
            if(curVal % 2 == 1):
                if(earliestEvenIndex != FLAG_VALUE):
                   curNumSubArr = (n - earliestEvenIndex)
            # Even
            elif(curVal % 2 == 0):
                curNumSubArr = (n - index)
                earliestEvenIndex = min(earliestEvenIndex,index)
            numEvenProdSubArr += curNumSubArr
        return numEvenProdSubArr

        
