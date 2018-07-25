# Set of Stacks

Imagine a stack of plates. If the stack gets too high, it might topple. Therefore, in real life,we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push\(\) and SetOfStacks.pop\(\)should behave identically to a single stack.

```python
class SetOfStacks():
    def __init__(self, threshold):
        self.data = []
        self.top = threshold
    
    def push(self, value):
        if (len(self.stacks) == 0) or (len(self.stacks[-1]) == self.top):
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if len(self.stacks) == 0:
            return None
        data = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return data

    def peek(self):
        if len(self.stacks) == 0:
            return None
        return self.data[-1][-1]
    
    def isEmpty(self):
        return self.data == []
```

