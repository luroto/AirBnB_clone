#!/usr/bin/python3
""" This module tests all about Storage """
from models.engine.file_storage import FileStorage
import os
import unittest
import pep8


class testUser(unittest.TestCase):
    ''' Test of the model BaseModel '''

    @classmethod
    def setUpClass(cls):
        ''' Set FileStorage Class '''
        cls.test_inst = FileStorage()

    def test_isInstance(self):
        ''' test if is a instance of BaseModel '''
        self.assertTrue(isinstance(self.test_inst, FileStorage))

    def test_hasDocumentation(self):
        ''' test the methods have documentation '''
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)

    def test_methods(self):
        ''' test the instance have the methods '''
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(hasattr(FileStorage, 'reload'))

    def test_pep8_conformance(self):
        ''' Test that we conform to PEP8 '''
        style = pep8.StyleGuide(quiet=True)
        path1 = "models/engine/file_storage.py"
        path2 = "tests/test_models/test_engine/test_file_storage.py"
        check = style.check_files([path1, path2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

    @classmethod
    def tearDownClass(cls):
        ''' test_inst Down '''
        del cls.test_inst
        try:
            os.remove("file.json")
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
