from Calculator.Square import squaring
from Calculator.Division import division
from Statistics.Mean import mean


def variance(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
    try:
        variance_list = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]
        variance_float = [float(i) for i in variance_list]
        pop_mean = mean(*variance_float)
        num_values = len(variance_float)
        x = 0
        for i in variance_float:
            x = x + squaring(i-pop_mean)
        return round(division(x, num_values), 5)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")