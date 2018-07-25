# Sort Stack

Write a program to sort a stack such that the smallest items are on the top.You can use an additional temporary stack, but you may not copy the elements into any other data structure.

```python
def sort_stack(stack):
    sorted_stack = Stack()
    sorted_stack.push(stack.pop())
    while not stack.isEmpty():
        if (stack.peek() < sorted_stack.peek()):
            sorted_stack.push(stack.pop())
        else:
            count = 0
            temp = stack.pop()
            while (not sorted_stack.isEmpty() and temp > sorted_stack.peek()):
                count += 1
                stack.push(sorted_stack.pop())
            sorted_stack.push(temp)
            for i in range(count):
                sorted_stack.push(stack.pop())
    return sorted_stack
```

