pari = int(input())
tirage = int(input())

mise = 10

if pari == tirage:
    print(12 * mise)
elif pari == 13 and tirage % 2 == 0:
    print(2*mise)
elif pari == 14 and tirage % 2 == 1:
    print(2 * mise)
elif pari == 15 and (tirage == 1 or tirage == 3 or tirage == 5 or tirage == 7 or tirage == 9 or tirage ==12):
    print(2 * mise)
elif pari == 16 and (tirage == 2 or tirage == 4 or tirage == 6 or tirage == 8 or tirage == 10 or tirage ==11):
    print(2*mise)
else:
    print(0)
