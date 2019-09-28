### [geeksforgeeks](https://www.geeksforgeeks.org/function-decorators-in-python-set-1-introduction/)

#### Option 1 - Use decorator

```
import sys, threading
import os
import math

def READ(fileName):
    script_dir = os.path.dirname(__file__)
    username = "trifiasco"
    if username in script_dir:
        sys.stdin = open(script_dir + '/' + fileName, 'r')

def momoize(f):
    dp = {}

    def inner(num, a, b, c):
        if num not in dp:
            dp[num] = f(num, a, b, c)
        return dp[num]
    return inner

@momoize
def solve(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -4010

    ans = max({1 + solve(n - a, a, b, c), 1 + solve(n - b, a, b, c), 1 + solve(n - c, a, b, c)})
    return ans

def main():
    READ('in.txt')
    while True:
        try:
            n, a, b, c = map(int, input().split())
        except EOFError:
            break

        res = solve(n, a, b, c)
        print(res)
    pass

if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    threading.stack_size(10240000)
    thread = threading.Thread(target=main)
    thread.start()

```

#### Option 2 - Use class

```
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        #Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]

def factorial(k):
    if k < 2: return 1
    return k * factorial(k - 1)

factorial = Memoize(factorial)

```

##### Option 2.1 - with both decorator and class
```
@Memoize
def factorial(k):
    if k < 2: return 1
    return k * factorial(k - 1)
```

#### Option 3 - Resettable memoization [SO link](https://stackoverflow.com/questions/4927323/what-can-be-done-to-speed-up-this-memoization-decorator)

```
import functools
import weakref

class Memoized(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.

    >>> counter = 0
    >>> @Memoized
    ... def count():
    ...     global counter
    ...     counter += 1
    ...     return counter

    >>> counter = 0
    >>> Memoized.reset()
    >>> count()
    1
    >>> count()
    1
    >>> Memoized.reset()
    >>> count()
    2

    >>> class test(object):
    ...     @Memoized
    ...     def func(self):
    ...         global counter
    ...         counter += 1
    ...         return counter
    >>> testobject = test()
    >>> counter = 0
    >>> testobject.func()
    1
    >>> testobject.func()
    1
    >>> Memoized.reset()
    >>> testobject.func()
    2
    """

    caches = weakref.WeakSet()

    def __init__(self, func):
        self.func = func
        self.cache = {}
        Memoized.caches.add(self)

    def __call__(self, *args):
      try:
          return self.cache[args]
      except KeyError:
          value = self.func(*args)
          self.cache[args] = value
          return value
      except TypeError:
          # uncachable -- for instance, passing a list as an argument.
          # Better to not cache than to blow up entirely.
          return self.func(*args)

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)

    @staticmethod
    def reset():
        for memo in Memoized.caches:
            memo.cache = {}

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```