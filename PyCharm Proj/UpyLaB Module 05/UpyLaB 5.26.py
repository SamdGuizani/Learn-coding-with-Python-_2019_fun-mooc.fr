def antisymetrique(M):
    res = True
    if M == []:
        res = res
    else:
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j] != - M[j][i]:
                    res = False
    return res


# Code principal
print(antisymetrique([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]))
print(antisymetrique([[0, 1], [1, 0]]))
print(antisymetrique([[1, -2], [2, 1]]))