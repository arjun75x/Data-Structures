# Return Kth to last

Implement an algorithm to find the Kth to last element of a singly linked list

Time Complexity: O\(n\)

```python
def return_kth_to_last(head, k):
    one_pointer = head
    two_pointer = head
    for i in range(0,k):
        if two_pointer.next:
            two_pointer = two_pointer.next
        else:
            raise Exception("K is larger than list size")
    while (two_pointer.next != None):
        one_pointer = one_pointer.next
        two_pointer = two_pointer.next
    return one_pointer
```

