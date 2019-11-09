from CsvReader.CsvReader import CsvReader

test_answers = CsvReader('Tests/Data/UnitTestStatsAnswers.csv').data
for row in test_answers:
    test_mean = float(row['mean'])
    test_stdev = float(row['stdev'])
    test_median = int(row['median'])
pass