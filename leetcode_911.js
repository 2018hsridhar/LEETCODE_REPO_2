/**
 * @param {number[]} persons
 * @param {number[]} times
 */
 /*
 URL := https://leetcode.com/problems/online-election/description/
 911. Online Election

 Binary search problem in the hiding
 Complexity
 5000 candidates T times bSearch O(logT)
 Time := O(logT)
 Space := O(T) ( map ) 
 */
var TopVotedCandidate = function(persons, times) {
    this.myCastVotes = new Map()
    let i = 0
    let n = persons.length
    for(let i = 0; i < n; i++){
        let person = persons[i]
        let time = times[i]
        if(!this.myCastVotes.get(person)){
            this.myCastVotes.set(person, [])
        }
        this.myCastVotes.get(person).push(time) // not automatically sorted
    }
    this.myCastVotes.forEach((val,key) => {
        this.myCastVotes.get(key).sort((a,b) => { return Number(a) - Number(b) })
    })
};

/** 
 * @param {number} t
 * @return {number}
 */
TopVotedCandidate.prototype.q = function(t) {
    let leadingPerson = 0
    let leadingIndex = -1 // val not found -> return -1 ( a max thing )
    let mostRecentVote = -1
    this.myCastVotes.forEach((castVotes,personId) => {
        let queryAns = this.bSearch(castVotes,t)
        // 0 -> # of votes as 1 -> receny of votes
        if(queryAns[0] > leadingIndex){
            leadingIndex = queryAns[0]
            mostRecentVote = queryAns[1]
            leadingPerson = personId
        }
        else if(queryAns[0] == leadingIndex){
            if(queryAns[1] > mostRecentVote){
                leadingIndex = queryAns[0]
                mostRecentVote = queryAns[1]
                leadingPerson = personId
            }
        }
    })
    return leadingPerson
};

TopVotedCandidate.prototype.bSearch = function(votes,t) {
    let foundIndex = -1
    let mostRecentVote = -1
    let low = 0
    let high = votes.length - 1
    while(low <= high){
        let mid = Math.floor((low + high ) / 2)
        // let mid = ((low + high ) / 2)
        // console.log(mid)
        if(votes[mid] === t){
            foundIndex = mid
            mostRecentVote = votes[mid]
            break
        } else if ( votes[mid] < t) {
            foundIndex = Math.max(foundIndex,mid)
            mostRecentVote = Math.max(mostRecentVote,votes[mid])
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    // Gotta return an array : not an object here
    return [foundIndex,mostRecentVote]
}


/** 
 * Your TopVotedCandidate object will be instantiated and called as such:
 * var obj = new TopVotedCandidate(persons, times)
 * var param_1 = obj.q(t)
 */
