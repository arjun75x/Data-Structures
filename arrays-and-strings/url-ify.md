# URL-ify

Write a method to replace all spaces in a string with '%20'. You may assume that the stringhas sufficient space at the end to hold additional characters, and that you are given the "true"length of the string. The string should be inputted as a list.

Time complexity: O\(n\)

```python
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
```

