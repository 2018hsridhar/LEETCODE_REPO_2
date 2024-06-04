/*
18. 4Sum
URL := https://leetcode.com/problems/4sum/

BLEH the amount of code written in Java8+e compared to the verbosity of Pythonic Code
Also the need for using an additional set to serve as a hashing structure here
At least it's solutioned now :-) 

*/
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) 
    {
        Arrays.sort(nums);
        return optimalSol(nums, (double)target);    
    }
    	
    private static List<List<Integer>> optimalSol(int[] A, double targetSum)
	{
        Set<String> uniqKeys = new HashSet<String>();
		List<List<Integer>> quadruplets = new ArrayList<List<Integer>>();
		int n = A.length;
		for(int i = 0; i < n; ++i)
		{
			// O(N) from here
			for(int j = i+1; j < n; ++j)
			{
				double leftSum = (double)(A[i]) + (double)(A[j]);
				double subSum = (double)(targetSum) - (double)(leftSum);
				// Execute the 2SUM algorithm here
				int low = j+1;
				int high = n-1;
				int leftPtr = low;
				int rightPtr = high;
				while(leftPtr < rightPtr)	// halt at equality or >, due to two distinct values property
				{
					double curSum = (double)(A[leftPtr]) + (double)(A[rightPtr]);
                    String keyHash = A[i] + "-" + A[j] + "-" + A[leftPtr] + "-" + A[rightPtr];
					if(curSum == subSum && !uniqKeys.contains(keyHash))
					{
                        uniqKeys.add(keyHash);
						List<Integer> quad = new ArrayList<Integer>();
                        quad.add(A[i]);
                        quad.add(A[j]);
                        quad.add(A[leftPtr]);
                        quad.add(A[rightPtr]);
						quadruplets.add(quad);
						++leftPtr;
						--rightPtr;
					}
					else if ( curSum < subSum )
					{
						++leftPtr;
					}
					else
					{
						--rightPtr;
					}
				}
			}
		}
		return quadruplets;
	}
}
