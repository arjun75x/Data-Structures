# Delete Middle Node

Implement an algorithm to delete a node in the middle \(i.e any node but the first and last node, not necessarily the exact middle\) of a singly linked list, given only access to that node

Time Complexity: O\(1\)

```python
def delete_middle_node(middle):
    if (middle is None or middle.next is None):
        raise Exception("Not a middle node")
    middle.value = middle.next.value
    middle.next = middle.next.next
```

