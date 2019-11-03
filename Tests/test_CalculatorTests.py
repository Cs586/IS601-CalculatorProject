import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from pprint import pprint

test_data = CsvReader('Tests/Data/UnitTestAll.csv').data
pprint(test_data)


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()


    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = CsvReader('Tests/Data/UnitTestAll.csv').data
        pprint(test_data)
        for row in test_data:
            result = float(row['addresult'])
            self.assertEqual(self.calculator.add(row['addvalue2'], row['addvalue1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

        for row in test_data:
            result = float(row['subresult'])
            self.assertEqual(self.calculator.subtract(row['subvalue2'], row['subvalue1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

        for row in test_data:
            result = float(row['multiplyresult'])
            self.assertEqual(self.calculator.multiply(row['multiplyvalue2'], row['multiplyvalue1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)

        for row in test_data:
            result = float(row['divideresult'])
            self.assertEqual(self.calculator.divide(row['dividevalue2'], row['dividevalue1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)

        for row in test_data:
            result = float(row['sqresult'])
            self.assertEqual(self.calculator.square(row['sqvalue1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.squareroot(4), 2)
        self.assertEqual(self.calculator.result, 2)

        for row in test_data:
            result = float(row['sqrootresult'])
            self.assertEqual(self.calculator.squareroot(row['sqrootvalue1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)


if __name__ == '__main__':
    unittest.main()
