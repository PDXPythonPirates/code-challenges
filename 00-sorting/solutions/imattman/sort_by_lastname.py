#!/usr/bin/env python3

names = [ "Anna Smith", 
          "John Anderson", 
          "Cliff Bates",
          "Jeffrey Sinclair",
          "Michael Garibaldi",
          "Susan Ivanova",
          "John Sheridan",
          "Delenn",
          "Kosh",
          "G'Kar",
          "Valen",
          "Zathras"
        ]

def by_last(full_name):
    # split on whitespace and use final element as lastname
    last_name = full_name.split()[-1]
    return (last_name, full_name) # note return of tuple

# sort using helper function to extract sorting key
# note: this could also be a 'lambda'
names.sort(key=by_last)
print("\n".join(names))
