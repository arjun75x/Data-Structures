# String Compression

Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the compressed string would not be smaller than the original string, return the original.

Time Complexity: O\(n\)

```python
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
```

