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

# Fonction pour effectuer un mouvement circulaire de diamètre 20 pixels
def mouvement_circulaire():
    rayon = 10  # La moitié du diamètre
    centre_x, centre_y = pyautogui.position()
    angle = 0

    while True:
        # Calcul des coordonnées polaires
        x = int(centre_x + rayon * math.cos(math.radians(angle)))
        y = int(centre_y + rayon * math.sin(math.radians(angle)))

        # Déplacement de la souris aux coordonnées calculées
        pyautogui.moveTo(x, y)
        time.sleep(0.01)  # Réglage de la vitesse du mouvement

        # Augmentation de l'angle pour effectuer un mouvement circulaire
        angle += 1

        if angle == 360:
            angle = 0
            break

# Boucle pour éviter la mise en veille
while True:
    if detecter_mouvement_souris():
        #pass
        print("Mouvement de la souris détecté.")
    else:
        # Si aucun mouvement n'est détecté, déplacez la souris d'1 pixel
        #pyautogui.move(1, 0)
        mouvement_circulaire()

    time.sleep(30)  # Attendez 60 secondes avant de vérifier à nouveau
