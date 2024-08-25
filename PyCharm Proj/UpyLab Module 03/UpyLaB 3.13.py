n = int(input())  # Nb de valeurs à sommer. Si n positif, liste finie, si n<0 liste infinie (clôturée par entrée F)
sum = 0

if n == 0:
    print(sum)
elif n>0:
    for i in range(n):
        x = int(input())
        sum += x
    print(sum)
elif n<0:
    x = 0
    while x != 'F':
        x = input()
        if x == 'F':
            print(sum)
        else:
            x = int(x)
            sum += x