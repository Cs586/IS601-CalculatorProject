import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/UnitTestStats.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        answers = CsvReader('Tests/Data/UnitTestStatsAnswers.csv').data
        for column in test_data:
            result = self.answers(float(column['mean']))
            self.assertEqual(self.statistics.mean['Value 1'], result)


if __name__ == '__main__':
    unittest.main()