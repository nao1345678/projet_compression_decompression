def encode_rle(data: str) -> str :
    encoded_data: str = ""
    i: int = 0
    while i < len(data):
        count: int = 1

        # Boucle tant que la data ne change pas
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        # On rajoute des délimiteurs afin de pouvoir distinguer
        # les data des occurences
        encoded_data += f"{str(count)}⁞{data[i]}ᶦ"
        i += 1
    return encoded_data


def decode_rle(encoded_data: str) -> str:
    num:int = ""
    decoded_data:str = ""
    for i in range(len(encoded_data) - 1):
        # Vérifie si le caractère suivant n'est pas un délimiteur
        # et ajoute les valeurs
        char:str = encoded_data[i + 1]
        if encoded_data[i].isdigit() and char != "ᶦ":
            num += encoded_data[i]
        elif encoded_data[i] == '⁞':
            decoded_data += int(num) * char
            num = ""
    return decoded_data
