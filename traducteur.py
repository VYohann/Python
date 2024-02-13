from googletrans import Translator
import keyboard
from colorama import init, Fore, Back, Style
import pyperclip

# Initialisation de colorama
init()

def translate_text(text, source_language='auto', target_language='fr'):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src=source_language, dest=target_language)
    return translation.text

key = ''
ctrl_pressed = False

def traduire(text, source_lg, target_lg):
    try:
        translation = translate_text(text, source_lg, target_lg)
        print(f'{Fore.MAGENTA + Back.WHITE}\nTraduction :\n {text} =>\n {translation}')
    except Exception as e:
        print(f'Erreur lors de la traduction : {str(e)}')
    print(Fore.GREEN + Back.BLACK + '--------------------')

def on_press(event):
    global key, ctrl_pressed
    cle = event.name

    if cle == '<':
        text = pyperclip.paste()
        traduire(text, source_language, target_language)

    key = key + ' ' + cle

def on_release(event):
    global ctrl_pressed
    cle = event.name

keyboard.on_press(on_press)
keyboard.on_release(on_release)

if __name__ == '__main__':
    source_language = 'en'
    target_language = 'fr'
    choix = '(1) Anglais vers Français'

    while True:
        print(Fore.GREEN + Back.BLACK + 'Choisissez la direction de traduction : (1) Anglais vers Français, (2) Français vers Anglais, (q) Quitter : \nLa touche "<" traduit automatiquement le texte copié. ')
        text = input('Entrez le texte à traduire {} : '.format(choix))

        if text == '1':
            source_language = 'en'
            target_language = 'fr'
            choix = '(1) Anglais vers Français'
        elif text == '2':
            source_language = 'fr'
            target_language = 'en'
            choix = '(2) Français vers Anglais'
        elif text.lower() == 'q':
            break
        elif text.lower() == 'k':
            print(f'Keys : {key}')
            key = ''
        elif text == '_':
            # Effacer le texte de la console
            key = ''
            print("\033c")  # Code pour effacer la console
        else:
            traduire(text, source_language, target_language)

# Réinitialisation de colorama à la fin du programme
init(autoreset=True)
input('Appuyez sur Entrée pour quitter...')
