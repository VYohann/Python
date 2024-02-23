import os

def rechercher_fichier(nom_fichier, chemin='C:/Chemin/De/Départ'):
    for dossier_parent, dossiers, fichiers in os.walk(chemin):
        if nom_fichier in fichiers:
            chemin_complet = os.path.join(dossier_parent, nom_fichier)
            print(f'Le fichier {nom_fichier} a été trouvé à l\'emplacement : {chemin_complet}')
            return chemin_complet
    print(f'Le fichier {nom_fichier} n\'a pas été trouvé dans le répertoire {chemin}')
    return None

while True:
    nom_fichier_recherche = input("Nom du fichier?: ")

    # Exemple d'utilisation
    #nom_fichier_recherche = '$MB52.txt'
    chemin_de_depart = 'C:/'

    rechercher_fichier(nom_fichier_recherche, chemin_de_depart)
