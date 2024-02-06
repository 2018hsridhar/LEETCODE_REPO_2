/**
 * @param {string} kingName
 */
 /*
 URL := https://leetcode.com/problems/throne-inheritance/description/
 1600. Throne Inheritance

 In-order tree traversal with nice maps too!
 Biggest difficulty was reading the word problem ; the actual coding is easy!
 */

// Default params even work
// Default params make extensibile constructors
var Node = function(name,left = null,right = null,parent=null,isDead=false){
    this.name = name
    this.children = []
    this.parent = parent
    this.isDead = isDead
}

var ThroneInheritance = function(kingName) {
    this.lookup = new Map()
    let kingNode = new Node(kingName)
    this.lookup.set(kingName, kingNode)
    this.root = kingNode
};

/** 
 * @param {string} parentName 
 * @param {string} childName
 * @return {void}
 */
ThroneInheritance.prototype.birth = function(parentName, childName) {
    // parent name guaranteed to be alive
    let parentNode = this.lookup.get(parentName)
    let childNode = new Node(childName,null,null,parentNode)
    parentNode.children.push(childNode)
    this.lookup.set(childName,childNode)
};

/** 
 * @param {string} name
 * @return {void}
 */
ThroneInheritance.prototype.death = function(name) {
    this.lookup.get(name).isDead = true
};

/**
 * @return {string[]}
 */
ThroneInheritance.prototype.getInheritanceOrder = function() {
    // the in order traversal
    let order = []
    let stk = [this.root]
    while(stk.length > 0) {
        let parent = stk.pop()
        if(!parent.isDead){
            order.push(parent.name)
        }
        // reverse iterate over the Nodes
        // Pushes right->left : stk contnets [ rightMostNode, leftMostNode]
        // for(let i = children.length - 1; i >= 0; i--){
            // stk.push(children.at(i))
        // Shallow copy not expensive   
        // https://stackoverflow.com/questions/32682962/javascript-loop-through-array-backwards-with-foreach
        parent.children.slice().reverse().forEach((child) => {
            stk.push(child)
        })
    }
    return order
};

/** 
 * Your ThroneInheritance object will be instantiated and called as such:
 * var obj = new ThroneInheritance(kingName)
 * obj.birth(parentName,childName)
 * obj.death(name)
 * var param_3 = obj.getInheritanceOrder()
 */
