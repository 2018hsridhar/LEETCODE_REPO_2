Intuition
See approach

Approach
Memory allocate a list of length n for handling n elements to insert into the stream.
For each insertion operation, update the index ( with offset of -1 )
On each insertion, calculate the target chunk to return leveraging a sliding pointer. Do not increment the pointer if the curent pointer's element value is not filled with a valid entry. Else, increment and append the element to an array to return back as the target chunk.
Complexity
Let N := #-els to insert into the stream ( also the stream size bound )

Time complexity:

O(N)
Space complexity:

O(N) ( explicit )
O(1) ( implicit call stack )
Code
'''
URL := https://leetcode.com/problems/design-an-ordered-stream/description/
1656. Design an Ordered Stream
Ordered streams frequently show up in eng contexts.

Construct a stream ( a heap ) to take n values
Insert into stream 
Order stream size is known ahead of time
Chunkified-based verification :-O 

'''
class OrderedStream:

    def __init__(self, n: int):
        self.stream = ["" for i in range(n)]
        self.streamPtr = 0

    # ahh evolve the underlying stream ptr
    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        targetChunk = []
        n = len(self.stream)
        while(self.streamPtr < n):
            curStreamEl = self.stream[self.streamPtr] 
            if(len(curStreamEl) == 0):
                break
            # Conditional guarding enables code path correctness.
            targetChunk.append(curStreamEl)
            self.streamPtr += 1
        return targetChunk

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
