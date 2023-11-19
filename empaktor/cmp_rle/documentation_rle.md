# Algorithme d'Encodage RLE (Run-Length Encoding)

## Prototype

### Encodage

```python
def encode_rle(data: str) -> str:
```
cette function permet d'encoder 'data' qui est en paramètre de type string et cette function renvoi un string après encodage. Data correspond a l'information qui sera encodée.
#### Sortie
```python
data: AAABBBCCD4!
encoded_data: 3⁞Aᶦ3⁞Bᶦ2⁞Cᶦ1⁞Dᶦ1⁞4ᶦ1⁞!ᶦ
```
L'algorithme RLE (Run-Length Encoding) est une technique de compression de données qui consiste à représenter les données répétitives par une seule occurrence suivie du nombre de répétitions. Dans notre cas les repetitions et les données sont séparé par des symbole afin d'aider au décodage.
encoded_data est de type string

### Décodage

```python
def decode_rle(encoded_data: str) -> str:
```
cette fonction permet de décoder la data encodée dans la function precedente en RLE cette fonction prend en parametre encoded_data de type string et cette fonction est elle même de type string.
#### Sortie
```python
data: AAABBBCCD4!
encoded_data: 3⁞Aᶦ3⁞Bᶦ2⁞Cᶦ1⁞Dᶦ1⁞4ᶦ1⁞!ᶦ
decoded_data: AAABBBCCD4!
```
pour effectuer cette décompression on utilise les caracteres spéciaux afin de différencier le nombre d'occurences des valeurs il suffit donc de lire la valeur avant "⁞" pour connaitre les occurences puis de prendre la valeure apres "⁞" afin de les multiplier ensemble.
Le decoded_data est donc de type string comme le data d'origine.
