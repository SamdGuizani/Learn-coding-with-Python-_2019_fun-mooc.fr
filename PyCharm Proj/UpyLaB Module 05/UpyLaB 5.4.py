def plus_grand_bord(w):
    res = ''
    i = 1  # compteur
    while i < len(w):
        bord_deb = w[:(len(w)-i)]
        bord_fin = w[i:len(w)]
        if bord_deb == bord_fin:
            res = bord_deb
            i = len(w) - 1
        i += 1
    return res


# Code principal
print(plus_grand_bord('abdabda'))
print(plus_grand_bord('abcabd'))
print(plus_grand_bord('abcba'))
