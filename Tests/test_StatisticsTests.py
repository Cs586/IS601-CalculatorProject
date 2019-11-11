import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from pprint import pprint
# from Statistics.Answers import Answers


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/UnitTestStats.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        for row in test_data:
            test_mean = float(9.45)
            mean = self.statistics.mean(test_data.values)
            self.assertEqual(mean, test_mean)
            pass
        pprint(test_data)


if __name__ == '__main__':
    unittest.main()