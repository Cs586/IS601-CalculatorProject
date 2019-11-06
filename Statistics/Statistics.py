from Calculator.Calculator import Calculator


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self):
        a = len(self)
        b = float(sum(self))
        return b / a


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