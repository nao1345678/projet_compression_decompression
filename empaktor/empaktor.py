import sys
import shutil
import json
import os
import tarfile 
from cmp_huffman import huffman
from cmp_rle import rle
from cmp_burrows import burrows_wheeler


# fonction pour ouvrir le fichier
def open_file(name: str):
    '''Fonction qui ouvre un fichier et lit son contenu.'''
    with open(name, 'r') as file :
        data = file.read()
        file.close()
    return data


# fonction de création + ajout dans l'archive
def create_and_add(nom_archive: str, fichiers_a_archiver: list):
    '''Fonction qui prend en paramètres une archive et une liste de 
    fichiers associés à celle-ci, pour les ajouter par itération dans l'archive'''
    with tarfile.open(nom_archive, "w:gz") as archive:
        for file in fichiers_a_archiver:
            archive.add(file)
    return archive

# permet de récupèrer les fichiers à compresser 
def get_files():
    '''Récupère les fichiers à compresser'''
    lst_fichiers = sys.argv[4:]
    return lst_fichiers

# permet de récupérer les fichiers d'une archive 
def get_archive_files(nom_archive):
    '''Récupére les fichiers d'une archive'''
    with tarfile.open(nom_archive, 'r') as archive: 
        lst_fichiers_extraits = archive.getnames()       
    return lst_fichiers_extraits

# permet de vérifier si l'archive a un nom valide
def check_arch_name_comp():
    '''Fonction pour vérifier que l'archive a un nom valide'''
    if "tar.gz" in sys.argv[1]:
        return True


# permet de vérifier si l'archive a un nom valide
def check_arch_name_dec():
    '''Fonction pour vérifier que l'archive a un nom valide'''
    if "tar.gz" in sys.argv[2]:
        return True
    else : 
        return "Not an archive name. Try again."


# fonction pour créer un dossier 
def create_file(nom_dossier_a_creer):
    '''Création d'un dossier'''
    chemin = os.path.join(os.getcwd(), nom_dossier_a_creer)
    dossier = os.makedirs(chemin, mode=0o777)
    return dossier 
    

def create_and_write(nom_fichier: str, contenu):
    '''Fonction qui crée un fichier et écrit dedans'''
    with open(nom_fichier, 'w') as fichier:
        fichier.write(contenu)
    return fichier


def extract_files(nom_archive, dossier_destination):
    '''Fonction qui extrait une archive vers un dossier spécifié'''
    with tarfile.open(nom_archive, 'r') as archive:
        archive.extractall(dossier_destination)
    return dossier_destination


# fonction pour la compression
def compression(nom_archive, fichiers_a_compresser):
    '''Fonction qui prend en argument une archive compressée
    et une liste de fichiers à encoder, et qui renvoie le
    dossier archivé avec les données compressées'''

    nom_algo = sys.argv[3]
    liste_fichiers_encodes = []
    fichiers_a_compresser = get_files()

    if check_arch_name_comp():
        if nom_algo == "rle":
            for fichier in fichiers_a_compresser: 
                data = open_file(fichier)
                data = rle.encode_rle(data)
                fichier_encode = create_and_write(fichier, data)
                liste_fichiers_encodes.append(fichier_encode.name)
            archive = create_and_add(nom_archive, liste_fichiers_encodes)
            print("Compression avec RLE réussie.")
            return archive

        elif nom_algo == "huffman":
            for fichier in fichiers_a_compresser: 
                data = open_file(fichier)
                data = huffman.compress_data(data)
                data, key = data[0], data[1]
                key_file_name = "key_" + fichier 
                fichier_encode = create_and_write(fichier, data)
                fichier_key = create_and_write(key_file_name, str(key))
                liste_fichiers_encodes.append(fichier_encode.name)
                liste_fichiers_encodes.append(fichier_key.name)
            archive = create_and_add(nom_archive, liste_fichiers_encodes)
            print("Compression avec Huffman réussie.")
            return archive

        elif nom_algo == "bwt":
            for fichier in fichiers_a_compresser: 
                data = open_file(fichier)
                data = burrows_wheeler.transform_bwt(data)
                data,key = data[0], data[1]
                key_file_name = "key_" + fichier
                fichier_encode = create_and_write(fichier, data)
                fichier_key = create_and_write(key_file_name, str(key))
                liste_fichiers_encodes.append(fichier_encode.name)
                liste_fichiers_encodes.append(fichier_key.name)
            archive = create_and_add(nom_archive, liste_fichiers_encodes)
            print("Compression avec Burrows Wheeler réussie.")
            return archive

        else:
            return "Not an algorithm. Try again."
    else : 
        return "Not an archive name. Try again."


