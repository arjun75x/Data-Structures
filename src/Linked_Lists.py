# Class for Linked List Nodes
class Node():

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    
    def string(self):
        out = ""
        while (self != None):
            out += str(self.value) + " "
            self = self.next
        return out
        

"""
Write code to remove duplicates from an unsorted linked list
Time Complexity: O(n)
"""
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

"""
Implement an algorithm to find the kth to last element of a singly linked list
Time Complexity: O(n)
"""
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

"""
Implement an algorithm to delete a node in the middle (i.e any node but
the first and last node, not necessarily the exact middle) of a singly linked list,
given only access to that node
Time Complexity: O(1)
"""
def delete_middle_node(middle):
    if (middle is None or middle.next is None):
        raise Exception("Not a middle node")
    middle.value = middle.next.value
    middle.next = middle.next.next

"""
Write code to partition a linked list around a value x, such that all nodes less than
x come before all nodes greater than or equal to x. If x is contained within the list,
the values of x only need to be after the elements less than x.
Time Complexity: O(n)
"""
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

"""
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
Time Complexity: O(m + n)
"""
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

"""
Implement a function to check if a linked list is a palindrome
Time Complexity: O(n)
"""
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

"""
Given two singly linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list list is the exact same node (by reference) as the jth node of the
second linked list, then they are intersecting.
Time Complexity: O(m + n)
"""
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

"""
Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop
Time Complexity: O(n) if no loop
"""
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