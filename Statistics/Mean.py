from Calculator.Addition import addition
from Calculator.Division import division


def mean(data):
    map(float, data)
    total = 0
    num_values = len(data)
    for num in data:
        total = addition(total, num.values)
    return division(total, num_values)