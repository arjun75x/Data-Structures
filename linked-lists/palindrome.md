# Palindrome

Implement a function to check if a linked list is a palindrome

Time Complexity: O\(n\)

```python
def palindrome(head):
    stack = []
    current = head
    while (current != None):
        stack.append(current.value)
        current = current.next

    current = head
    while (current != None):
        if (current.value != stack.pop()):
            return False
        current = current.next
    return True
```

