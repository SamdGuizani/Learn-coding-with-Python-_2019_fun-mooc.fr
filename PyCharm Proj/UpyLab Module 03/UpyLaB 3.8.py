TypePoly = input()  # Type polyèdre
a = float(input())

if TypePoly == 'T':
    print(2**0.5 / 12 * a**3)
elif TypePoly == 'C':
    print(a**3)
elif TypePoly == 'O':
    print(2**0.5 / 3 * a**3)
elif TypePoly == 'D':
    print((15 + 7 * 5**0.5) / 4 * a**3)
elif TypePoly == 'I':
    print(5 * (3 + 5**0.5) / 12 * a**3)
else:
    print('Polyèdre non connu')
