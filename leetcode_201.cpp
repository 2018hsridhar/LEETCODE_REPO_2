/*
URL := https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
201. Bitwise AND of Numbers Range

Test Cases
(A) 15,15
(B) 4,8 => 0
(C) 500, 7891213
(D) 4,8
(E) 255,256
(F) 3,3
(G) 1023, 2147483647

Exec the bitwise testing for all input digits
Return value -> not the boolean wow
Time, Space := O(1) all cases

Go up to the max radix only : the power you are less than ( square it ) 

*/
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        long long int lhs = left;
        long long int rhs = right;
        if(left == 0 || right == 0) {
            return 0;
        }
        if(left == right) {
            return left;
        } 
        bool canBitWiseAndRange = true;
        int maxRadix = ceil(log2(left) + 1); // what if 0 there too :-( oh no
        // cout << maxRadix << endl;
        int offset = 0;
        unsigned long long ull = left; // widening conv implicit
        std::bitset<33> myValue{ull};
        std::bitset<32> retValue{0};
        // Start from the right and do checks
        for(int radix = 0; radix < maxRadix; radix++){
            long long int cycleLength = std::pow(2,radix+ 1); // 1 as a special case
            // Value agnostic testing : whether 0 or 1
            long long int delta = (cycleLength / 2 ) - offset;
            if(lhs + delta <= rhs) { 
                retValue[radix] = 0;
            } else {
                retValue[radix] = myValue[radix];
            }
            if(myValue.test(radix)){ // if a one
                offset += (int)(std::pow(2,radix));
            }
        }
        // cout << retValue.to_string() << endl;
        int res = (int)(retValue.to_ulong());
        return res;
    }
};
