import os
import subprocess
import time

# Saisie du chemin du dossier
dossier = input("Entrez le chemin du dossier à examiner: ")

# Vérification de l'existence du dossier
if not os.path.exists(dossier):
    print("Le dossier spécifié n'existe pas.")
else:
    # Liste pour stocker les noms de fichiers et de dossiers
    noms = []

    # Parcours du dossier
    for element in os.listdir(dossier):
        noms.append(element)

    # Formater les noms pour la liste en Python
    noms_formates = [f'"{nom}"' if os.path.isfile(os.path.join(dossier, nom)) else f'"{nom}"' for nom in noms]

    # Chaîne finale à écrire dans le fichier bloc-notes
    chaine_finale = f'noms_a_rechercher = [{", ".join(noms_formates)}]'

    # Chemin du fichier bloc-notes
    chemin_bloc_notes = 'here.txt'

    # Écriture de la chaîne finale dans le fichier bloc-notes
    with open(chemin_bloc_notes, 'w') as fichier:
        fichier.write(chaine_finale)

    print("Noms des fichiers et dossiers formatés copiés dans le bloc-notes.")

    # Mettre en pause le terminal pendant 2 secondes
    time.sleep(2)

     # Ouvrir le fichier bloc-notes avec le bloc-notes par défaut du système
    subprocess.Popen(['notepad.exe', chemin_bloc_notes])

    sys.exit(0)
