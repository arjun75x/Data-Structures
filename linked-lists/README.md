# Linked Lists

All Problems related to Linked Lists

```python
# Class for Linked List Nodes
class Node():

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    
    def string(self):
        out = ""
        while (self != None):
            out += str(self.value) + " "
            self = self.next
        return out
```

