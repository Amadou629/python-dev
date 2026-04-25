nom = input("Entrez le  nom : ")
#for i in range(len(nom) -1, -1, -1):
    #print(nom[::-1])
#n = 0
#for i in range(0, len(nom) ,2):
    #print(nom[i], end="")
#for i in nom:
    #n = n + 1
#print(f"le nombre de caractere dans le nom {nom} est : {n} ")

t = 0
for i in range(len(nom)):
    if nom[i] != " ":
        t = t + 1
print(f"le nombre de caractere dans le nom {nom} est : {t} ")