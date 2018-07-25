# One Away

There are three types of edits that can be performed on strings: insert a character,remove a character, or replace a character. Given two strings, write a function to check if they are one or zero edits away.

Time complexity: O\(n\)

```python
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
```

