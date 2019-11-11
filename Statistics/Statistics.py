from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from CsvReader.CsvReader import CsvReader
from pprint import pprint

class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader('Tests/Data/UnitTestStats.csv').data
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    pass
