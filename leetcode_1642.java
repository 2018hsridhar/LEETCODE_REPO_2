/*
URL := https://leetcode.com/problems/furthest-building-you-can-reach/description/
1642. Furthest Building You Can Reach

PQ based solution : track the max building that we cover
Check invariant : #-stones >= remainingBuildingHeight sum
Invariant : must proceed left to right

Complexity
T = O(N)
S = O(N) ( E ) O(1) ( I ) 
N = #-buildings

Note : can have a case of 0 bricks too ( exert caution ) -> single el PQ case
Sol right for 1 ladder -> extend to multiple

*/
class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        int furthest = 0;
        int n = heights.length;
        int runBuildSum = 0;
        int pqSum = 0;
        // PriorityQueue<Integer> pq =new PriorityQueue<>((x, y) -> Integer.compare(y, x));
        PriorityQueue<Integer> pq =new PriorityQueue<>((x, y) -> Integer.compare(x, y));
        // Second running PQ ( for the ladders now )? ( or a given length ) 
        // Original PQ ( still contains all my other elements )
        // But we use the running sum -> why not just use pq for only the ladders too ( evict maxEl if a greater max El is found )?
        for(int i = 0; i < n - 1; i++){
            int curBuild = heights[i];
            int nextBuild = heights[i+1];
            if(curBuild < nextBuild){
                // use a ladder or a brick case
                int delta = Math.abs(nextBuild - curBuild);
                runBuildSum += delta;
                if(ladders > 0){
                    if(pq.size() < ladders){
                        pq.add(delta);
                        pqSum += delta;
                    } else if ( pq.size() >= ladders){
                        // min heap : insert maximal els if > minnest el
                        if(delta > pq.peek()){
                            pqSum -= pq.poll();
                            pq.add(delta);
                            pqSum += delta;
                        }
                    }
                }
                int remEls = runBuildSum - pqSum;
                if(remEls <= bricks){ // case : bricks = 5, buildings = { 2, 3, 5 }
                    furthest++;
                } else {
                    break;
                }
            } else {
                furthest++; // proceed as usual
            }
        }     
        return furthest;
    }
}
