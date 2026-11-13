def calculer_marge(vente, achat):
    marge= vente - achat
    taux_marge=(marge / achat) * 100
    taux_marque=(marge / vente) * 100
    return marge, taux_marge, taux_marque