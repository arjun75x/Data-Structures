# Intersection

Given two singly linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list list is the exact same node \(by reference\) as the jth node of the second linked list, then they are intersecting.

Time Complexity: O\(m + n\)

```python
def intersection(one, two):
    one_head = one
    one_tail = one
    one_length = 0
    while (one_tail != None):
        one_tail = one_tail.next
        one_length += 1
    
    two_head = two
    two_tail = two
    two_length = 0
    while (two_tail != None):
        two_tail = two_tail.next
        two_length += 1
    
    if (one_tail != two_tail):
        return None
    
    difference = abs(one_length - two_length)
    if (one_length > two_length):
        for i in range(0, difference):
            one_head = one_head.next
    else:
        for i in range(0, difference):
            two_head = two_head.next
    
    while (one_head != None):
        if (one_head == two_head):
            return one_head
        else:
            one_head = one_head.next
            two_head = two_head.next
```

