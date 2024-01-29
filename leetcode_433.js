/**
 * @param {string} startGene
 * @param {string} endGene
 * @param {string[]} bank
 * @return {number}
 */
 /*
 Harder to model in a bottom-up fashion versus a top-down fashion
 Easier to model with top-down memoization

 URL := https://leetcode.com/problems/minimum-genetic-mutation/
 433. Minimum Genetic Mutation

 Complexity
 Let N := #-genes in the bank
 Time := O(N)
 Space := O(N) ( EXP ) O(N) ( IMP ) 

 */
var minMutation = function(startGene, endGene, bank) {
    let stepsHash = new Map()
    let visited = new Set()
    let myMinMut = solveMinMut(startGene,endGene,bank,stepsHash,visited)
    if(myMinMut === Number.MAX_VALUE){
        return -1
    }
    return myMinMut
};

function solveMinMut(startGene,endGene,bank,stepsHash,visited){
    let geneCharSet = ['A','C','G','T']
    if(startGene.localeCompare(endGene) === 0){
        stepsHash.set(startGene,0)
        visited.add(startGene)
        return 0
    } else {
        if(stepsHash.has(startGene)){
            return stepsHash.get(startGene)
        }
        visited.add(startGene)
        let minMutateSteps = Number.MAX_VALUE // largest number possible in JS ( for safety ) 
        for(let a = 0; a < 8; a++){
            let curChar = startGene.at(a)
            for(let b = 0; b < 4; b++){
                let nextChar = geneCharSet.at(b)
                if(curChar !== nextChar){
                    let nextGene = startGene.slice(0,a) + nextChar + startGene.slice(a+1)
                    // .includes() has more browser support nowadays
                    // issue is in cycles detection in genetic mutations
                    if(bank.includes(nextGene) && !visited.has(nextGene)){
                    // if(bank.indexOf(nextGene) > -1 && !visited.has(nextGene)){
                        // console.log("a = " + a + "\tb = " + b + "\t Cur gene = " + startGene + "\t NExt gene = " + nextGene)
                        let childSteps = 1 + solveMinMut(nextGene,endGene,bank,stepsHash,visited)
                        minMutateSteps = Math.min(minMutateSteps, childSteps) // package static method dispatch
                    }
                }
            }
        }
        stepsHash.set(startGene,minMutateSteps)
        return stepsHash.get(startGene)
    }
}

