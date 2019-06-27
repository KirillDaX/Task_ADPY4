import unittest
import os
import json
import main_prog
# from unittest.mock import patch


class TestAppDocs(unittest.TestCase):

    def test_add_new_doc(self):
        """проверяет что кол-во элментов изменилось"""
        print('\n => now work: test_add_new_doc, Input: a')
        start_count = (len(main_prog.documents))
        main_prog.add_new_doc()
        self.assertNotEqual(start_count, len(main_prog.documents), f'до {start_count}, после {len(main_prog.documents)}')

    def test_delete_doc(self):
        """проверяет что стало меньше элементов"""
        print('\n => now work: test_delete_doc. Input: d,(numbers of documents: 2207 876234, 11-2, 10006)')
        base_count_of_docs = (len(main_prog.documents))
        main_prog.delete_doc()
        self.assertLess((len(main_prog.documents)), base_count_of_docs, 'документ не удалился')

    def test_add_new_shelf(self):
        """проверка созданнной полки"""
        print('\n => now work: test_add_new_shelf, Input: as')
        self.assertIn(main_prog.add_new_shelf('5')[0], list(main_prog.directories.keys()))
        print('end test_add_new_shelf')


if __name__ == '__main__':
    unittest.main()

