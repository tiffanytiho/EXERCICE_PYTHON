# Exo 2 : Calculer la factorielle d’un nombre
def nombre_fac(n):
    factoriel = 1
    for i in range(1, n + 1):
        factoriel = factoriel * i
    return factoriel

# sauvegarde des nombres saisis
nombre_saisi = int(input("Entrez un nombre : "))

factoriel = nombre_fac(nombre_saisi)

# le f permet à la variable nombre_saisi de prendre la valeur qui a été saisie et de pouvoir l'afficher dans le print
print(f"La factorielle de {nombre_saisi} est : {factoriel}")
