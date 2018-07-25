# Sum Lists

You have two numbers represented by a linked list, where each node contains a single digit.The digits are stored in reverse order, such that the 1's digit is at the head of the list.Write a function that adds the two numbers and returns the sum as a linked list.

Time Complexity: O\(m + n\)

```python
import math # only used for log function

def sum_lists(one, two):
    number_one = 0
    count = 0
    while (one != None):
        number_one += one.value * (10 ** count)
        count += 1
        one = one.next

    number_two = 0
    count = 0
    while (two != None):
        number_two += two.value * (10 ** count)
        count += 1
        two = two.next
    
    number_out = number_one + number_two
    digits = int(math.log10(number_out))
    current = None
    for i in range(0, digits + 1):
        previous = Node(int(number_out / (10 ** (digits - i))))
        previous.next = current
        current = previous
        number_out -= int(number_out / (10 ** (digits - i))) * (10 ** (digits - i))
    return current
```

