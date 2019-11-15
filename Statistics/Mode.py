from collections import Counter


def mode(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
    try:
        mode_list = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]
        float_list = [float(i) for i in mode_list]
        num_values = len(float_list)
        count = Counter(float_list)
        get_mode = dict(count)
        mode = [k for k, v in get_mode.items() if v == max(list(count.values()))]
        if len(mode) == num_values:
            get_mode = "No mode found"
        else:
            get_mode = mode[0]
        return get_mode
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")