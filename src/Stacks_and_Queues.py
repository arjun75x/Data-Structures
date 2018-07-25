class Stack():
    def __init__(self):
        self.data = []

    def pop(self):
        return self.data.pop()

    def push(self, item):
        self.data.append(item)

    def peek(self):
        return self.data[-1]
    
    def isEmpty(self):
        return self.data == []

class Queue():
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.insert(0,item)

    def dequeue(self):
        return self.data.pop()

    def peek(self):
        return self.data[0]
    
    def isEmpty(self):
        return self.data == []

"""
Describe how you could use a single array to implement three stacks
"""
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

"""
How would you design a stack which, in addition to push and pop, has a function min_value
which returns the minimum element. All functions should operate in O(1) time
"""
import math
class StackMin():
    def __init__(self):
        self.data = []
        self.min_value = math.inf
        self.min_stack = []

    def pop(self):
        if (self.data[-1] is self.min_value):
            self.min_stack.pop()
            self.min_value = self.min_stack[len(self.min_stack) - 1]
        return self.data.pop()

    def push(self, item):
        self.data.append(item)
        if (item < self.min_value):
            self.min_value = item
            self.min_stack.append(item)

    def peek(self):
        return self.data[-1]
    
    def isEmpty(self):
        return self.data == []
    
    def get_min(self):
        return self.min_value

"""
Imagine a stack of plates. If the stack gets too high, it might topple. Therefore, in real life, 
we would likely start a new stack when the previous stack exceeds some threshold. Implement a data 
structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should 
create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() 
should  behave identically to a single stack.
"""
class SetOfStacks():
    def __init__(self, threshold):
        self.data = []
        self.top = threshold
    
    def push(self, value):
        if (len(self.stacks) == 0) or (len(self.stacks[-1]) == self.top):
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if len(self.stacks) == 0:
            return None
        data = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return data

    def peek(self):
        if len(self.stacks) == 0:
            return None
        return self.data[-1][-1]
    
    def isEmpty(self):
        return self.data == []

"""
Implement a MyQueue class which implements a queue using two stacks
"""
class QueueViaStacks():
    def __init__(self):
        self.one = Stack()
        self.two = Stack()
    
    def enqueue(self, value):
        self.one.push(value)
    
    def dequeue(self):
        while not self.one.isEmpty():
            self.two.push(self.one.pop())
        out = self.two.pop()
        while not self.two.isEmpty():
            self.one.push(self.two.pop())
        return out
    
    def isEmpty(self):
        return self.one.isEmpty
    
    def peek(self):
        while not self.one.isEmpty():
            self.two.push(self.one.pop())
        out = self.two.peek()
        while not self.two.isEmpty():
            self.one.push(self.two.pop())
        return out

"""
Write a program to sort a stack such that the smallest items are on the top. 
You can use an additional temporary stack, but you may not copy the elements 
into any other data structure.
"""
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

"""
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
People must adopt either the oldest (based on arrival time) of all animals in the shelter, or they can select
whether they would prefer a dog or a cat and receive the oldest animal of that type. They cannot select which
animal they would like. Create the data structures to maintain this system and implement operations such as enqueue,
dequeueAny, dequeueDog, dequeueCat. You may use the built in LinkedList data structure.
"""
class AnimalShelter():
    class Dog():
        def __init__(self, name):
            self.name = name
    class Cat():
        def __init__(self, name):
            self.name = name

    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()
        self.queue = Queue()

    def enqueue(self, animal):
        self.queue.enqueue(animal)
        if (type(animal) is AnimalShelter.Dog):
            self.dog_queue.enqueue(animal)
        else:
            self.cat_queue.enqueue(animal)

    def dequeueAny(self):
        temp = self.queue.dequeue
        if (type(temp) is AnimalShelter.Dog):
            self.dog_queue.dequeue()
        else:
            self.cat_queue.dequeue()
        return temp
    
    def dequeueDog(self):
        out = self.dog_queue.dequeue()
        temp = self.queue.dequeue()
        if (type(temp) is AnimalShelter.Dog):
            return out
        else:
            new_queue = Queue()
            new_queue.enqueue(temp)
            while (not self.queue.isEmpty()):
                temp = self.queue.dequeue
                if (type(temp) is AnimalShelter.Dog):
                    break
                else:
                    new_queue.enqueue(temp)
            while (not self.queue.isEmpty()):
                new_queue.enqueue(self.queue.dequeue())
            self.queue = new_queue
        return out
    
    def dequeueCat(self):
        out = self.cat_queue.dequeue()
        temp = self.queue.dequeue()
        if (type(temp) is AnimalShelter.Cat):
            return out
        else:
            new_queue = Queue()
            new_queue.enqueue(temp)
            while (not self.queue.isEmpty()):
                temp = self.queue.dequeue
                if (type(temp) is AnimalShelter.Cat):
                    break
                else:
                    new_queue.enqueue(temp)
            while (not self.queue.isEmpty()):
                new_queue.enqueue(self.queue.dequeue())
            self.queue = new_queue
        return out