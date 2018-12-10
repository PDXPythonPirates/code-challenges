# Challenge: Build a Grep Clone

## Pygrep

Write a simplified version of [grep][grep] named `pygrep` that is executable from the command line and supports basic text searching capabilities.

Your version of `pygrep` should behave similarly to the standard utility and search all candidate files supplied as arguments.  

If no files are specified as arguments to search then `pygrep` should read and process `STDIN`.

Upon conclusion of execution if at least one match is made `pygrep` should exit with a `0` value indicating success; otherwise it should exit with a non-zero value.

Examples of execution from command line:

    # searching in specified files
    pygrep SEARCH_PATTERN file1.txt file2.txt file3.txt

    # searching data streamed in via STDIN
    tail -f /path/to/growing/log | pygrep SEARCH_PATTERN

## Supported Flags

Your version of `pygrep` is to support the following command line flags:

- `-n` prepends the file `<line number>:` to search matches
- `-H` prepends the `<filename>:` to search matches
- `-l` prints only the filename of files with matches
- `-c` prints only the count of matching lines
- `-v` inverts the search to select lines that do *not* match
- `-q` quiet operation with zero output so that only the exit code is returned

Some of the flags conflict with each other in their behavior (e.g. `-n` and `-l` are mutually exclusive).

It is at your discretion to determine if such conflicts trigger an error and help message or one option simply supersedes another.

[grep]: https://en.wikipedia.org/wiki/Grep
