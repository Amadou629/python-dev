dict = {
    'nom': 'Alhassane',
    'age': '25',
    'ville': 'conakry'
}
print(dict)


etudiant = {
    "nom": "sadio",
    "note": 15
}
# ou bien
etudiant = {}
etudiant["nom"] = input("entrez votre nom : ")
etudiant["note"] = float(input("entrez une note : "))
for x,y in etudiant.items():
    print(f"{x} : {y}")