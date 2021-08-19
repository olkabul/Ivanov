import unittest
from  expected_results import *
from main import *

class FakeArgs():
    machine = False
    under = False

class MyTestCase(unittest.TestCase):

    def test_machine_format(self):
        fake_args = FakeArgs()
        fake_args.machine = True
        real_result = get_result_by_argument(fake_args)
        assert machine_formatting_expected == real_result, \
            f"Expected result: {machine_formatting_expected}, actual: {real_result}"

    def test_circumflex_format(self):
        fake_args = FakeArgs()
        fake_args.under = True
        real_result = get_result_by_argument(fake_args)
        assert under_formatting_expected == real_result, \
            f"Expected result: {under_formatting_expected}, actual: {real_result}"

    def test_basic_format(self):
        fake_args = FakeArgs()
        real_result = get_result_by_argument(fake_args)
        assert basic_formatting_expected == real_result, \
            f"Expected result: {basic_formatting_expected}, actual: {real_result}"


if __name__ == '__main__':
    unittest.main()