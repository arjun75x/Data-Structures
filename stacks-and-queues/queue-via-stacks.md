# Queue via Stacks

Implement a MyQueue class which implements a queue using two stacks

```python
class QueueViaStacks():
    def __init__(self):
        self.one = Stack()
        self.two = Stack()
    
    def enqueue(self, value):
        self.one.push(value)
    
    def dequeue(self):
        while not self.one.isEmpty():
            self.two.push(self.one.pop())
        out = self.two.pop()
        while not self.two.isEmpty():
            self.one.push(self.two.pop())
        return out
    
    def isEmpty(self):
        return self.one.isEmpty
    
    def peek(self):
        while not self.one.isEmpty():
            self.two.push(self.one.pop())
        out = self.two.peek()
        while not self.two.isEmpty():
            self.one.push(self.two.pop())
        return out
```

