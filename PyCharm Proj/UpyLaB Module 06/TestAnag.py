def anagramme_list(a,b):
    res = False
    if len(a) == len(b):
        liste_b = list(b)
        res = True
        for i in a:
            if i in liste_b:
                liste_b.remove(i)
            else:
                res = False
    return res


# code principal
print('cas correct True : ', anagramme_list('gare', 'rage'))
print('cas correct True : ', anagramme_list('g', 'g'))

print('cas correct False : ', anagramme_list('garé', 'rage'))
print('cas correct False : ', anagramme_list('gare', 'tout'))

print('cas incorrect mot a plus long que mot b : ', anagramme_list('garer', 'rage'))
print('cas incorrect mot b plus long que mot a : ', anagramme_list('rage', 'garer'))

print('cas incorrect mot présence d\'un espace : ', anagramme_list('gare', 'rage '))

print('cas incorrect mot a contient un doublon : ', anagramme_list('rager', 'garea'))
