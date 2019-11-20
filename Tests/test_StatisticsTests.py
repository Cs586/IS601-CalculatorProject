import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from pprint import pprint


class MyTestCase(unittest.TestCase):
    test_data = CsvReader('Tests/Data/Test_Data.csv').data
    column1 = [int(row['value1']) for row in test_data]
    column2 = [int(row['value2']) for row in test_data]
    p_answers = CsvReader('Tests/Data/Test_Proportion.csv').data
    column_proportion = [float(row['Proportion']) for row in p_answers]
    z_answers = CsvReader('Tests/Data/Test_ZScores.csv').data
    column_zscore = [float(row['Z-Score']) for row in z_answers]
    test_answer = CsvReader('Tests/Data/UnitTestStatsAnswers.csv').data

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_population_mean_statistics(self):
        for row in self.test_answer:
            pprint(row["mean"])
        self.assertEqual(self.statistics.population_mean(self.column1), float(row['mean']))
        self.assertEqual(self.statistics.result, float(row['mean']))

    def test_median_statistics(self):
        for row in self.test_answer:
            pprint(row["median"])
        self.assertEqual(self.statistics.median(self.column1), float(row['median']))
        self.assertEqual(self.statistics.result, float(row['median']))

    def test_mode_statistics(self):
        for row in self.test_answer:
            pprint(row["mode"])
        self.assertEqual(self.statistics.mode(self.column1), float(row['mode']))
        self.assertEqual(self.statistics.result, float(row['mode']))

    def test_standard_deviation_statistics(self):
        for row in self.test_answer:
            pprint(row["stddev"])
        self.assertEqual(self.statistics.stddev(self.column1), float(row['stddev']))
        self.assertEqual(self.statistics.result, float(row['stddev']))

    def test_variance_statistics(self):
        for row in self.test_answer:
            pprint(row['variance'])
        self.assertEqual(self.statistics.variance(self.column1), float(row['variance']))
        self.assertEqual(self.statistics.result, float(row['variance']))

    def test_proportion_statistics(self):
        self.assertEqual(self.statistics.proportion(self.column1), self.column_proportion)
        self.assertEqual(self.statistics.result, self.column_proportion)


if __name__ == '__main__':
    unittest.main()