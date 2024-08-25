def categorie(vent):
   """renvoie la catégorie de cyclone enregistré en fonction du vent"""

   assert vent > 118 # sinon provoque une erreur dans le code

   if vent < 154:
       res = 1
   elif vent < 178:
       res = 2
   elif vent < 210:
       res = 3
   elif vent < 251:
       res = 4
   else: # catégorie 5
       res = 5
   return res


def historique_tempetes(vent_max):
   """affiche pour chaque année la catégorie de vents subis cette année-là
   entrée : vent_max: liste des vents maximums enregistrés en km/h
   chaque année (composante 0 étant pour l'an 2000)"""

   annee = 2000
   for vent in vent_max:
       if vent < 64:
           print("En", annee, ": pas de tempête enregistrée")
       elif vent < 119:
           print("En", annee, ": il y a eu au moins une tempête mais pas de cyclone")
       else:
           print("En", annee, ": le plus gros cyclone enregistré était de catégorie", categorie(vent))
           annee += 1
           return None


def cyclone_annee(vent_max, annee):
   """renvoie la catégorie de cyclone à laquelle les îles ont été confrontées
   pour l'année annee à partir de 2000)"""

   assert annee >= 2000 # si annee est inférieure à 2000, provoque une erreur

   vent = vent_max[annee - 2000] # valeur de vent pour cette année
   if vent < 119: # pas de cyclone
       res = 0
   else:
       res = categorie(vent) # appel de la fonction categorie pour déterminer la catégorie
   return res


mes_valeurs = [75, 200, 230, 260, 100, 80, 50, 45, 180, 100, 200, 63, 64, 65,\
        118, 119, 153, 154, 280]

historique_tempetes(mes_valeurs)

for i in (2001, 2002, 2003, 2009):
    print(cyclone_annee(mes_valeurs, i))