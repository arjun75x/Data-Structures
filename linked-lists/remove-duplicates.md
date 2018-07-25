# Remove Duplicates

Write code to remove duplicates from an unsorted linked list

Time Complexity: O\(n\)

```python
def remove_duplicates(head):
    unique_values = set()
    current = head
    unique_values.add(head.value)
    while (current.next != None):
        if current.next.value in unique_values:
            current.next = current.next.next
        else:
            unique_values.add(current.next.value)
            current = current.next
```



