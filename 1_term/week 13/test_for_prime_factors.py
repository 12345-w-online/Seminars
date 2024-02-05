import unittest

from mnk_for_test_from_graphics import mnk


class MyCustomTest(unittest.TestCase):
    def my_custom_test(self):
        self.assertEqual(mnk(0), 0, 'should be 0')


class PraimeFactorsCustomTest(unittest.TestCase):
    def negative_numbers(self):
        with self.assertRaisesRegex(Exception):
            print(mnk(-1))


class FloatNumbersTest(unittest.TestCase):
    def float_numbers_test(self):
        with self.assertRaises(ValueError):
            mnk(1.5)


if __name__ == '__main__':
    print("it's main file")
    unittest.main()
