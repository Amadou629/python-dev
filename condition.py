x = int(input("Entrer un entier : "))
y = float(input("entrer un nombre : "))
# DIVISION
if y != 0:
    div = x/y
    print(f"la division de {x} et {y} est : {div}\n")
else:
    print("erreur : division par zero n'est pas autorisee.\n")
    print("vous ne pouvez pas diviser par zero.")
# Modulo
if y != 0:
    mod = x % y
    print(f"le modulo de {x} et {y} est : {mod}\n")
else:
    print("saisissez la bonne valeur")


nom = input("Quel est votre nom ?")
note1 = float(input("premiere note"))
note2 = float(input("seconde note"))
note3 =float(input("entrez la troisieme note"))
som = note1 + note2 + note3
moy = som / 3

if moy >= 10:
    print(f"felicitations {nom}, vous avez reussi avec une moyenne de {moy:.2f} ! ")
elif moy >= 7:
    print(f"{nom}, vous avez une moyenne de {moy:.2f}. vous etes en zone de rattrapage")
else:
    print(f"Désolé{nom}, vous avez échoué avec une moyenne de {moy:.2f}.")