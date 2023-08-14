word = input("Entrez un mot : ")
result = ""

for i, letter in enumerate(word):
    if i % 2 == 0:
        result += letter.upper()
    else:
        result += letter.lower()

print("Résultat :", result)
