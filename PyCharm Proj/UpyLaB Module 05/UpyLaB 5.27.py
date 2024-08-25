def symetrie_horizontale(A):
    A_symH = []
    if A == []:
        A_symH = A_symH
    else:
        for i in range(len(A)-1, -1, -1):
            A_symH.append(A[i])
    return A_symH


# Code principal
print(symetrie_horizontale([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(symetrie_horizontale([['a', 'b'], ['c', 'd']]))
print([])