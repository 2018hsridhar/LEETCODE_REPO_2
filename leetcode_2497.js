 /*
 2497. Maximum Star Sum of a Graph
 URL := https://leetcode.com/problems/maximum-star-sum-of-a-graph/description/

 Star Graphs as a property of undirected graphs?
 Start graphs := center node >= 0 neighbhors ( common edge properties ) 

 Seems to be a priority queue based problem
 Go through this by the list(edges) only without constructing the actual graph
 Maintain a priority queue of size k : unless we have k elems in PQ, discard it
 Leverage the PQs to track running sums as well
 But track the running sum as we go ( versus compute at end )

 Use PQ dynamic insertions to save on compute and RAM limitations

 */
class Solution {
    public int maxStarSum(int[] vals, int[][] edges, int k) {
        int maxSS = Integer.MIN_VALUE;
        if(k == 0 || edges.length == 0){
            for(int val : vals){
                maxSS = Math.max(val,maxSS);
            }
            return maxSS;
        }
        int n = vals.length;
        Map<Integer,PriorityQueue<Integer>> starVals = new HashMap<Integer,PriorityQueue<Integer>>();
        for(int i = 0; i < n; i++){
            starVals.put(i,new PriorityQueue<Integer>((a,b) -> {return b-a;}));
        }
        // Undirected graph bidirectionality GAAAAH code duplication happening now
        for(int[] edge: edges) {
            int src = edge[0];
            int dst = edge[1];
            int srcVal = vals[src];
            int dstVal = vals[dst];
            starVals.get(src).add(dstVal);
            starVals.get(dst).add(srcVal);
        }
        // Now compute the starSums ( start from init vertex though )
        for(int i = 0; i < n; i++){
            PriorityQueue<Integer> curNodeVals = starVals.get(i);
            int localSS = vals[i];
            maxSS = Math.max(maxSS, localSS);
            for(int a = 0; a < k; a++){
                if(curNodeVals.size() > 0){
                    localSS += curNodeVals.poll();
                    maxSS = Math.max(maxSS, localSS);
                } else {
                    break;
                }
            }
        }
        return maxSS;    
    }
}
