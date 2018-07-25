# Rotate Matrix

Given an image represented by an NxN matrix, where each pixel in the image is 4bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

Time Complexity: O\(n^2\)

```python
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
```

