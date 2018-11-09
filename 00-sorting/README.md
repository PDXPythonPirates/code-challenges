# Warmup Challenge: Sorting

Given a list of strings where each string is 2 words, a _first name_ and _last name_ separated by a space, write a function `sort_by_last` that sorts the list by last name, *then* first name.

```python
# Example:
names = ["Anna Smith", "John Anderson", "Cliff Bates"]
names_sorted = sort_by_last(names)

print(names_sorted)
# prints:
# ["John Anderson", "Cliff Bates", "Anna Smith"]
```

An incomplete version of `sort_by_last()` is available in `sort_names.py` along with unit tests in `test_sort_names.py` to check your implementation.

You can run the unit tests within PyCharm by executing `test_sort_names.py`.

Alternatively, you can run the tests from the command line.  Change directories to where you have this challenge on your local disk and execute the following:

    # change directories where you have the challenges on your local drive
    # replace `/path/to/challenges` with your local path
    cd /path/to/challenges/00-sorting

    python3 -m unittest -v

_TODO: Instructions for Windows command line_
