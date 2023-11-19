def transform_bwt(data: str)->str:
    a:str = data
    # on fait une liste de chaque caractère de data
    words:list = list(a)
    # creation d'un tableau afin de stoquer chaque étapes 
    result:str = []
    # ititialization des deux sorties
    transformed_data: str = ""
    key:int =''
    # boucle du burrows-wheeler qui bouge les lettres
    # a chaque tour de boucle 
    for i in range(len(words)):
        word:str = a[-1] + a[:-1]
        new:str = ''.join(word)
        a = new
        result.append(new)
        i += 1
    # sorted trie alphabetiquement result
    sort:list = sorted(result)
    for i in range(len(words)):
        # creation de la clef afin de détranformer en prenant
        # l'index de la première occurence
        key = sort.index(data)
        element = sort[i]
        last = element[- 1]
        i = i + 1
        transformed_data += last
    return transformed_data,key


def inverse_bwt(transformed_data:str, key:int)->str:
    # Crée une liste avec les caractère et leurs index respectifs
    chars_i = [(char, index) for index, char in enumerate(transformed_data)]
    # Trie la liste
    sorted_chars = sorted(chars_i)
    # creation du tableau afin de retrouver la sequence originale
    inversed_data = [''] * len(transformed_data)
    # met les indices dans le tableau
    for i in range(len(transformed_data)):
        inversed_data[i] = sorted_chars[key][0]
        key = sorted_chars[key][1]
    # rejoin les caractères a la fin
    return ''.join(inversed_data)
