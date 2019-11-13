import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from pprint import pprint
# from Statistics.Answers import Answers


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/UnitTestStatsBaby.csv')

    # def setUp(self) -> None:
        # self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        # self.assertEqual(self.statistics.mean(2, 2), 4)
        # self.assertEqual(self.statistics.result, 4)
        test_data = CsvReader('Tests/Data/UnitTestStatsBaby.csv').data
        # test_mean = float(2)
        # for row in test_data:
            # result = float(row['Mean'])
            # self.assertEqual(self.calculator.divide(self.calculator.add(self.calculator.add(
                # row['Value 1'], row['Value 2']), row['Value 3']), 3), result)
            # self.assertEqual(result, test_mean)
        for row in test_data:
            result = float(row['Mean'])
            self.assertEqual(self.statistics.mean(test_data), result)
            self.assertEqual(self.statistics.result, result)
        pprint(test_data)


if __name__ == '__main__':
    unittest.main()