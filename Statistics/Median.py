from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition


def median(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
    try:
        median_list = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]
        float_list = [float(i) for i in median_list]
        num_values = len(median_list)
        float_list.sort()
        if num_values % 2 == 0:
            median1 = float_list[int(num_values // 2)]
            median2 = float_list[int(subtraction((num_values // 2), 1))]
            median_result = division(addition(median1, median2), 2)
        else:
            median_result = float_list[int(division(num_values, 2))]
        return median_result
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")