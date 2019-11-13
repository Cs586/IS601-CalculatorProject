# from Calculator.Addition import addition
from Calculator.Division import division


def mean(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        num_values = 3
        total = a + b + c
        # for num in data:
            # total = addition(total, float(num))
        return division(total, num_values)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")