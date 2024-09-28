Intuition and Approach
See problem title

Complexity
Let N,K:= lengths of the binary string : longest and shortest

Time complexity:
O(N)+O(K)

Space complexity:
O(1) ( Implicit )
O(MAX(N,K)) ( Explicit )

Code
'''
URL := https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/description/
3226. Number of Bit Changes to Make Two Integers Equal

'''
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        minNumChanges = 0
        n_bin = self.getBinaryRep(n)
        k_bin = self.getBinaryRep(k)
        n_ptr = len(n_bin) - 1
        k_ptr = len(k_bin) - 1
        while(n_ptr >= 0 and k_ptr >= 0):
            n_val = n_bin[n_ptr]
            k_val = k_bin[k_ptr]
            if(n_val != k_val):
                if(n_val == "0"):
                    return -1
                else:
                    minNumChanges += 1
            k_ptr -= 1
            n_ptr -= 1
        # equal to 1 : set to zero
        while(n_ptr >= 0):
            n_val = n_bin[n_ptr]
            if(n_val == '1'):
                minNumChanges += 1
            n_ptr -= 1
        while(k_ptr >= 0):
            k_val = k_bin[k_ptr]
            if(k_val == '1'):
                return -1
            k_ptr -= 1
        return minNumChanges

    def getBinaryRep(self, n:int) -> str:
        binRep = []
        while(n > 1):
            rem = n % 2
            binRep.append((str)(rem))
            n = (int)(n/2)
        binRep.append((str)(n))
        binRep.reverse()
        binString = "".join(binRep)
        return binString
        
