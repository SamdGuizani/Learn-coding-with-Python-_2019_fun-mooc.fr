def my_filter(liste, f):
    res = []
    for i in range(len(liste)):
        if f(liste[i]) == True:
           res += [liste[i]]
    return res


# Code principal
print(my_filter(['hello', 666, 42, 'Thierry', 1.5], lambda x : isinstance(x, int)))
print(my_filter([-2, 0, 4, -5, -6], lambda x : x < 0))
