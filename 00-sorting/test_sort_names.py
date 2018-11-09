#!/usr/bin/env python3

import unittest
import random
import sort_names


class TestSortNames(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_names.sort_by_last([]), [], "expected empty list to be unmodified")

    def test_single_elem_list(self):
        self.assertEqual(sort_names.sort_by_last(["Jane Doe"]), ["Jane Doe"], 
                         "expected single element list to be unmodified")

    def test_multi_list(self):
        unsorted = ["Anna Smith", "John Anderson", "Cliff Bates"]
        expected = ["John Anderson", "Cliff Bates", "Anna Smith"]

        self.assertEqual(sort_names.sort_by_last(unsorted), expected, 
                         "expected different sort order")

    def test_single_word_names(self):
        unsorted = ["Anna Smith", "John Anderson", "Cliff Bates", "Jeffrey Sinclair",
                   "Michael Garibaldi", "Susan Ivanova", "John Sheridan", "Delenn",
                   "Kosh", "G'Kar", "Valen", "Zathras" ]

        expected = ['John Anderson', 'Cliff Bates', 'Delenn', "G'Kar", 'Michael Garibaldi',
                    'Susan Ivanova', 'Kosh', 'John Sheridan', 'Jeffrey Sinclair',
                    'Anna Smith', 'Valen', 'Zathras']

        self.assertEqual(sort_names.sort_by_last(unsorted), expected, 
                         "expected different sort order")


if __name__ == '__main__':
    unittest.main()