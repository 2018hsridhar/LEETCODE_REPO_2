/*
URL := https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/
2997. Minimum Number of Operations to Make Array XOR Equal to K

Approach : Greedy, Counting, Linea Scan of Nums
Time := O(N)
Space := O(1) ( EXP & IMP ) ( 32 bits utilize an array instead )

https://stackoverflow.com/questions/38892455/initializing-an-array-of-zeroes
Without aggregate initialization, code is undefined
*/
class Solution {
public:

    bool isEven(int num){
        return (num % 2 == 0);
    }

    bool isOdd(int num){
        return (num % 2 == 1);
    }

    int minOperations(vector<int>& nums, int k) {
        typedef unsigned long long ull;
        int myMinOps = 0;
        int radixOneCount[32] = {0}; // aggregate init
        for(ull num: nums){
            std::bitset<32> curVal{num};
            for(int r = 0; r < 31; r++){
                if(curVal.test(r)){ // is one
                    radixOneCount[r]++;
                }  
            }
        }
        std::bitset<32> targetVal{(ull)(k)};
        for(int r = 0; r < 31; r++){
            int oneCount = radixOneCount[r];
            if((targetVal.test(r) && isEven(oneCount)) || (!targetVal.test(r) && isOdd(oneCount)) ){ // if 1
                myMinOps++;
            }
        }
        return myMinOps;
    }
};
