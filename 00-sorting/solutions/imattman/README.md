# SOLUTION: Warmup Challenge: Sorting

The purpose of this challenge is to explore additional controls the programmer has at their disposal when sorting lists of data.

I take advantage of two such controls in my solution:
- a `key` function is used for converting elements to an alternate value for comparison
- the use of tuple sorting behavior to offer primary and secondary comparisons

## Key Functions
By default Python sorts lists according to the natural ordering of the data types.  An example is lexicographic order for strings.  This behavior of how list elements are compared can be overridden. The various sort functions support an optional `key` parameter that takes a function reference (or lambda) as an argument.  This function is then applied to each element, returning an alternate value for comparison.

My solution uses `by_last` as a key function that returns a tuple comprised of 2 parts: `(last_name, full_name)`.   

As a side note on safety, the last name is indexed using `[-1]` to access the final element after the `split()`.  This avoids a possible index-out-of-bounds error using an index of `[1]` in cases where the split returns only a single element list.

## Tuple Sorting

In Python tuples are compared lexicographically, position by position. The first items are compared; if they are the same, then the second items, and so on.

My solution leverages this behavior by building a tuple of `(last_name, full_name)` so that the last names are the first items compared. In cases where two people share the same last name, the sort falls back to compare the second tuple element containing the full name.

## Additional Reading

- [More on key functions](https://docs.python.org/3.3/howto/sorting.html#key-functions)
- [More on tuple lexicographic comparison](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

