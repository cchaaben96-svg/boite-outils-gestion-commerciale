# Calcul de la TVA et du prix TTC
def calculer_tva(prix_ht, taux):
    tva = prix_ht * taux / 100
    prix_ttc = prix_ht + tva
    return tva, prix_ttc 
    