from Statistics.ZScore import zscore


def correlation(data, data1):
    try:
        z1 = zscore(data)
        z2 = zscore(data1)
        z1_z2 = list(map(lambda x, y: x * y, z1, z2))
        corr = sum(z1_z2) / len(z1_z2)
        return round(corr, 7)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")

        # r = Σ(xy) / sqrt[(Σ x2) * (Σ y2)]
        # where Σ is the summation symbol, x = xi - x, xi is the x value
        # for observation i, x is the mean x value, y = yi - y, yi is the y value for observation i, and y is the mean y value.
