def init_mat(m, n):
    res = [[0 for i in range(n)] for k in range(m)]
    return res


# code principal
print(init_mat(2, 3))
print(init_mat(0, 0))