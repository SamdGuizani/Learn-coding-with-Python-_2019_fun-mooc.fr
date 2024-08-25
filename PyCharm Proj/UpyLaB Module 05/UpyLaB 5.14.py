def my_remove(lst, e):
    if type(lst) is not list:
        lst = lst
    else:
        if e in lst:
            lst.remove(e)
    return


# code principal
l = [1, 2, 3, 4, 3, 2, 1]
my_remove(l, 2)
print(l)

l = [1, 2, 3, 4, 3, 2, 1]
my_remove(l, 5)
print(l)

l = (1, 2, 3)
my_remove(l, 2)
print(l)

l = 'aba'
my_remove(l, 'a')
print(l)