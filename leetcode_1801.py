/**
 * @param {number[][]} orders
 * @return {number}
 */
/*
 URL := https://leetcode.com/problems/number-of-orders-in-the-backlog/
1801. Number of Orders in the Backlog
Market orders placed in batches @ given prices.
Greedy look -> largestPriceBuy,smallestPriceSell
Both sides are auction market driven.
Do these buy-sell order backlogs ever clear up?

Steps
(A) Match the order
(B) Execute the order
(C) Remove the order from the backlog OR add the order to the baclog

 Stock markets driven by order backlogs and PME : Price Matching Engine
 number backlog orders = num(buy_backlog) + num(sell_backlog)
 Markets prioritize the buy and sell orders


 */
class Solution {

    public int getNumberOfBacklogOrders(int[][] orders) {
        long numberBacklogOrders = 0;
        // https://stackoverflow.com/questions/683041/how-do-i-use-a-priorityqueue
        // Lambda Expr Java 8 inlining custom comparators for dstructures
        PriorityQueue<int[]> buyBacklog = new PriorityQueue<int[]>((a,b) -> b[0] - a[0]);
        PriorityQueue<int[]> sellBacklog = new PriorityQueue<int[]>((a,b) -> a[0] - b[0]);
        for(int[] order: orders) {
            int orderType = order[2];
            if(orderType == 0) { // batch of buy orders
                // Own function : repeat code here
                if(sellBacklog.size() == 0){
                    buyBacklog.add(order);
                } else if ( sellBacklog.size() > 0) {
                    boolean addOrder = true;
                    while(order[1] > 0 && sellBacklog.size() > 0){
                        int[] bestSell = sellBacklog.remove();
                        // Potential bug here ( with future in lines 61-62 )
                        if(bestSell[0] > order[0]) {
                            buyBacklog.add(order);
                            sellBacklog.add(bestSell);
                            addOrder = false;
                            break; // sell orders all higher than buy
                        } else {
                            int numOrdersExec = Math.min(bestSell[1], order[1]);
                            order[1] -= numOrdersExec;
                            bestSell[1] -= numOrdersExec;
                            if(bestSell[1] > 0) { // we did not sell them all here
                                sellBacklog.add(bestSell);
                                break;
                            }
                        }
                    }
                    if(addOrder && order[1] > 0){ // still orders to buy after decrs
                        buyBacklog.add(order);
                    }
                }
            } else if ( orderType == 1) { // batch of sell orders
                if(buyBacklog.size() == 0){
                    sellBacklog.add(order);
                } else if ( buyBacklog.size() > 0) {
                    boolean addOrder = true;
                    while(order[1] > 0 && buyBacklog.size() > 0){
                        int[] bestBuy = buyBacklog.remove();
                        if(bestBuy[0] < order[0]) {
                            addOrder = false;
                            sellBacklog.add(order);
                            buyBacklog.add(bestBuy);
                            break; // buy orders are less than current sell order : no profit
                        } else {
                            int numOrdersExec = Math.min(bestBuy[1], order[1]);
                            // System.out.printf("Num sell exec = %d\n", numOrdersExec);
                            order[1] -= numOrdersExec;
                            bestBuy[1] -= numOrdersExec;
                            if(bestBuy[1] > 0) { // we did not sell them all here
                                // System.out.println("Still have old buy");
                                buyBacklog.add(bestBuy);
                                break;
                            }
                        }
                    }
                    if(addOrder && order[1] > 0){ // still orders to buy after decrs
                        sellBacklog.add(order);
                    }
                }
            }
        }
        // Get remaining buy-sell amounts in market backlogs
        Iterator<int[]> pqItr;
        pqItr = buyBacklog.iterator();
        while(pqItr.hasNext()){
            int[] buyOrder = pqItr.next();
            numberBacklogOrders += (long)(buyOrder[1]);
        }
        // reassignation of iterators
        pqItr = sellBacklog.iterator();
        while(pqItr.hasNext()){
            int[] sellOrder = pqItr.next();
            numberBacklogOrders += (long)(sellOrder[1]);
        }
        long modulo = (long)(Math.pow(10,9) + 7);
        numberBacklogOrders = numberBacklogOrders % modulo;
        return (int)(numberBacklogOrders); // overflow long->int
    }
}

