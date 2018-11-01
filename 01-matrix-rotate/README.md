# Challenge: Matrix Rotation

Given an _N x N_ matrix represented as a list of lists, write a function that rotates the matrix by 90 degrees clockwise.

> examples:
```python
[[1, 2],           -- rotate -->  [[3, 1],
 [3, 4]]                           [4, 2]]


[['a', 'b', 'c'],                 [['x', 1, 'a'],
 [ 1,   2,   3 ],  -- rotate -->   ['y', 2, 'b'],
 ['x', 'y', 'z']]                  ['z', 3, 'c']]
```

Try writing two implementations: with and without using `zip()`.
