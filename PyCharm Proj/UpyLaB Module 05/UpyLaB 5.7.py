def my_pow(m, b):
    if type(m) != int or type(b) != float:
        res = None
    else:
        res = [0] * m
        for i in range(m):
            res[i] = b**i
    return res


# Code principal
print(my_pow(3, 5.0))
print(my_pow(3.0, 5.0))
print(my_pow('a', 'b'))
