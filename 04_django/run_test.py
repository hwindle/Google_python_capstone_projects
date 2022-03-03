#!/usr/bin/env python3

import run
import unittest

class TestScript(unittest.TestCase):

    def test_dir_list(self):
        test_list = run.get_descriptions('supplier-data/descriptions')
        self.assertEqual(
            ['supplier-data/descriptions/001.txt', 'supplier-data/descriptions/002.txt'],
            test_list, 'Should be equal')


    def test_json_output(self):
        correct_output = [
            {
                'name': 'Mango',
                'weight': 300,
                'description': 'Mango contains higher levels of vitamin C than other fruits.',
                'image_name': 'supplier-data/images/001.jpg'
            },
            {
                'name': 'Apple',
                'weight': 450,
                'description': 'Sweet, crunchy and tasty.',
                'image_name': 'supplier-data/images/002.jpg'
            }
        ]
        test_dicts = run.text_processing(['supplier-data/descriptions/001.txt', 'supplier-data/descriptions/002.txt'])
        self.assertEqual(correct_output, test_dicts, 'dicts should be equal')

#self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
