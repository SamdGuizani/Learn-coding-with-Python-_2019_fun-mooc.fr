def deux_egaux(a, b, c):
    if (a == b) or (a == c) or (b == c):
        res = True
    else:
        res = False
    return res

x = int(input())
y = int(input())
z = int(input())

print(deux_egaux(x, y, z))