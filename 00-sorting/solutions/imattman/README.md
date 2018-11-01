# SOLUTION - Warmup Challenge: Sorting

The purpose of this challenge is to explore additional ways data can be analyzed for sorting.  By default Python sorts lists using natural element ordering, such as lexicographic order for text.  This sorting behavior can be overriden by specifying an optional `key` parameter that takes a function reference that converts each element into an alternate value used in comparisons.  

A common way to leverage this is to have the `key` function return a tuple of values.  Tuples are compared position by position, starting with the first index.  If the first positions in the compared tuples are the same, then the second positions in the tuples are compared, and then the third, and so on.

This mechanism of comparison using tuples is the same one used in this exercise sorting names, last name first.   The sorting function is supplied a `key` function of `by_last` that splits the string on whitespace, then returns a 2-element tuple comprised of `(last_name, full_name)` so that the last names are compared first in the sort.  If two people happen to share the same last name, the comparison falls back to checking the second element in each tuple: the *full_name*.
