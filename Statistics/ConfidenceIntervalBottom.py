from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.SquareRoot import squarerooting
from Statistics.PopulationMean import populationmean
from Statistics.StandardDeviation import stddev


def confidence_interval_bottom(num):
    try:
        num_values = len(num)
        z = 1.96
        sd = stddev(num)
        avg = populationmean(num)
        return round(avg - (z * sd / squarerooting(num_values)), 5)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")