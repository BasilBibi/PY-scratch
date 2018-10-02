import unittest
import tempfile
import pickle
import os


def get_temp_file_path():
    os_file_handle, file_path = tempfile.mkstemp()
    os.close(os_file_handle)
    return file_path


def pickle_dump(obj, temp_file_name):
    with open(temp_file_name, 'wb') as fh:
        pickle.dump(obj, fh, protocol=pickle.HIGHEST_PROTOCOL)


def pickle_load(temp_file_name):
    with open(temp_file_name, 'rb') as fh:
        return pickle.load(fh)


class PicklingTests(unittest.TestCase):

    def test_can_dump_and_load_pickle(self):

        temp_file_name = get_temp_file_path()

        cid = {'a': 1, 'b': 2}

        pickle_dump(cid, temp_file_name)

        cid_from_load = pickle_load(temp_file_name)

        self.assertEqual(cid, cid_from_load)

        os.remove(temp_file_name)


if __name__ == '__main__':
    unittest.main()