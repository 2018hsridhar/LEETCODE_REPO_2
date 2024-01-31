/*
URL := https://leetcode.com/problems/find-if-array-can-be-sorted/description/
3011. Find if Array Can Be Sorted
It's a fun problem : For any increasing sorted base 10 array, it's corresponding base 2 array equivalent must also be sorted in incr order

Any two adjacent elements with the same number of set_bits ( take note of this )
- it's not just a count of number of elements with the same bit sits => one a grouping is gone, it is gone

The number of set_bits = popcount ( https://en.cppreference.com/w/cpp/numeric/popcount ) 
Adjacency invariant yields power to problem 

Complexity : Time = O(N) Space = O(1)
*/
class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        // O(N) pass vs O(NlgN) performancy with adjacency?
        // 8 bits max only : pow(2,8) bounding
        // popcount ranges can go [1,1,1,2,2,3,3,1,1,1,4,4] type of thing
        // localMax of each popCountGrp
        std::vector<int> grpStats{INT_MAX, INT_MIN}; // ordering : min, max
        int localMax = nums.at(0);
        int localMin = nums.at(0);
        for(int i = 0; i < nums.size() - 1; i++){
            // only on extended unsigned integer types for std::popcount() logic
            // https://leetcode.com/problems/find-if-array-can-be-sorted/
            int popCountOne = std::popcount((unsigned int)nums.at(i));
            int popCountTwo = std::popcount((unsigned int)nums.at(i+1));
            if(popCountOne != popCountTwo){
                if(localMin < grpStats.at(1)){
                    return false;
                } else {
                    grpStats.at(0) = localMin;
                    grpStats.at(1) = localMax;
                    localMax = nums.at(i+1);
                    localMin = nums.at(i+1);
                }
            } else {
                localMin = min(localMin,nums.at(i+1));
                localMax = max(localMax,nums.at(i+1));
            }
        }
        return (localMin > grpStats.at(1));
    }
};
