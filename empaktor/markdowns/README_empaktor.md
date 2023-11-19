# Empaktor 

## Description du programme 

Le programme ```empaktor.py``` est le logiciel permettant de compresser et décompresser les fichiers présents dans empaktor/. 

### Comment fonctionne-t-il ? 

Le programme principal réagit aux données entrées par l'utilisateur et détecte si l'entrée correspond à une requête de compression ou d'extraction, et exécute en conséquence une fonction ```compression``` ou une fonction ```décompression```.

```py 
# programme principal
if sys.argv[2] == "--compression": 
    compression()
elif sys.argv[1] == "--extract": 
    decompression()
else : 
    display_error()
```

## Comment l'utiliser ?

### Compresser 

```bash
python3 empaktor.py nom_archive.tar.gz --compression nom_algo fichier
```
- ```python3 empaktor.py``` exécute le programme.
- ```nom.archive.tar.gz``` est le nom qu'on donnera à l'archive compressée.
- ```--compression``` choisit l'utilisation de la compression.
- ```nom_algo``` est le nom du mode de compression que l'on souhaite utiliser ayant le choix parmi ```huffman```, ```rle``` et ```bwt```.
- ```fichier``` est le nom du fichier à compresser.

### Exemple 
```bash
python3 empaktor.py document.tar.gz --compression huffman document.txt
```

### Décompresser 

```bash
python3 empaktor.py --extract nom_archive.tar.gz
```

- ```python3 empaktor.py``` exécute le programme.
- ```--extract``` choisit l'utilisation de la décompression.
- ```nom.archive.tar.gz``` est le nom de l'archive à décompresser.

### Exemple 

```bash
python3 empaktor.py --extract document.tar.gz
```

## En cas d'erreur 

Le programme renverra : 
```py 
Wrong use of the program.
```

Vérifiez que les commandes entrées correspondent bien à celles indiquées ci-dessus.

