def liste_des_mots(file):
    # ouverture fichier texte et affectation du contenu à une variable chaine de caractères txt
    with open(file, encoding='utf-8') as f:
        txt = f.read()

    # liste de tous les mots présents dans txt
    separateurs = ' -\'"?!:;.,*=()1234567890\n\t'
    m = ''
    lst = []
    for c in txt:
        if c not in separateurs:
            m += c
        else:
            lst.append(m.lower())
            m = ''
    lst = [m for m in lst if m != '']

    # tri alphabétique de la liste lst
    lst.sort()

    # retrait des mots en double
    lst_sans_doublons =[]
    for m in lst:
        if m not in lst_sans_doublons:
            lst_sans_doublons.append(m)

    return lst_sans_doublons


# code principal
print(liste_des_mots('C:\\Users\\Samd\\PycharmProjects\\MOOC Apprendre Python\\UpyLaB\\Zola.txt'))
print(liste_des_mots('C:\\Users\\Samd\\PycharmProjects\\MOOC Apprendre Python\\UpyLaB\\le-petit-prince.txt'))
