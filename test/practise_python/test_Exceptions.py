import unittest


def guess(participants):

    try:
        if 'Larry' in participants:
            return participants['Larry']
    except KeyError:
        print('Impossible to get here')
        return None

    try:
        return participants['Larry']
    except KeyError:
        print(''''Larry' not in participants''')
        return None


class ExceptionsTests(unittest.TestCase):

    def test_should_find_larry(self):
        participants = {'Larry': 1}
        actual = guess(participants)
        self.assertEqual(1, actual)

    def test_should_get_exception_then_None(self):
        participants = {'Cathy': 1, 'Fred': 2, 'Jack': 3, 'Tom': 4}
        actual = guess(participants)
        self.assertEqual(None, actual)


if __name__ == '__main__':
    unittest.main()
