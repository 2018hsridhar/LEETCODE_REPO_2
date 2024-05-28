'''
URL := https://leetcode.com/problems/lru-cache/
146. LRU Cache

Category : Tapes, DLL, Counting, HashMaps, Ordering, Monotonicity of Keys

Test Cases :
(A)
(B)
(C)
(D)
(E)

30 minutes to solutioning
Some caches are version-history based :-)

'''
class LRUCache:

    def __init__(self, capacity: int):
        self.kvMap = dict()
        self.kvVersion = dict()
        self.tape = []
        self.capacity = capacity
        self.numCurKeys = 0

    # Wooh {-1 or trueValue return safety }
    def get(self, key: int) -> int:
        keyValue = -1
        if key in self.kvMap:
            keyValue = self.kvMap[key]
            curVersion = self.kvVersion[key]
            nextVersion = curVersion + 1
            self.tape.append([key,nextVersion])
            self.kvVersion[key] = nextVersion
        return keyValue

    # Two different behaviors key put calls
    def put(self, key: int, value: int) -> None:
        curVersion = 0
        if key not in self.kvMap:
            if(self.numCurKeys == self.capacity):
                # remove LRU key
                while(len(self.tape) > 0):
                    curEntry = self.tape.pop(0)
                    curKey = curEntry[0]
                    histVersion = curEntry[1]
                    latestVersion = self.kvVersion[curKey]
                    if(histVersion == latestVersion):
                        # is the key to remove
                        del self.kvVersion[curKey]
                        del self.kvMap[curKey]
                        self.numCurKeys -= 1
                        break
                    # implicit else to always remove
            self.numCurKeys += 1
            self.kvVersion[key] = 1
        else:
            curVersion = self.kvVersion[key]
            self.kvVersion[key] += 1
        self.kvMap[key] = value
        nextVersion = curVersion + 1
        self.tape.append([key,nextVersion])

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
