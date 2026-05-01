c = "2026"
saisi = ""
rep = 100
tent = 0
while c != saisi and rep > 0:
    saisi = input("Entrez le code : ")
    if saisi != c:
        if saisi < c:
            print("Code trop petit, essayez à nouveau.\n")
        if saisi > c:
            print("Code trop grand, essayez à nouveau.\n")
        rep -= 20
        tent += 1
        print(f"Il vous reste {rep} tentatives.\n")
    
    if rep <= 0:
        print("Vous avez épuisé toutes vos tentatives. Accès refusé.")
        break
print(f"Code correct, vous avez trouvé en {tent} tentative(s).")