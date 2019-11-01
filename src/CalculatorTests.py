import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

        test_data_squareroot = CsvReader('/src/UnitTestAll.csv').data
        pprint(test_data_squareroot)

        for row in test_data_add:
            self.assertEqual(self.calculator.add(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

        for row in test_data_subtract:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result'])


    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

        for row in test_data_multiply:
            self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)

        for row in test_data_divide:
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), round(float(row['Result']),9))
            self.assertEqual(self.calculator.result, float(row['Result'])


    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)

        for row in test_data_square:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.squareroot(4), 2)
        self.assertEqual(self.calculator.result, 2)



        for row in test_data_squareroot:
            self.assertEqual(self.calculator.squareroot(row['Value 1']), round(float(row['Result']),8))
            self.assertEqual(self.calculator.result, round(float(row['Result']),8))

if __name__ == '__main__':
    unittest.main()
