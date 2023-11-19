# algorithme de transformation BWT(Burrows-Wheeler)

## Prototype

### ```Transformation```
```python
def transform_bwt(data: str)->str:
```
cette function permet de transformer 'data' qui est en paramètre de type string et cette function renvoi un string après transformation. Data correspond a l'information qui sera modifiée.

#### sortie :
```python
data : 'hello'
transformed_data: 'hoell'
```
À partir de la chaîne d'origine, on génère une liste de rotations circulaires de cette chaîne.

Par exemple, si la chaîne d'origine est "hello", les rotations circulaires seraient :
```python
'
ohell
lohel
llohe
elloh
hello
'
```
Ensuite, on trie ces rotations dans l'ordre de l'alphabet pour obtenir une nouvelle liste de chaînes.

Pour notre exemple, après le tri, la liste ressemblera à ceci :
```python
'
elloh
hello
llohe
lohel
ohell
'
```
 La dernière colonne de la liste triée est extraite. Cette colonne contient les derniers caractères de chaque rotation.

Pour notre exemple la derniere colone est:
```python
'
h
o
e
l
l
'
donc: 'hoell' une fois alligné.
```
"hoell" sera donc l'une des sorties de notre fonction,sous la forme de "transformed_data" qui est de type string. Cette fonction renvoi aussi une autre information en sortie c'est la clef qui n'est pas affiché en sortie mais sera utilisé dans l'inversion. "key" est de type integer.

### ```Inversion```
```python
def inverse_bwt(transformed_data:str, key:int)->str:
```
cette fonction permet d'inverser la transformation effectuée dans la function precedente. cette fonction prend en parametre transformed_data de type string ansi que key de type integer. cette fonction est elle même de type string.
#### sortie :
```python
data: 'hello'
transformed_data: 'hoell'
inversed_data: 'hello'
```
On prend la sortie transformed_data qu'on va mettre dans une liste dans laquelle il y aura donc les caractère ainsi que leur index

pour notre exemple la liste sera comme ça:

```python
[('h', 0), ('o', 1), ('e', 2), ('l', 3), ('l', 4)]
```
ensuite on trie cette liste alphabetiquement elle prendra donc cette forme :
```python
[('e', 2), ('h', 0), ('l', 3), ('l', 4), ('o', 1)]
```
ensuit on reforme le mot d'origine avec la liste des caractères et leurs indexs respectifs, l'ordre des index est donné par la clef "key" réalisé dans la transformation voici la demonstration pour notre exemple :
```python
['h', '', '', '', '']
1
['h', 'e', '', '', '']
0
['h', 'e', 'l', '', '']
2
['h', 'e', 'l', 'l', '']
3
['h', 'e', 'l', 'l', 'o']
4
```
et pour finir cette fonction on ".join" les listes du tableau afin de faire qu'une chaine de caractère qui sera donc ```hello``` inséré dans inversed_data de type string.