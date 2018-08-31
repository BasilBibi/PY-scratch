import unittest
import tempfile
import os
from py_scratch.udemy_oo.section4.Assignment2 import *


def read_and_clean_tempfile(file_path):
    contents = get_file_contents(file_path)
    clean_up_temp_file(file_path)
    return contents


def get_file_contents(fn):
    with open(fn, 'r') as fh:
        return '\n'.join([line for line in fh.readlines()])


def get_temp_file_path():
    os_file_handle, file_path = tempfile.mkstemp()
    os.close(os_file_handle)
    return file_path


def clean_up_temp_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)


class Assignment2Tests(unittest.TestCase):

    def test_can_write_to_LogFile(self):

        file_path = get_temp_file_path()

        lw = LogFile(file_path)
        msg = 'This is a test'
        lw.write(msg)
        lw.close()

        self.assertTrue(msg in read_and_clean_tempfile(file_path) )

    def test_can_write_to_DelimFile(self):

        file_path = get_temp_file_path()

        df = DelimFile(file_path)
        l = ['a', 'b', 'c', 'd']
        df.write(l)
        df.close()

        self.assertEqual('a,b,c,d', read_and_clean_tempfile(file_path))

    def test_can_write_fields_containing_delimiter_to_DelimFile(self):

        file_path = get_temp_file_path()

        df = DelimFile(file_path)
        l = ['a', 'b,x', 'c', 'd']
        df.write(l)
        df.close()

        self.assertEqual('a,"b,x",c,d', read_and_clean_tempfile(file_path))


if __name__ == 'main':
    unittest.main()
