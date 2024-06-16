'''
URL := https://leetcode.com/problems/simplified-fractions/description/
1447. Simplified Fractions

Fraction simplification problem -> woooh based on GCD
Any order -> leverage sets ( hmmm specifically a decimal set ) ( or a string set too ! ) 
Either or works
Answer in either order

Complexity :
Let N := some positive integer
Time = O(N^2) 
    Start with 2 ( base case ) and then decrease and lower.
    e.g. n = 7 : 1/7,2/7,...,6/7 ( 1...(n-1)) reasoning up to the nth number
    Triangular pyramid pattern
Space = O(N^2)

'''
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        myFracs = set()
        for den in range(2,n+1,1):
            for num in range(1,den,1):
                gcd = (int)(math.gcd(num,den))
                # adjust for non-integer division to integer division
                adjNum = (str)((int)(num / gcd))
                adjDen = (str)((int)(den / gcd))
                simplifiedFrac = "".join([adjNum,"/",adjDen])
                if(simplifiedFrac not in myFracs ):
                    myFracs.add(simplifiedFrac)
        return list(myFracs)
