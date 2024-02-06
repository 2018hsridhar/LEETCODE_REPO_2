/**
 * @param {string} characters
 * @param {number} combinationLength
 */
 /*
 URL := https://leetcode.com/problems/iterator-for-combination/description/
 1286. Iterator for Combination
 10 minutes to solution

 TBH I did not use bitmasking, but probably should.
 */
var CombinationIterator = function(characters, combinationLength) {
  this.combinationLength = combinationLength
  this.combos = []

  let startIndex = 0
  let startCombo = ""
  createCombos(characters, startIndex, startCombo, this.combos, combinationLength)
  
  this.combos.sort() // should be default dictionary TBH
  this.readIndex = 0
  this.numCombos = this.combos.length
};

function createCombos(characters,index, curCombo, combos, combinationLength){
    let n = characters.length
    if(index === n && curCombo.length === combinationLength) {
        let sortCombo = curCombo.split("").sort().join("")
        combos.push(sortCombo)
    } else if ( index < n ) {
        let selectChar = characters.at(index) + curCombo
        createCombos(characters,index+1, selectChar,  combos, combinationLength)
        createCombos(characters,index+1, curCombo, combos, combinationLength)
    }
}

/**
 * @return {string}
 */
CombinationIterator.prototype.next = function() {
    if(this.hasNext()){
        return this.combos.at(this.readIndex++)
    } 
};

/**
 * @return {boolean}
 */
CombinationIterator.prototype.hasNext = function() {
    return (this.readIndex < this.numCombos)
};

/** 
 * Your CombinationIterator object will be instantiated and called as such:
 * var obj = new CombinationIterator(characters, combinationLength)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */
