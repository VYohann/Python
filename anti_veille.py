import pyautogui
import math
import time

# Fonction pour détecter le mouvement de la souris
def detecter_mouvement_souris():
    position_initiale = pyautogui.position()
    time.sleep(5)  # Attendez 5 secondes pour détecter le mouvement

    # Vérifiez si la position de la souris a changé
    nouvelle_position = pyautogui.position()
    if nouvelle_position != position_initiale:
        return True
    else:
        return False

# Boucle pour éviter la mise en veille
while True:
    if detecter_mouvement_souris():
        #pass
        print("Mouvement de la souris détecté.")
    else:
        # Si aucun mouvement n'est détecté, déplacez la souris d'1 pixel
        pyautogui.move(10, 0)
        time.sleep(0.1)
        pyautogui.move(-10, 0)

    time.sleep(30)  # Attendez xx secondes avant de vérifier à nouveau
