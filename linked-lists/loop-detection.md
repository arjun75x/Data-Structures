# Loop Detection

Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop

Time Complexity: O\(n\) if no loop

```python
def loop_detection(head):
    slow = head
    fast = head
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if (slow == fast):
            break

    if (fast is None or fast.next is None):
        return None

    slow = head
    while (slow != fast):
        slow = slow.next
        fast = fast.next
    return fast
```

