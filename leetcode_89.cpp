/*
89. Gray Code
Relief @ usage of C++ bitset library here :-)

URL := https://leetcode.com/problems/gray-code/
Gaaah bitset needs a constant -> have to pass ints :-(

Can affix known length : 16 value?
Bit tracking works
Gaaah so much learning ... on the C++ bitset library.
*/
typedef unsigned long long ull;

class Solution {
public:
    vector<int> grayCode(int n) {
        ull initState = 0;
        set<int> grayCodeSet;
        vector<int> grayCodeSeq;
        grayCodeSet.insert(0); // this is a known anyways
        grayCodeSeq.push_back(0);
        dfs(n, initState, grayCodeSet,grayCodeSeq);
        return grayCodeSeq;
    }

    // Iterate only so many values then
    // Early termination a value hit
    // Vector is needed for ordering though :-(
    bool dfs(int n, ull parentVal, set<int>& seenCodes, vector<int>& grayCodeSeq){
        bool hitAllCodes = false;
        int totalNeeded = pow(2,n);
        std::bitset<16> parentState{parentVal};
        for(int i = 0; i < n; i++){
            std::bitset<16> childState = parentState;
            childState.flip(i); // length is guaranteed ( but do we need a set )?
            ull childVal = childState.to_ullong();
            // Woooh C++20 contains() method for sets
            if(!seenCodes.contains(childVal)){
                seenCodes.insert(childVal);
                grayCodeSeq.push_back(childVal);
                // pop_count() : only one bit set 
                // gaaah use count() method isntead
                if(seenCodes.size() == totalNeeded && childState.count() == 1){
                    hitAllCodes = true;
                    break;
                } else {
                    bool childDfs = dfs(n,childVal,seenCodes, grayCodeSeq);
                    if(childDfs){
                        hitAllCodes = true;
                        break; // return vector and sets as they are
                    }
                    seenCodes.erase(childVal);
                    grayCodeSeq.pop_back();
                }
            }
        }
        return hitAllCodes;
    }
};
