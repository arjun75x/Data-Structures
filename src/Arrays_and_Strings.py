"""
Implement and algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
Time complexity: O(n)
"""
def is_unique(string):
    ascii = [0 for i in range(128)]
    for char in string:
        ascii[ord(char)] += 1
    for char_count in ascii:
        if (char_count > 1):
            return False
    return True

"""
Given two strings, write a method to decide if one is a permutation of the other
Time complexity: O(n)
"""
def check_permutation(string_one, string_two):
    ascii = [False for i in range(128)]
    for char in string_one:
        ascii[ord(char)] = not ascii[ord(char)]
    for char in string_two:
        if not ascii[ord(char)]:
            return False
    return True

"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string 
has sufficient space at the end to hold additional characters, and that you are given the "true" 
length of the string. The string should be inputted as a list.
Time complexity: O(n)
"""
def url_ify(string, length):
    last_letter = length - 1
    index = len(string) - 1
    while (index > 0):
        if (string[last_letter] == " "):
            string[index - 2 : index + 1] = "%20"
            index -= 2
        else:
            string[index] = string[last_letter]
        last_letter -= 1
        index -= 1
    return string

"""
Given a string, write a function to check if it is a permutation of a palindrome
Time complexity: O(n)
"""
def palindrome_permutation(string):
    ascii = [0 for i in range(128)]
    for char in string:
        ascii[ord(char)] += 1
    if (len(string) % 2 == 0):
        for char_count in ascii:
            if (char_count % 2 != 0):
                return False
    else:
        odd = True
        for char_count in ascii:
            if (char_count % 2 != 0):
                if odd:
                    odd = not odd
                else:
                    return False
    return True

"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to
check if they are one or zero edits away
Time complexity: O(n)
"""
def one_away(string_one, string_two):
    ascii_one = [0 for i in range(128)]
    ascii_two = [0 for i in range(128)]
    for char in string_one:
        ascii_one[ord(char)] += 1
    for char in string_two:
        ascii_two[ord(char)] += 1
    only_one = True
    for i in range(0, 128):
        if (ascii_one[i] != ascii_two[i]):
            if only_one:
                only_one = not only_one
            else:
                return False
    return True

"""
Implement a method to perform basic string compression using the counts of repeated
characters. For example, the string aabcccccaaa would becom a2b1c5a3. If the
compressed  string would not be smaller than the original string, return the original.
Time Complexity: O(n)
"""
def string_compression(string):
    count = 0
    temp = string[0]
    out = ""
    for char in string:
        if (char == temp):
            count += 1
        else:
            out += temp + str(count)
            temp = char
            count = 1
    out += temp + str(count)
    return out if (len(out) < len(string)) else string

"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
Time Complexity: O(n^2)
"""
def rotate_matrix(matrix):
    n = len(matrix) - 1
    for i in range (0, int(len(matrix)/2)):
        for j in range (i, n - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j][i]
            matrix[n - j][i] = matrix[n - i][n - j]
            matrix[n - i][n - j] = matrix[j][n - i]
            matrix[j][n - i] = temp
    return matrix

"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to zero
Time Complexity: O(mn)
"""
def zero_matrix(matrix):
    zero_x = []
    zero_y = []
    for i in range (0, len(matrix)):
        for j in range (0, len(matrix[0])):
            if (matrix[i][j] == 0):
                zero_x.append(i)
                zero_y.append(j)
    zero_x = set(zero_x)
    zero_y = set(zero_y)
    for x in zero_x:
        for i in range (0, len(matrix[0])):
            matrix[x][i] = 0
    for y in zero_y:
        for j in range (0, len(matrix)):
            matrix[j][y] = 0
    return matrix

"""
Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring
Time Complexity: O(N), based on time complexity of isSubstring function
"""
def string_rotation(s1, s2):
    if (len(s1) != len(s2)):
        return False
    return s1 in (s2 + s2) # same as isSubstring function