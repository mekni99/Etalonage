def calculer_valeurs_etalonnage(lignes):
    total = 0
    for ligne in lignes:
        chiffres = [char for char in ligne if char.isdigit()]
        if len(chiffres) >= 2:
            premier = chiffres[0]
            dernier = chiffres[-1]
            valeur = int(premier + dernier)
            total += valeur
    return total
print("Entrez vos lignes de texte (une ligne à la fois).")
print("Appuyez sur Entrée sans taper de texte pour terminer.")

lignes = []
while True:
    ligne = input("")
    if ligne == "": 
        break
    lignes.append(ligne)

# Calcul du total
total = calculer_valeurs_etalonnage(lignes)
print(f"Le total des valeurs d'étalonnage est : {total}")
