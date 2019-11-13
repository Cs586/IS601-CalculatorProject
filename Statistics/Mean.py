# from Calculator.Addition import addition
from Calculator.Division import division


def mean(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
    try:
        mean_list = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]
        mean_float = [float(i) for i in mean_list]
        num_values = len(mean_float)
        total = sum(mean_float)
        # for num in data:
            # total = addition(total, float(num))
        return division(total, num_values)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")