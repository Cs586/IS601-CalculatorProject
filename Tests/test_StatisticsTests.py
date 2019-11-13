import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from pprint import pprint
# from Statistics.Answers import Answers


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/UnitTestStats.csv')

    # def setUp(self) -> None:
        # self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        for row in test_data:
            result = float(row['Mean'])
            self.assertEqual(self.statistics.mean(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'],
                                                  row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8'],
                                                  row['Value 9'], row['Value 10'], row['Value 11'], row['Value 12'],
                                                  row['Value 13'], row['Value 14'], row['Value 15'], row['Value 16'],
                                                  row['Value 17'], row['Value 18'], row['Value 19'], row['Value 20']),
                             result)
            self.assertEqual(self.statistics.result, result)
        pprint(test_data)

    def test_median_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        for row in test_data:
            result = float(row['Median'])
            self.assertEqual(self.statistics.median(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'],
                                                  row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8'],
                                                  row['Value 9'], row['Value 10'], row['Value 11'], row['Value 12'],
                                                  row['Value 13'], row['Value 14'], row['Value 15'], row['Value 16'],
                                                  row['Value 17'], row['Value 18'], row['Value 19'], row['Value 20']),
                             result)
            self.assertEqual(self.statistics.result, result)
        pprint(test_data)


if __name__ == '__main__':
    unittest.main()