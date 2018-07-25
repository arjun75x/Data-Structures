# Zero Matrix

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to zero

Time Complexity: O\(mn\)

```python
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
```



