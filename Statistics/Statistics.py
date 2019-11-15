from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import stddev
from Statistics.Variance import variance
from CsvReader.CsvReader import CsvReader


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

    def mode(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
        self.result = mode(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t)
        return self.result

    def stddev(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
        self.result = stddev(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t)
        return self.result

    def variance(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
        self.result = variance(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t)
        return self.result

    pass
