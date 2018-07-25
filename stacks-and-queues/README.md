# Stacks and Queues

All Problems related to Stacks and Queues

Stack Class:

```python
class Stack():
    def __init__(self):
        self.data = []

    def pop(self):
        return self.data.pop()

    def push(self, item):
        self.data.append(item)

    def peek(self):
        return self.data[-1]
    
    def isEmpty(self):
        return self.data == []
```

Queue Class:

```python
class Queue():
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.insert(0,item)

    def dequeue(self):
        return self.data.pop()

    def peek(self):
        return self.data[0]
    
    def isEmpty(self):
        return self.data == []
```

