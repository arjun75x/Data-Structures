# String Rotation

Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only onecall to isSubstring

Time Complexity: O\(N\), based on time complexity of isSubstring function

```python
def string_rotation(s1, s2):
    if (len(s1) != len(s2)):
        return False
    return s1 in (s2 + s2) # same as isSubstring function
```

