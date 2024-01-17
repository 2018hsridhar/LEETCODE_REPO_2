/*
URL := https://leetcode.com/problems/design-memory-allocator/description/
2502. Design Memory Allocator

For now, we'll be more effiicent and avoid decent data structures
In actual practice, we should strive for efficiency when dealing with contiguous blocks of memory.


*/
class Allocator {
    Map<Integer,HashSet<int[]>> myAllocations;
    int[] myMemory;
    public Allocator(int n) {
        this.myMemory = new int[n];
        this.myAllocations = new HashMap<Integer,HashSet<int[]>>();
        // https://stackoverflow.com/questions/2154251/any-shortcut-to-initialize-all-array-elements-to-zero
        // Save on loop with default initialization of primitives (in JAVA )
    }
    
    public int allocate(int size, int mID) {
        if(!this.myAllocations.containsKey(mID)){
            this.myAllocations.put(mID, new HashSet<int[]>());
        }
        int blockFirstIndex = -1; // if memory block exists or not
        int curFreeSizeAvail = 0;
        for(int i = 0; i < this.myMemory.length; i++){ // scope for variable access patterns here
            if(this.myMemory[i] == 0){ // hit free memory
                curFreeSizeAvail++;
                if(curFreeSizeAvail == size){
                    int leftIdx = i - curFreeSizeAvail + 1;
                    int rightIdx = i;
                    blockFirstIndex = leftIdx;
                    myAllocations.get(mID).add(new int[]{leftIdx,rightIdx});
                    for(int j = rightIdx; j >= leftIdx; j--){
                        this.myMemory[j] = mID; // memory write operation
                    }
                    break;
                }
            } else {
                curFreeSizeAvail = 0;
            }
        }
        return blockFirstIndex;
    }
    
    // If only types were more compatible with one another
    /// gaaah TLE here
    public int free(int mID) {
        int unitFreeded = 0;
        if(this.myAllocations.containsKey(mID)){
            Set<int[]> myMIDAllocs = this.myAllocations.get(mID);
            // Enhacenced for loop Java 5 
            for(int[] allocRange : myMIDAllocs){
                for(int i = allocRange[0]; i <= allocRange[1]; i++){
                    this.myMemory[i] = 0;
                }
                unitFreeded += allocRange[1] - allocRange[0] + 1;
            }
            // remove key operation too!
            this.myAllocations.remove(mID);
        }
        return unitFreeded;
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator obj = new Allocator(n);
 * int param_1 = obj.allocate(size,mID);
 * int param_2 = obj.free(mID);
 */
