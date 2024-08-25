def print_mat(M):
    if M == []:
        print('\n')
    else:
        for i in range(len(M)):
            l = ''
            for k in range(len(M[i])):
                l = l + str(M[i][k]) + ' '
            print(l)
    return


# Code principal
ma_matrice = eval(input())
print_mat(ma_matrice)
"""print_mat([[1, 2], [3, 4], [5, 6]])
print_mat([])"""