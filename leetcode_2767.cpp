/*
2767. Partition String Into Minimum Beautiful Substrings
URL := https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

Partitioning is a DP problem TBH
Semblance of a DP problem in the hiding

*/
class Solution {
public:
    int minimumBeautifulSubstrings(string s) {
        int n = s.length();
        vector<int> memo(n+1,INT_MAX); // let compiler optimized for this expr : dodge init lists via vectors
        int startIndex = 0;
        int minBeat = solveMinBeat(s,startIndex,memo);
        return (minBeat == INT_MAX) ? -1 : minBeat;
    }

    // Vector<T> over T[] array style in C++
    // Be careful with memoizations here
    int solveMinBeat(string s, int index, vector<int>& memo){
        int minBeat = INT_MAX;
        int n = s.length();
        if(index == n) {
            minBeat = 0;
        } else if ( index < n) {
            if(memo[index] != INT_MAX) {
                return memo[index];
            }for(int j = index; j < n; j++){
                string prefix = s.substr(index, j - index + 1);
                if(isBeautiful(prefix)){
                    int childCase = solveMinBeat(s,j+1,memo);
                    // please catch overflow exceptions : if child case unsolveable, do not account for it
                    if(childCase != INT_MAX ) {
                        minBeat = std::min(minBeat, 1 + childCase);
                    }
                }
            }
        }
        memo.at(index) = (minBeat == INT_MAX) ? INT_MAX : minBeat;
        return memo.at(index);
    }

    // C++ is std::basic_string<T> based
    // C++ hates idea of specific Math package -> forces use of std lib for math operations
    // Also gaaah at bitsets also being part of standard library.
    // At least they enable working with binary strings rapid
    bool isBeautiful(string s){
        bool isBeat = true;
        if(s[0] == '0'){
            isBeat = false;
        } else {
            std::bitset<16> bit_string(s);
            unsigned long bitVal = bit_string.to_ulong(); // bitsets on unsigned long conversions
            float logVal = std::log(bitVal) / std::log(5);
            if(!is_integer(logVal)){
                isBeat = false;
            }
        }
        return isBeat;
    }

    // Integer is floor(x) == x TBH
    bool is_integer(float k)
    {
        return std::floor(k) == k;
    }
};
