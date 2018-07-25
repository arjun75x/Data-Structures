# Palindrome Permutation

Given a string, write a function to check if it is a permutation of a palindrome

Time complexity: O\(n\)

```python
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
```

