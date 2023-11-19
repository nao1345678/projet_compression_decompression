import heapq
import pandas as pd

# création de la classe Noeud pour la création de l'arbre de huffman 
class Noeud:
    def __init__(self, char, frequency):
        self.frequency = frequency
        self.char = char
        self.right = None
        self.left = None

    def __lt__(self, other):
       return self.frequency < other.frequency


# création d'une fonction qui crée un arbre de Huffman
def huffman_tree(table_frequence):

    '''Création d'un arbre de Huffman
    Entree : dictionnaire correspondant une table de fréquence
    Sortie : arbre de Huffman
    '''
    # création d'une pile
    heap = [Noeud(char, frequency) for char, frequency in
            table_frequence.items()]

    #tranforme une liste en pile
    heapq.heapify(heap)

    while len(heap) > 1:
        # retire le plus petit élement de la pile
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        parent = Noeud(None, left.frequency + right.frequency)

        parent.left = left
        parent.right = right

        # ajout du parent à la pile
        heapq.heappush(heap, parent)
    return heap[0]
    

# création d'une fonction qui crée une table de fréquence
def table_frequence(chaine: str):

    '''Création d'une table de fréquence
    Entree : les données à compresser
    Sortie : un dictionnaire de l'occurence des 
    caractères en fonction leur fréquence '''
    
    lst_chaine = []
    for caracteres in chaine:
        lst_chaine.append(caracteres)

    # utilisation de pandas pour créer une table 
    data = pd.Series(lst_chaine)
    temp =  data.value_counts(sort=True)
    df = pd.DataFrame({"Valeur": temp.index, 
                         "Fréquence": temp.values})
    df = df.sort_values(by="Fréquence", ascending=True)

    # transformation de la table en dictionnaire
    dictionnaire = df.set_index("Valeur")["Fréquence"].to_dict()

    return dictionnaire


# création d'une fonction qui donne les codes huffman 
# des élements de l'arbre construit au préalable
def codes(node: Noeud, prefix: str = "", code = None):

    '''Donne les codes binaires des éléments de 
    l'arbre de Huffman de façon récursive
    Entree : noeud (type: Noeud)
    Sortie : code binaire du noeud (type: str)'''

    # création d'un dictionnaire vide  
    if code is None:
        code = {}

    # ajout des caractères dans le dictionnaire
    if node is not None:
        if node.char is not None:
            code[node.char] = prefix

        # ajout récursif en parcourant l'arbre
        # on ajoute 0 quand on descend vers la gauche
        # on ajoute 1 quand on descend vers la droite
        codes(node.left, prefix + "0", code)
        codes(node.right, prefix + "1", code)
    return code

# création de la fonction principale
def compress_data(chaine: str):

    '''Compresse les données
    Entree : chaîne de caractères à compresser (str)
    Sortie : chaîne de caractères compressée (str)'''

    # création de la table de fréquence des données à compresser
    table = table_frequence(chaine)
    # création de l'arbre à partir de la table 
    tree = huffman_tree(table)
    # création du dictionnaire à parcourir pour compresser 
    donnees_compressees = codes(tree)
    # création de la chaîne à laquelle on ajoute les données encodées
    resultat = ""
    # parcours de la chaîne et ajout des données
    # encodées en fonction du caractère
    for caractere in chaine:
        resultat = resultat + donnees_compressees[caractere]
    return resultat, donnees_compressees


# création d'une fonction qui décode les données encodées 
def decompress_data(chaine_compressee, dico): 

    '''Décompression de 'une chaîne codée en Huffman.
    Entree : chaîne encodée (type: str), caractères associés à leur 
    code binaire (type: dict)
    Sortie : chaîne décodée (type:str)'''

    # création de la chaîne à renvoyer
    donnees_decodees = ''
    # parcours de la chaine compressée
    while len(chaine_compressee) > 0:
        # parcours des éléments du dictionnaire et 
        # ajout des caractères décodés à la chaine à renvoyer 
        for key in dico : 
            if chaine_compressee[0:len(dico[key])] == dico[key] : 
                donnees_decodees += key
                # retirer les caractères décodés de la chaîne compressée 
                chaine_compressee = chaine_compressee[len(dico[key]):]
    return donnees_decodees

