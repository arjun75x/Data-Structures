# Partition

Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list,the values of x only need to be after the elements less than x.

Time Complexity: O\(n\)

```python
def partition(head, partition_value):
    before_head = None
    before_tail = None
    after_head = None
    after_tail = None
    current = head
    while (current != None):
        if (current.value < partition_value):
            if (before_head):
                before_tail.next = current
                before_tail = before_tail.next
                current = before_tail
            else:
                before_head = current
                before_tail = current
        else:
            if (after_head):
                after_tail.next = current
                after_tail = after_tail.next
                current = after_tail
            else:
                after_head = current
                after_tail = current
        current = current.next
    after_tail.next = None
    before_tail.next = after_head
    return before_head
```

