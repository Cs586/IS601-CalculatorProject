from Calculator.Calculator import Calculator


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

#class CSVStats(Calculator):
#    data = []
#
#    def __init__(self, data_file):
#        self.data = CsvReader(data_file)
#        pass

#    def mean(self, ):

#    def mean(data):
#        mean = data
#        return mean