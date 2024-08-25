n = int(input()) # Nb de ligne de la pyramide

for i in range(1, n + 1):
    k = i
    string = ''
    for j in range (1, 2 * i):
        if j < i:
            x = k % 10
            string += str(x)
            k += 1
        elif j >= i:
            x = k % 10
            string += str(x)
            k -= 1
    string = str((n - i) * ' ' + string + (n - i) * ' ')
    print(string)