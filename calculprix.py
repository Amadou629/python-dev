x = float (input("saisir le prix "))
if x > 30000 :
    red = x - (0.3*x)
    print(f"le prix est : " ,x)
else :
    red = x + (0.3*x)
    print(f"le prix est : " ,x)