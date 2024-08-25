def my_insert(list_input, n):
    if type(n) is not int:
        list_output = None
    else:
        list_output = list_input.copy()
        i = 0
        while i < len(list_output):
            if n < list_input[0]:
                list_output.insert(0, n)
                i = len(list_output) - 1
            elif n > list_output[len(list_output) - 1]:
                list_output.insert(len(list_output), n)
                i = len(list_output) - 1
            elif i < len(list_output) - 1 and list_output[i] < n and n < list_output[i + 1]:
                list_output.insert(i + 1, n)
                i = len(list_output) - 1
            i += 1
    return list_output


# Code principal
print(my_insert([1, 3, 5], 4))
print(my_insert([2, 3, 5], 1))
print(my_insert([1, 2, 3, 4], 6))
print(my_insert([2, 3, 5], 0.5))

lst = [1,5,78]
print(my_insert(lst, -1))