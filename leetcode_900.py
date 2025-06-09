# Intuition and Approach
We already have a good encoding array, the meat of the problem lies in the decoding steps.

# Complexity
$$N = len(input)$$

- Time complexity:
$$T = O(N)$$

- Space complexity:
$$S = O(N)$$ ( Explicit ) $$O(1)$$ ( Implicit ) 

# Code
```python3 []
'''
URL := https://leetcode.com/problems/rle-iterator/description/
900. RLE Iterator
'''
class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.ptr = 0  # Pointer to the current frequency

    def next(self, n: int) -> int:
        while self.ptr < len(self.encoding) and n > 0:
            freq = self.encoding[self.ptr]
            if n > freq:
                n -= freq
                self.ptr += 2
            else:
                self.encoding[self.ptr] -= n
                return self.encoding[self.ptr + 1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
```
