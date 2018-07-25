---
description: >-
  Implement and algorithm to determine if a string has all unique characters.
  What if you cannot use additional data structures? Time complexity: O(n)
---

# Is Unique

{% code-tabs %}
{% code-tabs-item title="is\_unique.py" %}
```python
def is_unique(string):

    ascii = [0 for i in range(128)]
    for char in string:
        ascii[ord(char)] += 1
    for char_count in ascii:
        if (char_count > 1):
            return False
    return True
```
{% endcode-tabs-item %}
{% endcode-tabs %}



