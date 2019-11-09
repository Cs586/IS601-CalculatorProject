import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
# from Statistics.Answers import Answers


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/UnitTestStats.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        test_mean = float(100.474)
        # answers = CsvReader('Tests/Data/UnitTestStatsAnswers.csv').data
        for row in test_data:
            mean = self.statistics.mean()
            self.assertEqual(mean, test_mean)


if __name__ == '__main__':
    unittest.main()