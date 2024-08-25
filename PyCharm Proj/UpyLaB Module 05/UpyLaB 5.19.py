hist_path = input()  # saisir le chemin du fichier histoire
hist = open(hist_path)
hist_str = hist.read()

noms = []
new_entry = ''
while new_entry != 'FINI':
    new_entry = input()
    noms.append(new_entry)
del noms[len(noms) - 1]
noms = tuple(noms)

print(hist_str.format(*noms), end='')