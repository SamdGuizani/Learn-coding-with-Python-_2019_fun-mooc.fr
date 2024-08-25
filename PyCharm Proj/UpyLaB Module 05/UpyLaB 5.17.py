def decompresse(list):
    result = []
    for i in range(len(list)):
        result += [list[i][1] for x in range(list[i][0])]
    return result


# Code principal
print(decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]))