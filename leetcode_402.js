/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
 /*
402. Remove K Digits
 URL := https://leetcode.com/problems/remove-k-digits/description/

 Stack based
 1. Must remove exactly k -> take note of this
 Ordering of removes
 (A) Any time we have a decrease in a sequence - greedily - '4->3->2' or '9->5->6->7' types
 (B) After all decreases out -> increases from the left : 12345->2345->345. Remove leftmost radix digit : numbers become tinier
 (C) Then leading zeros, if possible ( although it would have zeroed out at this point too )

Classification : Greedy, Stack Based

Complexity
Let N := #-digits
Time := O(N)
Space := O(N) ( EXP ) O(1) ( IMP ) 

So many handling conditions on edge cases GAAAH!!

 */
var removeKdigits = function(num, k) {
    let numStk = []
    // Liking the MDN web docs for JS
    // If we hit a decrease, we know to take the number to the left out at least
    // and we keep wanting to do this too
    num.split("").forEach((curNum) => {
        if(numStk.length > 0){
            let topNum = numStk.at(numStk.length - 1) // nice prototype method
            while(topNum > curNum && numStk.length > 0){
                if(k > 0){
                    numStk.pop()
                    k--
                    topNum = numStk.at(numStk.length - 1)
                } else {
                    break
                }
            }
        }
        numStk.push(curNum)
    })

    // remove positive elements left to right
    // 10203 (k=3) => 00 => 0 => effectively NOP
    // can we really just do this ( e.g. 112) => "11" or "12" possible
    // '12345' k = 4 => "1" or '54321' k = 4 => '1'
    // removing any digit decreases overall number of values -> take out the digits, largest to smallest, instead 
    // here eveyrthing is increasing though
    // increasing with k > 0 -> take away larger elements
    // hard to do removal when all increasing -> save for removal of the largest digits ( if you can locate them )
    // n times iterate over the string
    let digitStr = "987654321"
    digitStr.split("").forEach((digit) => {
        for(let i = 0; i < numStk.length; i++){
            if(numStk.at(i) === digit){
                if(k > 0){
                    numStk.splice(i,1)
                    i -= 1
                    k--
                } else {
                    return // not just a break ( careful with forEach )
                }
            }
        }
    })
    // Remove leading zeroes
    while(numStk.length > 0){
        let leftEl = numStk.at(0)
        if(leftEl === "0"){
            numStk.shift()
        } else {
            break
        }
    }
    // if length is 0, return 0
    return (numStk.length === 0) ? "0" : numStk.join("")
};
