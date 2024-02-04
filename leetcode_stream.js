/*
URL := https://leetcode.com/problems/product-of-the-last-k-numbers/
Use arrays over more complex DSA for streams
Classic "stream of numbers" problem -> need to compute aggregate(stream ) such as sum/product
Gaaah data stream problems

Sums easier in a stream ( versus products in a stream ) 

0 for sparsity though?

If the number is 0, realize you can only fetch so deep
it does render a NOP operation too

*/
var ProductOfNumbers = function() {
    this.prefixProds = []
    this.streamProd = 1
};

/** 
 * @param {number} num
 * @return {void}
 */
ProductOfNumbers.prototype.add = function(num) {
    if(num === 0){
        this.prefixProds.length = 0
        this.streamProd = 1
    } else {
        this.streamProd *= num
        this.prefixProds.push(this.streamProd)
    }
};

/** 
 * @param {number} k
 * @return {number}
 */
 /*
 Good assumption : single 32-bit int no overflow
 Called on only k numbers
 Note : k is not known here
 Careful due to the 0 number too
 */
ProductOfNumbers.prototype.getProduct = function(k) {
    let endIdx = this.prefixProds.length - 1
    let endProd = this.prefixProds.at(endIdx)
    let startIdx = endIdx - k
    let result = 1
    if(startIdx < -1) { 
        result = 0
    } else if ( startIdx >= -1) {
        if(startIdx == -1) {
            result = endProd
        } else {
            let startProd = this.prefixProds.at(startIdx)
            result = endProd / startProd
        }
    }
    return result    
};

/** 
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = new ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */
