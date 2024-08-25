def my_insert(list_input, n):
    assert type(n) is int
    i = 0
    while i < len(list_input):
        if n < list_input[0]:
            list_input.insert(0, n)
            i = len(list_input) - 1
        elif n > list_input[len(list_input) - 1]:
            list_input.insert(len(list_input), n)
            i = len(list_input) - 1
        elif i < len(list_input) - 1 and list_input[i] < n and n < list_input[i + 1]:
            list_input.insert(i + 1, n)
            i = len(list_input) - 1
        i += 1
    return


# Code principal
l = [1, 3, 5]
my_insert(l, 4)
print(l)

l = [1, 3, 5]
my_insert(l, 'a')
print(l)
