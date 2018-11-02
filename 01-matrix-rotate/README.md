# Challenge: Matrix Rotation

Given an _N x N_ matrix represented as a list of lists, write a function that rotates the matrix by 90 degrees clockwise.

> examples:

    [[1, 2],            rotated ->    [[3, 1],
     [3, 4]]                           [4, 2]]


    [['a', 'b', 'c'],                 [['x', 1, 'a'],
     [ 1,   2,   3 ],   rotated ->     ['y', 2, 'b'],
     ['x', 'y', 'z']]                  ['z', 3, 'c']]

Try writing two implementations: with and without using `zip()`.
