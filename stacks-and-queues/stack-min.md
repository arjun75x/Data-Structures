# Stack Min

How would you design a stack which, in addition to push and pop, has a function min\_value which returns the minimum element. All functions should operate in O\(1\) time

```python
import math
class StackMin():
    def __init__(self):
        self.data = []
        self.min_value = math.inf
        self.min_stack = []

    def pop(self):
        if (self.data[-1] is self.min_value):
            self.min_stack.pop()
            self.min_value = self.min_stack[len(self.min_stack) - 1]
        return self.data.pop()

    def push(self, item):
        self.data.append(item)
        if (item < self.min_value):
            self.min_value = item
            self.min_stack.append(item)

    def peek(self):
        return self.data[-1]
    
    def isEmpty(self):
        return self.data == []
    
    def get_min(self):
        return self.min_value
```

