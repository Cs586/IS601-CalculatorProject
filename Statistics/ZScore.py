from Calculator.Square import squaring
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Statistics.PopulationMean import populationmean
from Statistics.StandardDeviation import stddev


def zscore(num):
    zmean = populationmean(num)
    zstandard_deviation = stddev(num)
    z_list = []
    for i in num:
        z = division((i - zmean), zstandard_deviation)
        z_list.append(z)
    return z_list

