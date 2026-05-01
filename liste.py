# les listes
#creation d'une liste
ma_liste = ["sadio", 25, "oumar", 5]
print(len(ma_liste)) #affiche le nombre d'éléments dans la liste
print(ma_liste[0]) #affiche le premier élément de la liste
print(ma_liste[1]) #affiche le deuxième élément de la liste
print(ma_liste[-1]) #affiche le dernier élément de la liste

#fonction append() pour ajouter un élément à la fin de la liste
ma_liste.append("mamadou")
print(f"liste avec append {ma_liste}")

#fonction insert() pour ajouter un élément à une position spécifique de la liste
ma_liste.insert(1, "abdou")
print(f"liste avec insert {ma_liste}")