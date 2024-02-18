/**
 * @param {number} a
 * @param {number} b
 * @return {string}
 */
/*
984. String Without AAA or BBB
URL = https://leetcode.com/problems/string-without-aaa-or-bbb/description/
*/
var strWithout3a3b = function(a, b) {
    let constString = []
    let maxLet = (a > b) ? 'a' : 'b'
    let minLet = (a > b) ? 'b' : 'a'
    let maxFreq = Math.max(a,b)
    let minFreq = Math.min(a,b)
    let i = 0
    // potential bug odd case hang on
    while(i < maxFreq){
        if(i === maxFreq - 1){
            constString.push(maxLet)
            i++
        } else {
            constString.push(maxLet)
            constString.push(maxLet)
            if(minFreq > 0){
                constString.push(minLet)
                minFreq -= 1
            }
            i += 2
        }
    }
    let constStringTwo = []
    let curLen = constString.length
    for(let rPtr = 0; rPtr < curLen; rPtr++){
        let firstLet = constString[rPtr]
        constStringTwo.push(firstLet)
        // Fill up the remaining slots with min Leter ( have minLeter remaining case )
        if(minFreq > 0){
            if(rPtr + 1 < curLen){
                let secondLet = constString[rPtr+1]
                if(firstLet === secondLet){
                    constStringTwo.push(minLet)
                    minFreq--
                }
            } else {
                constStringTwo.push(minLet)
                minFreq--
            }
        }
    }
    let resultStr = constStringTwo.join("")
    return resultStr
};
