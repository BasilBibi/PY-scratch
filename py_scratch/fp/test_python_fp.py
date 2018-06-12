import unittest


class FunctionalProgrammingTests(unittest.TestCase):

    def test_curry(self):
        def g(*args):
            myArgs = []

            def f(*args):
                nonlocal myArgs  # now it's non-local: it isn't global
                if len(args):  # some more args!
                    myArgs += args
                    return f
                else:  # time to evaluate...
                    print(*myArgs)

            return f(*args)

        g1 = g(1, 2)
        g1(3, 4)()

        g2 = g(10, 20)
        g2(30, 40)()

    def test_lambda(self):
        # Using `def` (old way).
        def old_add(a, b):
            return a + b

        # Using `lambda` (new way).
        new_add = lambda a, b: a + b

        old_add(10, 5) == new_add(10, 5)

        print(new_add(10,5))

    def test_map(self):
        values = [1, 2, 3, 4, 5]

        # Note: We convert the returned map object to
        # a list data structure.
        add_10 = list(map(lambda x: x + 10, values))

        print(add_10)

    def testFilter(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Note: We convert the returned filter object to
        # a list data structure.
        even = list(filter(lambda x: x % 2 == 0, values))

        print(even)

    def test_reduce(self):
        from functools import reduce

        values = [1, 2, 3, 4]

        summed = reduce(lambda a, b: a + b, values)
        print(summed)

    def test_list_comprehensions(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Map.
        add_10 = [x + 10 for x in values]
        print(add_10)

        # Filter.
        even = [x for x in values if x % 2 == 0]
        print(even)

        nested = [x for x in add_10 if x % 2 == 0]
        print(nested)

        def square(x): return x*x
        print( [square(x) for x in values] )


if __name__ == '__main__':
    unittest.main()
