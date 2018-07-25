# Three Stacks

Describe how you could use a single array to implement three stacks

```python
class ThreeStacks():
    def __init__(self, size):
        fixed_array = [None for i in range(3 * size)]
        self.stack_one = fixed_array[0 : size]
        self.stack_two = fixed_array[size : 2 * size]
        self.stack_three = fixed_array[2 * size : 3 * size]
        self.top_one = 0
        self.top_two = size
        self.top_three = 2 * size
    
    def determine_stack(self, stack_number):
        if (stack_number is 1):
            return self.stack_one
        elif (stack_number is 2):
            return self.stack_two
        elif (stack_number is 3):
            return self.stack_three
        else:
            raise Exception("Stack number invalid")

    def determine_top(self, stack_number):
        if (stack_number is 1):
            return self.top_one
        elif (stack_number is 2):
            return self.top_two
        elif (stack_number is 3):
            return self.top_three
        else:
            raise Exception("Stack number invalid")

    def pop(self, stack_number):
        stack = self.determine_stack(stack_number)
        top = self.determine_top(stack_number)
        if (stack[top] is None):
            return
        elif (top is (stack_number - 1) * len(stack)):
            temp = stack[top]
            stack[top] = None
            return temp
        else:
            temp = stack[top]
            stack[top] = None
            top -= 1
            return temp

    def push(self, stack_number, value):
        stack = self.determine_stack(stack_number)
        top = self.determine_top(stack_number)
        if (stack[top] is None):
            stack[top] = value
        else:
            top += 1
            stack[top] = value
    
    def peek(self, stack_number):
        stack = self.determine_stack(stack_number)
        top = self.determine_top(stack_number)
        return stack[top]
    
    def isEmpty(self, stack_number):
        stack = self.determine_stack(stack_number)
        top = self.determine_top(stack_number)
        if (stack[top] is None):
            return True
        return False
```