# fonction pour la décompression
def decompression(nom_archive: str):
    '''Fonction qui prend en argument une archive compressée 
    et renvoie les fichiers décodés dans le répértoire actuel'''
    
    nom_algo = sys.argv[3]
    lst_fichiers_decodes = []

    if check_arch_name_dec():

        #TOUCHE PLUS
        if nom_algo == "rle":
            nom_dossier_extraction =  nom_archive + "_temp"
            dossier_extraction = create_file(nom_dossier_extraction)
            dossier_extraction = extract_files(nom_archive, nom_dossier_extraction)
            for fichier in os.listdir(dossier_extraction):
                data = open_file(fichier)
                data = rle.decode_rle(data)
                fichier_decode = create_and_write(fichier, data)
                lst_fichiers_decodes.append(fichier_decode.name)
            
            nom_final = nom_archive[:-7]
            dossier_final = create_file(nom_final)

            for nom_fichier in lst_fichiers_decodes:
                chemin_fichier = os.path.join(os.getcwd(), nom_fichier)
                chemin_destination = os.path.join(nom_final, nom_fichier)
                shutil.move(chemin_fichier, chemin_destination)

            print("Décompression réussie.")
            return dossier_final
        #TOUCHE PLUS
    
        elif nom_algo == "huffman":
            nom_dossier_extraction =  nom_archive + "_temp"
            dossier_extraction = create_file(nom_dossier_extraction)
            dossier_extraction = extract_files(nom_archive, nom_dossier_extraction)
            lst_fichiers_decodes = []

            for fichier in os.listdir(dossier_extraction):
                if "key_" not in fichier :
                    cle = 'key_'+ fichier
                    data_key = open_file(cle)
                    data_key = data_key.replace("'",'"')
                    data_key = json.loads(data_key)
                    
                    for values in data_key.values():
                        values.replace("'", "")
                    
                    data = open_file(fichier)
                    data = huffman.decompress_data(data, data_key)
                    fichier_decode = create_and_write(fichier, data)
                    lst_fichiers_decodes.append(fichier_decode.name)
            
            nom_final = nom_archive[:-7]
            dossier_final = create_file(nom_final)

            for nom_fichier in lst_fichiers_decodes:
                chemin_fichier = os.path.join(os.getcwd(), nom_fichier)
                chemin_destination = os.path.join(nom_final, nom_fichier)
                shutil.move(chemin_fichier, chemin_destination)

            print("Décompression réussie.")
            return dossier_final

        #FINITO PIPPO
        elif nom_algo == "bwt":
            nom_dossier_extraction =  nom_archive + "_temp"
            dossier_extraction = create_file(nom_dossier_extraction)
            dossier_extraction = extract_files(nom_archive, nom_dossier_extraction)

            for fichier in os.listdir(dossier_extraction):
                if "key_" not in fichier :
                    cle = 'key_'+ fichier
                    data = open_file(fichier)
                    data = burrows_wheeler.inverse_bwt(data, int(open_file(cle)))
                    fichier_decode = create_and_write(fichier, data)
                    lst_fichiers_decodes.append(fichier_decode.name)
            
            nom_final = nom_archive[:-7]
            dossier_final = create_file(nom_final)

            for nom_fichier in lst_fichiers_decodes:
                chemin_fichier = os.path.join(os.getcwd(), nom_fichier)
                chemin_destination = os.path.join(nom_final, nom_fichier)
                shutil.move(chemin_fichier, chemin_destination)

            print("Décompression réussie.")
            return dossier_final
        #FINITO PIPPO
    
        else : 
            return "Not an algorithm. Try again."
    else : 
        return "Not an archive. Try again."


# programme principal
if sys.argv[2] == "--compression": 
    print(compression(sys.argv[1], get_files()))
elif sys.argv[1] == "--extract":
    print(decompression(sys.argv[2]))
else :
    print("Wrong input. Try again.")

