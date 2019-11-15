from Calculator.SquareRoot import squarerooting
from Statistics.Variance import variance


def stddev(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
    try:
        stddev_list = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]
        stddev_float = [float(i) for i in stddev_list]
        variance_float = variance(*stddev_float)
        return round(squarerooting(variance_float), 5)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")