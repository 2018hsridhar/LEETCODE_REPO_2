'''
1146. Snapshot Array
URL := https://leetcode.com/problems/snapshot-array/description/

Categories : Binary search
Do other DS&A structures follow snapshotting?

Complexity
C := #-calls made ( to insert or snap ) 
N := len(arr)
Time = O(ClgN)
Space = O(N) ( Explicit )
O(1) ( Implicit ) 
'''
class SnapshotArray:

    # Init each element equals 0 
    def __init__(self, length: int):
        self.snap_id = 0
        baseRecord = [0,0]
        self.baseArr = [[baseRecord] for idx in range(length)]

    def set(self, index: int, val: int) -> None:
        record = [self.snap_id,val]
        targetList = self.baseArr[index]
        [latest_snap_id, latestVal] = targetList[-1]
        if(latest_snap_id == self.snap_id):
            del targetList[-1]
        targetList.append(record)

    def snap(self) -> int:
        init_snap_id = self.snap_id
        self.snap_id += 1
        return init_snap_id

    # never negative one : snap_id a monotonically increasing value
    # get values closest to, or exactly equal, to snap_id ( leveraging binary search ) 
    def get(self, index: int, snap_id: int) -> int:
        targetVal = float('inf')
        records = self.baseArr[index]
        low = 0
        high = len(records) - 1
        while(low <= high):
            mid = (int)(0.5 * ( low + high))
            [cur_snap_id, cur_snap_val] = records[mid]
            if(cur_snap_id > snap_id):
                high = mid - 1
            elif(cur_snap_id < snap_id):
                targetVal = cur_snap_val
                low = mid + 1
            elif(cur_snap_id == snap_id):
                targetVal = cur_snap_val
                break
        return targetVal


        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
