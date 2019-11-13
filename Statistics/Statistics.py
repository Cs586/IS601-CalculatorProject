from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from CsvReader.CsvReader import CsvReader
from pprint import pprint

class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader('Tests/Data/UnitTestStats.csv').data
        super().__init__()

    def mean(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
        self.result = mean(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t)
        return self.result

    def median(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
        self.result = median(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t)
        return self.result

    pass
