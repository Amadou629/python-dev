code = 1337
energie = 100
saisi = 0
while saisi != 1337 and energie > 0:
    saisi = int(input("Entrez le code : "))
    if saisi != code:
        print("Code incorrect, essayez à nouveau.\n")
        energie -= 25
        print(f"Il vous reste {energie}% d'énergie.\n")
    
    if energie <= 0:
        print("Vous avez épuisé toute votre énergie. Accès refusé.")
        break
print("Code correct, vous avez trouvé le code secret !")