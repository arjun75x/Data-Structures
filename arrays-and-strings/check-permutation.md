# Check Permutation

Given two strings, write a method to decide if one is a permutation of the other

Time complexity: O\(n\)

```python
def check_permutation(string_one, string_two):
    ascii = [False for i in range(128)]
    for char in string_one:
        ascii[ord(char)] = not ascii[ord(char)]
    for char in string_two:
        if not ascii[ord(char)]:
            return False
    return True
```

