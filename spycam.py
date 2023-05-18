import os
import webbrowser
import sys
from urls import pays_urls

def afficher_menu_principal():
    os.system('clear')  # Efface le terminal (pour Linux/macOS)
    os.system('cls')  # Efface le terminal (pour Windows)
    print("\033[1m" + "╔══════════════════════════╗")
    print("║        \033[94m\033[1mSpyCam\033[0m\033[1m        ║")
    print("╚══════════════════════════╝\033[0m")
    print("\nMenu Principal")
    print("1. Afficher SpyCam")
    print("2. Quitter")

def afficher_menu_camhack():
    os.system('clear')  # Efface le terminal (pour Linux/macOS)
    os.system('cls')  # Efface le terminal (pour Windows)
    print("\033[1m" + "╔══════════════════════════╗")
    print("║        \033[94m\033[1mSpyCam\033[0m\033[1m        ║")
    print("╚══════════════════════════╝\033[0m")
    print("\nMenu SpyCam")
    print("1. Belgique")
    print("2. France")
    print("3. Espagne")
    print("4. Italie")
    print("5. United States")
    print("6. Japan")

def afficher_menu_urls(urls, choix_camhack):
    os.system('clear')  # Efface le terminal (pour Linux/macOS)
    os.system('cls')  # Efface le terminal (pour Windows)
    print("\033[1m" + "╔══════════════════════════╗")
    print("║        \033[94m\033[1mSpyCam\033[0m\033[1m        ║")
    print("╚══════════════════════════╝\033[0m")
    pays = ""
    if choix_camhack == 1:
        pays = "Belgique"
    elif choix_camhack == 2:
        pays = "France"
    elif choix_camhack == 3:
        pays = "Espagne"
    elif choix_camhack == 4:
        pays = "Italie"
    elif choix_camhack == 5:
        pays = "United States"
    elif choix_camhack == 6:
        pays = "Japan"
    print(f"\nMenu URL - {pays}")
    urls_pays = urls[choix_camhack - 1][1]
    for i, url in enumerate(urls_pays, start=1):
        print(f"{i}. {pays}: {url}")

def ouvrir_url(url):
    if os.name == 'posix':  # Vérifie si l'environnement est Android avec Termux ou Linux
        if 'ANDROID_ROOT' in os.environ:
            os.system(f"termux-open-url {url}")  # Environnement Termux sur Android
        else:
            try:
                os.system(f"xdg-open {url}")  # Environnement Linux
            except OSError:
                print("Impossible d'ouvrir l'URL. Veuillez vérifier que xdg-utils est installé.")
    elif os.name == 'nt':  # Vérifie si l'environnement est Windows
        webbrowser.open(url)
        
# Fonction principale
def main():
    choix_principal = 0
    try:
        while choix_principal != 2:
            afficher_menu_principal()
            try:
                choix_principal = int(input("Choisissez une option: "))
            except ValueError:
                continue
            if choix_principal == 1:
                choix_camhack = 0
                while choix_camhack != 7:
                    afficher_menu_camhack()
                    try:
                        choix_camhack = int(input("Choisissez un pays (1-6) ou 7 pour revenir au menu principal CTRL + c pour quitter: "))
                    except ValueError:
                        continue
                    if choix_camhack in [1, 2, 3, 4, 5, 6]:
                        choix_url = 0
                        while choix_url != len(pays_urls[choix_camhack - 1][1]) + 1:
                            afficher_menu_urls(pays_urls, choix_camhack)
                            try:
                                choix_url = int(input(f"Choisissez une URL (1-{len(pays_urls[choix_camhack - 1][1])}) ou {len(pays_urls[choix_camhack - 1][1]) + 1} pour revenir au menu SpyCam: CTRL + c pour quitter:"))
                            except ValueError:
                                continue
                            if choix_url == 0:
                                continue
                            elif choix_url <= len(pays_urls[choix_camhack - 1][1]):
                                url_choisi = pays_urls[choix_camhack - 1][1][choix_url - 1]
                                ouvrir_url(url_choisi)
                            else:
                                print("URL invalide.")
                    elif choix_camhack != 7:
                        print("Choix non valide")
            elif choix_principal != 2:
                print("Choix non valide")
    except KeyboardInterrupt:
        print("\nProgramme interrompu.")
        sys.exit(0)
if __name__ == "__main__":
    main()

