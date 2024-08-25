def my_count(lst, e):
    if type(lst) is not list:
        n_element = 0
    else:
        n_element = 0
        for i in range(len(lst)):
            if lst[i] == e:
                n_element += 1
    return n_element


# code principal
print(my_count([1, 2, 3, 4, 3, 2, 1], 3))
print(my_count([1, 2, 3], 4))
print(my_count(['a', 'b'], 2))
print(my_count((2, 3, 5), 2))
print(my_count(2, 2))
print(my_count('aba', 'a'))