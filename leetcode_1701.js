/**
 * @param {number[][]} customers
 * @return {number}
 */
 /*
 URL := https://leetcode.com/problems/average-waiting-time/description/
 1701. Average Waiting Time

Emulates a FIFO-based single-threaded CPU :-). 
Also emulates real-world customer-order-service processing problems.
Are threads idle or are they executing a task @ hand.


 */
var averageWaitingTime = function(customers) {
    let wt = 0
    let n = customers.length
    let chefTime = 0
    for(let i = 0; i < n; i++){
        let curCustomer = customers[i]
        let arrivalTime = curCustomer[0]
        let orderProcTime = curCustomer[1]
        if(chefTime <= arrivalTime){
            wt += orderProcTime
            chefTime = arrivalTime // gotta wait for customer anyways
            chefTime += orderProcTime
        } else { // chef time >= arrivalTime : need to wait
            // from my arrival until chef if available : must wait
            let chefDelay = (chefTime - arrivalTime)
            wt += (orderProcTime + chefDelay)
            chefTime += orderProcTime
        }
    }
    let awt = wt / n // Averages : Java math dyn-typed no need for double EXPRS
    return awt
};
