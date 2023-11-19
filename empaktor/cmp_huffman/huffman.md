# Algorithme d'Encodage Huffman 

## Encodage

### Prototype et paramètres

```py
def compress_data(chaine: str) -> str, dict: 
```
*Entrée :* une chaîne de caractères "data" (type: str) qui sera compressée dans la fonction en utilisant le code d'Huffman. 

*Sortie:* une suite de 0 et de 1 (type: str), qui correspond aux données compressées par l'algorithme.

### Description de l'algorithme

*Etape 1 :*
Créer une table de fréquence de ```data``` grâce à une fonction qui renvoie un dictionnaire, qui associe les caractères de la chaîne à leur nombre d'occurence dans celle-ci.

```py
def table_frequence(chaine: str): -> dict
```

*Etape 2 :*
Créer un arbre de Huffman à partir de cette table de fréquence grâce à la fonction ```huffman_tree()```. 
Un arbre de Huffman attribue des codes binaires plus courts aux éléments fréquents et des codes plus longs aux éléments moins fréquents, grâce à la fonction ```codes()```.

```py
# création d'un arbre de huffman
def huffman_tree(table_frequence: dict): 

# attribution des codes binaires
def codes(node: Noeud, prefix: str = '', code = None):
```

*Etape 3 :* 
Compresser les données dans une fonction principale qui utilise les fonctions précédentes. Cette fonction de compression ajoute à une chaîne de caractères vides les codes binaires du dictionnaire créé grâce à ```codes()``` en fonction du caractère parcouru dans le paramètre ```chaine: str```.

```py
def compress_data(chaine: str) -> str, dict:
```

### Exemple 

*Entrée :*
```py
# affichage de "hello" compressé avec l'algo de huffman 
# en sélectionnant le premier élément du tuple renvoyé  
print(compress_data("hello")[0])
```

*Sortie :*
```py
# résultat 
0110111100
```

## Décodage

### Prototype et paramètres 

```py
def decompress_data(chaine_compressee: str, dico: dict): ->  str
```
*Entrée :* une chaîne de caractères (type: str) déja compréssée par la fonction ```compress_data()```, qu'on va venir décoder, ainsi qu'un dictionnaire (type: dict) contenant chaque caractère et son code binaire encodé grâce à la fonction ```codes()```.

*Sortie :* une chaîne de caractères (type: str) décodée

### Description de l'algorithme 

*Etape 1 :*
Parcourir le code compressé passé en paramètres pour pouvoir effectuer une comparaison de celui-ci avec les valeurs du dictionnaires.

```py
while len(chaine_compressee) > 0:
```

*Etape 2 :* 
Si les deux premiers éléments de la chaîne compressée correspond à la valeur du dictionnaire, on ajoute la clé à la chaîne finale, et on oublie pas de retirer le caractère déjà traité de la chaîne compressée, au risque de créer une boucle infinie.

```py
for key in dico : 
            if chaine_compressee[0:len(dico[key])] == dico[key] : 
                donnees_decodees += key        
```

*Etape 3:*
Renvoyer le résultat décodé à la fin de la boucle ```while```.

### Exemple

*Entrée :*
```py
# on assigne les paramètres à des variables
# puis on affiche le résultat de la décompression
code, dico = '0110111100', {'o': '00', 'h': '01', 'e': '10', 'l': '11'}
print(decompress_data(code, dico))
```

*Sortie :*
```py
hello
```

