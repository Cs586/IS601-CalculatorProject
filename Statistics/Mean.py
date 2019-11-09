from Calculator.Addition import addition
from Calculator.Division import division


def mean(data):
    num_values = len(data)
    total = 0
    for x in data:
        total = total + x
    return division(total, num_values)