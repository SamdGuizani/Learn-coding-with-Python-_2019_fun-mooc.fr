def wc(nomFichier):
    """wc est une fonction permettant de compter le nombre de caractères, le nombre de mots et le nombre de lignes
    dans un fichier txt """

    # ouverture fichier texte et affectation du contenu à une variable chaine de caractères txt
    with open(nomFichier, encoding='utf-8') as f:
        txt = f.read()

    # comptage caractères
    nb_c = len(txt)

    # comptage mots
    m = ''
    lst = []
    for i in range(len(txt)):
        if txt[i].isalnum():
            m += txt[i]
        else:
            lst.append(m)
            m = ''
    lst = [m for m in lst if m != '']
    nb_m = len(lst)

    # comptage lignes
    nb_l = 0
    for line in open(nomFichier):
        nb_l +=1

    return nb_c, nb_m, nb_l


# Code principal
print(wc('C:\\Users\\Samd\\PycharmProjects\\MOOC Apprendre Python\\UpyLaB\\wc1.txt'))
print(wc('C:\\Users\\Samd\\PycharmProjects\\MOOC Apprendre Python\\UpyLaB\\Zola.txt'))
print(wc('C:\\Users\\Samd\\PycharmProjects\\MOOC Apprendre Python\\UpyLaB\\le-petit-prince.txt'))
