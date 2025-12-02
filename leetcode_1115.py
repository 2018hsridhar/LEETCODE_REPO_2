'''
URL := https://leetcode.com/problems/print-foobar-alternately/
1115. Print FooBar Alternately
Turn based mechanism - 10 mintues - passed
Mutexes can't force a serialized threading order
'''
import threading
import time

class FooBar:
    def __init__(self, n):
        self.n = n
        self.turn = True  # True: Thread 1's turn, False: Thread 2's turn
        self.condition = threading.Condition()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.condition:
                while not self.turn:
                    self.condition.wait()
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.turn = False
                self.condition.notify()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                while self.turn:
                    self.condition.wait()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.turn = True
                self.condition.notify()
