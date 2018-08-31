import unittest
import tempfile
import os
from py_scratch.udemy_oo.section4.Assignment2Composition import *


def get_file_contents(fn):
    with open(fn, 'r') as fh:
        return '\n'.join([word for word in fh.readlines()])


class Assignment2Tests(unittest.TestCase):

    def test_can_write_to_LogFile(self):

        new_file, file_path = tempfile.mkstemp()
        os.close(new_file)

        lw = WriteFile(LogFile, file_path)
        msg = 'This is a test'
        lw.write(msg)
        lw.close()

        log_file_contents = get_file_contents(file_path)
        self.assertTrue(msg in log_file_contents )

    def test_can_write_to_DelimFile(self):

        new_file, file_path = tempfile.mkstemp()
        os.close(new_file)

        df = WriteFile(DelimFile, file_path)
        l = ['a', 'b', 'c', 'd']
        df.write(l)
        df.close()

        log_file_contents = get_file_contents(file_path)
        self.assertTrue('a,b,c,d' in log_file_contents )

    def test_can_write_to_delimited_fields_DelimFile(self):

        new_file, file_path = tempfile.mkstemp()
        os.close(new_file)

        df = WriteFile(DelimFile, file_path)
        l = ['a', 'b,x', 'c', 'd']
        df.write(l)
        df.close()

        log_file_contents = get_file_contents(file_path)
        self.assertTrue('a,"b,x",c,d' in log_file_contents )


if __name__ == 'main':
    unittest.main()
