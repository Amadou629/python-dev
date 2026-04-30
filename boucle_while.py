mp = "2020"
saisi = ""
tentative = 0
while mp != saisi:
    saisi = input("Entrez le mot de passe : ")
    tentative += 1
    if saisi != mp:
        print("Mot de passe incorrect, essayez à nouveau.\n")
print(f"Mot de passe correct, vous avez trouvé en {tentative} tentative(s).")

print("-----------------------------------------------------")

pv = 100
tour = 1
while pv > 0:
    pv -= 15
    tour += 1
    print(f"tour {tour} : PV = {pv} \n")
    if pv < 20:
        print("Attention santé critique ! pv = {pv}\n")

print(f"la personne est morte avec PV = {pv}")