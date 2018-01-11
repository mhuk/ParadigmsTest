# -*- coding: utf-8 -*-

from unittest import main as ut_main
from unittest import TestCase
from unittest.mock import patch
from main import FileManager
import shutil, tempfile


class TestFileManager(TestCase):

    def setUp(self):
        """Create a temporary directory"""
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Remove the directory after the test"""
        shutil.rmtree(self.test_dir)

    @patch('builtins.open')
    @patch('os.path.isfile', return_value=True)
    @patch('builtins.input', return_value='2017')
    def test_if_no_file_returned(self, input_mock, is_file_mock, open_mock):
        file_manager = FileManager()
        res = file_manager.open_file()
        input_mock.assert_called_once()
        is_file_mock.assert_called_once_with('2017.txt')
        open_mock.assert_called_once_with('2017.txt', 'r+')
        self.assertNotEqual(None, res)

if __name__ == "__main__":
    ut_main()

