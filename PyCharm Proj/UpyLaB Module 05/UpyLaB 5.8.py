def anagrammes(v, w):
    if len(v) != len(w):
        res = False
    else:
        x = []
        y = []
        for i in range(len(v)):
            x.append(v[i])
            x.sort()
            y.append(w[i])
            y.sort()
        if x == y:
            res = True
        else:
            res = False
    return res


# Code principal
print(anagrammes('marion', 'romina'))
print(anagrammes('bonjour', 'jour'))
print(anagrammes('pate', 'patte'))