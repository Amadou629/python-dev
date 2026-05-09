def calculer_somme():
    a =float(input("entrer le premier entier:"))
    b = float(input("entrer le second entier: "))
    somme = a + b
    return somme
resultat = calculer_somme()
print(f"la somme est : {resultat}")

def moyenne():
    a = float(input("entrer la première note: "))
    b = float(input("entrer la deuxième note: "))
    c = float(input("entrer la troisième note: "))
    moy = (a + b + c) / 3
    return moy

resultat_moyenne = moyenne()
print(f"la moyenne est : {resultat_moyenne}")
if resultat_moyenne >= 10:
    print("vous avez réussi")
else:    print("vous avez échoué")