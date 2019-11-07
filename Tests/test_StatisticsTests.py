import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        for row in test_data:
            result = 'mean'
            self.assertEqual(self.statistics.mean(self.data, result))


if __name__ == '__main__':
    unittest.main()