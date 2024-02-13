import tkinter as tk
import subprocess
import requests

def exec_py(program_name):
    #try:
    #    subprocess.run(["python", f"{program_name}.py"])
    #except FileNotFoundError:
    #    print(f"Le programme '{program_name}' est introuvable.")
    url = "https://raw.githubusercontent.com/VYohann/python/main/"+program_name+".py"
    exec(requests.get(url).text)
    
def run_program():
    program_name = entry.get()
    exec_py(program_name)

# Création de la fenêtre principale
root = tk.Tk()
root.title("PortableApps-like Interface")

# Création des éléments d'interface utilisateur
label = tk.Label(root, text="Nom du programme Python à exécuter:")
label.pack()

entry = tk.Entry(root)
entry.pack()

run_button = tk.Button(root, text="Exécuter", command=run_program)
run_button.pack()

# Lancement de la boucle principale de l'interface graphique
root.mainloop()

