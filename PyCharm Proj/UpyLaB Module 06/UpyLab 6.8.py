def decompose(email):
    """Decompose une adresse e-mail en nom et domaine:
    ex. pour email = 'prenom.nom@domaine.com', la fonction renvoie un couple (nom, domaine)
    avec nom = 'prenom.nom' et domaine = 'domaine.com' """
    nom = str(email.split('@')[0])
    domaine = str(email.split('@')[1])
    return nom, domaine


def store_email(liste_mails):
    """Reçoit en paramètre une liste d’adresses e-mail et qui renvoie un dictionnaire avec comme clés les domaines
    des adresses e-mail et comme valeurs les listes d’utilisateurs correspondantes, triées par ordre croissant (
    UTF-8) """
    d = {}

    # Création du dictionnaire
    for e in liste_mails:
        e_decomp = decompose(e)
        if e_decomp[1] not in d:
            d[e_decomp[1]] = [e_decomp[0]]
        else:
            d[e_decomp[1]].append(e_decomp[0])

    # Tri des valeurs dans chaque entrée du dictionnaire
    for k in d:
        d[k].sort()

    return d


# code principal
print(store_email(["ludo@prof.ur", "andre.colon@stud.ulb",
             "thierry@profs.ulb", "sébastien@prof.ur",
             "eric.ramzi@stud.ur", "bernard@profs.ulb",
             "jean@profs.ulb" ]))