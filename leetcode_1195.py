# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
'''
URL := https://leetcode.com/problems/fizz-buzz-multithreaded/
1195. Fizz Buzz Multithreaded
Single Atomic Counter - no lost updates
13 mins and solved :-)

All threads called externally ( and respawned up on crash ) 

'''
import threading

class FizzBuzz:
    # How to get calls going up ( dispatch threads ) ( until condition met ) 
    # Ok
    def __init__(self, n: int):
        self.n = n
        # Shared counter ( instance var )
        self.sharedCounter = 1
        # Lock to protect the counter
        self.sharedCounterLock = threading.Lock()  # lock to protect self.counter

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        # Release lock if exception/thread crash ( woah ) 
        while(self.sharedCounter <= self.n):
            with self.sharedCounterLock:
                # only on thread @ a time
                if(self.sharedCounter % 3 == 0 and self.sharedCounter % 5 != 0):
                    printFizz()
                    self.sharedCounter += 1
    	

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while(self.sharedCounter <= self.n):
            with self.sharedCounterLock:
            # only on thread @ a time
                if(self.sharedCounter <= self.n and self.sharedCounter % 3 != 0 and self.sharedCounter % 5 == 0):
                    printBuzz()
                    self.sharedCounter += 1
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while(self.sharedCounter <= self.n):
            with self.sharedCounterLock:
            # only on thread @ a time
                if(self.sharedCounter <= self.n and self.sharedCounter % 3 == 0 and self.sharedCounter % 5 == 0):
                    printFizzBuzz()
                    self.sharedCounter += 1
    	

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while(self.sharedCounter <= self.n):
            with self.sharedCounterLock:
            # only on thread @ a time
                if(self.sharedCounter <= self.n and self.sharedCounter % 3 != 0 and self.sharedCounter % 5 != 0):
                    printNumber(self.sharedCounter )
                    self.sharedCounter += 1
    	
```
