def substitue(message, abreviation):

    # liste de tous les mots présents dans message (dans leur ordre d'apparition)
    separateurs = ' '
    m = ''
    lst = []
    for c in message:
        if c not in separateurs:
            m += c
        else:
            lst.append(m)
            m = ''
    lst.append(m)

    # écriture du message non abrégé (variable res)
    res = ''
    for m in lst:
        if m in abreviation:
            res += abreviation[m]
            res += ' '
        else:
            res += m
            res += ' '

    return res.strip()


# code principal
print(substitue('C. N. cpt 2 to inf', {'C.' : 'Chuck',
                                 'N.' : 'Norris',
                                 'cpt' : 'counted',
                                 '2' : 'two times',
                                 'inf' : 'infinity'}))