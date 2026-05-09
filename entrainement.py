utilisateur = {
    "nom": "Alice",
    "age": 17,
    "abonnement": "premium"
}
if utilisateur["age"] >= 18:
    if utilisateur["abonnement"] == "premium":
        print("accès complet au site ! \n")
    else:
        print("accès limité ! \n")
else:
    print("accès refusé !")

print("------------------------------------------------")
articles = ["Accueil", "A propos", "Blog", "Contact"]
for article in articles:
    if article == "Blog":
        print(article, "page populaire")
    else:
        print(article)