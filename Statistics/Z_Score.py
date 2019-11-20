from Calculator.Square import squaring
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Statistics.PopulationMean import populationmean
from Statistics.StandardDeviation import stddev


def zscore(num):
    try:
        z_list = list()
        mean = populationmean(num)
        standard_deviation = stddev(num)
        for i in num:
            z = (i - mean) / standard_deviation
            z_list.append(z)
        return z_list
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")
