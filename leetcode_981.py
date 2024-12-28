'''
981. Time Based Key-Value Store
URL := https://leetcode.com/problems/time-based-key-value-store/description/

Multiple values, same key, diff time
We can set a time value -> heap or sort . Careful
    Ok monoIncr timestamps :-)

Complexity

'''
class TimeMap:

    def __init__(self):
        self.valueTimes = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.valueTimes):
            self.valueTimes[key] = []
        record = [timestamp,value]
        self.valueTimes[key].append(record)        

    def get(self, key: str, timestamp: int) -> str:
        targetValue = ""
        if(key in self.valueTimes):
            records = self.valueTimes[key]
            low = 0
            high = len(records) - 1
            while(low <= high):
                mid = (int)(0.5 * (low + high))
                targetRecord = records[mid]
                timeAtMid = targetRecord[0]
                if(timeAtMid > timestamp):
                    high = mid - 1
                elif(timeAtMid < timestamp):
                    targetValue = targetRecord[1]
                    low = mid + 1
                else:
                    targetValue = targetRecord[1]
                    break
        return targetValue

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
