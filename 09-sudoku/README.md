# Challenge: Sudoku Solver

Write a program that reads in an unsolved [sudoku puzzle][sudoku] and prints the solved puzzle.  

Unsolved locations in the puzzle are represented by `_`.
The input may be read in from a file or STDIN (your choice).

Your program should print the solved puzzle in the same format but with the `_` empty slots filled in.

Example input:

    1 _ 3 _ _ 6 _ 8 _
    _ 5 _ _ 8 _ 1 2 _
    7 _ 9 1 _ 3 _ 5 6
    _ 3 _ _ 6 7 _ 9 _
    5 _ 7 8 _ _ _ 3 _
    8 _ 1 _ 3 _ 5 _ 7
    _ 4 _ _ 7 8 _ 1 _
    6 _ 8 _ _ 2 _ 4 _
    _ 1 2 _ 4 5 _ 7 8

Example solution:

    1 2 3 4 5 6 7 8 9
    4 5 6 7 8 9 1 2 3
    7 8 9 1 2 3 4 5 6
    2 3 4 5 6 7 8 9 1
    5 6 7 8 9 1 2 3 4
    8 9 1 2 3 4 5 6 7
    3 4 5 6 7 8 9 1 2
    6 7 8 9 1 2 3 4 5
    9 1 2 3 4 5 6 7 8

This is a problem that can be solved using exhaustive brute force or more sophisticated rules and data handling.   How you go about it is up to you!  :-)

*This challenge is shamelessly stolen from a [similar challenge][golang_challenge] in the Go community.*

[sudoku]: https://en.wikipedia.org/wiki/Sudoku
[golang_challenge]: http://golang-challenge.org/go-challenge8/
