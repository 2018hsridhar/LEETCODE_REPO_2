/**
 * @param {string} s
 * @return {number}
 */
 /*
 2938. Separate Black and White Balls
 URL := https://leetcode.com/problems/separate-black-and-white-balls/
 Should be reclassified as easy
 6 mins to solutioning
 
 Goal : to minimize the number of swap operations on a binary string
 Swap for groupings of elements

 Complexity
 Let N = len(input)
 Time := O(N)
 Space := O(1) ( EXP & IMP ) 

 Every <1> values needs to get pushed to the right
 Can we be greedy with our push values?
 Only way to move is to engage in swaps
 We know what the write index will be as well

 No swaps needed -> basic counting

{ WHITE -> LEFT as BLACK -> RIGHT }

 10001001010001010111
 */
var minimumSteps = function(s) {
    let minSteps = 0;
    let n = s.length; // properties ain't functions :-)
    let readPtr = writePtr = n-1;
    let delta = 0;
    while(readPtr >= 0) {
        // https://www.freecodecamp.org/news/javascript-string-comparison-how-to-compare-strings-in-js/
        // localeCompare over mathematical operatinos for correct behavior in ordering and I18n
        if(s[readPtr].localeCompare("1") === 0){
            delta = (writePtr - readPtr);
            minSteps += delta;
            writePtr--;
        }
        readPtr--;
    }
    return minSteps;
};
