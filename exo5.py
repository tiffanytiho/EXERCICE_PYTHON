liste_utilisateur = input("Entrez une liste de nombres séparés par des espaces : ")

# Convertit la chaîne d'entrée en une liste de nombres
liste_nombres = [int(x) for x in liste_utilisateur.split()]

# Parcours de la liste et affichage des nombres divisibles par 5
print("Les nombres divisibles par 5 sont :")
for nombre in liste_nombres :
    if nombre % 5 == 0:
        print(nombre)
