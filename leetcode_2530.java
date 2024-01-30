/*
URL := https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/
2530. Maximal Score After Applying K Operations

This question is basically just a max heap in the hiding
Maximization(value) after finite bounded number of operations


java.lang.Math -> part of the ,lang> package here
*/
class Solution {
    public long maxKelements(int[] nums, int k) {
        long maxScore = 0;
        // Appreciating numerics being objects -> enables the .compareTo() methods :-)
        PriorityQueue<Double> maxHeap = new PriorityQueue<Double>((a,b) -> { return b.compareTo(a); } );
        for(int num : nums){
            maxHeap.add((double)(num));
        }
        for(int a = 0; a < k; a++){
            double maxVal = maxHeap.poll();
            maxScore += (long)(maxVal);
            double pushVal = Math.ceil(maxVal / 3.0); //ceil takes us to an int anyways
            maxHeap.add(pushVal);
        }
        return maxScore;
    }
}
