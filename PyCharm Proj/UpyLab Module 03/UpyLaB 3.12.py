n = int(input())

for i in range(n):
    string = i * ' ' + (n - i) * 'X'
    print(string)
