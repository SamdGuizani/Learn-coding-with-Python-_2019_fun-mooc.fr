def belongs_to_file(word, filename):
    """Renvoie True si le mot word se trouve dans le fichier texte indiqué par filename.
    Il est supposé que chaque mot est sur une ligne dans le fichier filename"""
    with open(filename) as f:
        txt = f.readlines()
    # Nettoyage caractères retour de ligne
    for i in range(len(txt)):
        txt[i] = txt[i].strip()
    if word in txt:
        res = True
    else:
        res= False
    return res


# code principal
print(belongs_to_file("renard", "C:\\Users\\Samd\\PycharmProjects\\MOOC Apprendre Python\\UpyLaB\\words.txt"))
print(belongs_to_file('prince', "C:\\Users\\Samd\\PycharmProjects\\MOOC Apprendre Python\\UpyLaB\\words.txt"))