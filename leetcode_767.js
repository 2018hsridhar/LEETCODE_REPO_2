/**
 * @param {string} s
 * @return {string}
 */
 /*
 URL := https://leetcode.com/problems/reorganize-string/description/
 767. Reorganize String

Let's skip modularization for now

Complexity
N := #-letters in a string
T = O(N)
S = O(N) ( EXP ) O(1) ( IMP ) 

15 mins to solutioning :-)

 */
var reorganizeString = function(s) {
    let letFreq = new Map()
    let nextFreq = -1
    let maxOccurLetter = ""
    let maxOccurFreq = -1
    s.split("").forEach((letter) => {
        if(!letFreq.has(letter)){
            letFreq.set(letter,0)
        }
        nextFreq = letFreq.get(letter) + 1
        if(nextFreq > maxOccurFreq) {
            maxOccurFreq = nextFreq
            maxOccurLetter = letter
        }
        letFreq.set(letter, nextFreq)
    })
    let remLetterCount = s.length - maxOccurFreq
    let reorgString = ""
    if(remLetterCount >= maxOccurFreq - 1) {
        let wIdx = 0
        let writeStrings = Array(maxOccurFreq).fill(maxOccurLetter)
        letFreq.forEach((freq,letter) => {
            if(letter !== maxOccurLetter) {
                for(let a = 0; a < freq; a++){
                    writeStrings[wIdx] += letter
                    wIdx = (wIdx + 1) % maxOccurFreq
                }
            }
        })
        // concatenate an array(of srings) into a full string
        reorgString = writeStrings.join("") // liking `join` prototype method
    } 
    return reorgString
};
