#!/usr/bin/env python3

def sort_by_last(name_list):
    # define a local 'key' function that extracts the lastname based on white space, 
    # combining the last_name and full_name in a tuple for comparison
    def by_last(full_name):
        # split on whitespace and use final element as lastname
        last_name = full_name.split()[-1]
        return (last_name, full_name) # note return of tuple

    # note: the 'key' function could also be handled by a 'lambda'
    return sorted(name_list, key=by_last)
