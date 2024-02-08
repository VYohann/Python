import requests

#url = "https://raw.githubusercontent.com/VYohann/Python/main/fonction.py"
url = input("Url du fichier python a executer: ")

# Télécharger le contenu du fichier depuis l'URL
response = requests.get(url)

# Vérifier si le téléchargement s'est bien passé (code 200)
if response.status_code == 200:
    # Execute le contenu du fichier
    exec(response.text)
else:
    print(f"Échec du téléchargement. Code de statut : {response.status_code}")

