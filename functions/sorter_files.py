# coding:utf-8
import os
import sys
import time


def sort_files():
    default_path = os.path.join(os.path.expanduser("~"), "Downloads")

    def animate_loading(atime=3.8, btime=0.5):
        time.sleep(btime)
        symbols = ["/", "-", "\\", "|", "-"]
        start_time = time.time()
        while True:
            for symbol in symbols:
                args = atime
                sys.stdout.write('\r' + 'Chargement ' + symbol)
                sys.stdout.flush()
                time.sleep(0.1)
                if time.time() - start_time > args:
                    print('\r')
                    return

    path = input("Quel dossier trier ? ( /Download/ par défaut ) : ")

    if os.path.isdir(path):
        msg = "Analyse des fichiers en cours..."
        print(msg)
        animate_loading()

    elif len(path) == 0:
        msg = "Chemin : /Downloads/ séléctioné. Analyse des fichiers en cours..."
        print(msg)
        path = default_path
        animate_loading()

    elif not os.path.exists(path):

        while path is not os.path.isdir(path):

            path = input("Le chemin est incorrect. Entrez un chemin d'accès valide : ")

            if os.path.isdir(path):
                print("Chemin correct. Analyse des fichiers en cours...")
                animate_loading(atime=2.3, btime=0.4)
                break

            elif len(path) == 0:
                path = default_path
                print("La valeur par défaut a été apliquée")
                animate_loading(atime=2.3, btime=0.8)
                break

    # Lecture du fichier de configuration
    with open('./config/sorter/config_extensions.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()

    # Initialisation du dictionnaire d'config
    extensions = {}

    # Parcours des lines du fichier de configuration
    for i, line in enumerate(lines):
        # Recherche de la ligne commençant par '%%%'
        if line.startswith(u'%%%'):
            # Extraction du nom après '%%%'
            name = line[3:].strip()
            # Initialisation de la liste d'config correspondante
            extensions[name] = []
            # Parcours des lignes suivantes jusqu'à la prochaine ligne '%%%' ou la fin du fichier
            j = i + 1
            while j < len(lines) and not lines[j].startswith(u'%%%'):
                # Ajout de l'extension à la liste
                ext = lines[j].strip()
                if ext.startswith('.'):
                    extensions[name].append(ext)
                j += 1

    # Initialisation des listes pour stocker les dossiers créés et ceux déjà existants
    dossiers_crees = []
    dossiers_existant = []

    # On boucle pour créer (ou pas) les dossiers s'ils ne le sont pas
    for f in extensions:
        slash = "\\\\"
        # mettre avant le "f" deux \\
        if not os.path.exists(path + slash + f):
            os.mkdir(path + slash + f)
            dossiers_crees.append(f)
        elif os.path.exists(path + slash + f):
            dossiers_existant.append(f)

    # Impression des dossiers créés et ceux déjà existants à la fin de la boucle
    if dossiers_crees:
        print(u"Les dossiers suivants ont été créés : " + ", ".join(dossiers_crees))
    if dossiers_existant:
        print(u"Les dossiers suivants étaient déjà existants : " + ", ".join(dossiers_existant))

    for files in extensions:
        key_list = list(extensions.keys())
        key_list.append(files)
        valeurs = list(extensions.values())
        valeurs.append(files)

    # parcours des fichiers dans le dossier
    for file_name in os.listdir(path):
        # extraction de l'extension du nom de fichier
        extension = os.path.splitext(file_name)[1]
        # parcours des clés du dictionnaire
        for key in extensions.keys():
            # vérification si l'extension est dans la liste de l'élément du dictionnaire
            if extension in extensions[key]:
                # Modification de l'emplacement des fichers, donc, tri !
                res = os.path.join(path, key, file_name)
                os.replace(os.path.join(path, file_name), res)
