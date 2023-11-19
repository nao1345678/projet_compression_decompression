# Empaktor
## Sommaire
1. [Description Projet](#description)
    1. [Objectifs](#objectifs)
    2. [Programmes](#programmes)
        1. [RLE (Run-Length Encoding)](./empaktor/cmp_rle/rle.py)
        2. [BWT(Burrows-Wheeler)](./empaktor/cmp_burrows/burrows_wheeler.py)
        3. [Huffman](./empaktor/cmp_huffman/huffman.py)
        4. [Empaktor](./empaktor/empaktor.py)
    3. [Markdowns](#markdowns)  
        1. [RLE Markdown](./markdowns/rle.md)
        2. [BWT Markdown](./markdowns/burrows.md)
        3. [Huffman Markdown](./markdowns/huffman.md)
        4. [Empaktor Markdown](./empaktor/README_empaktor.md)

# Description
Dans cette activité, nous avons pour objectif de créer un programme Python appelé ```empaktor.py```.  
Empaktor est un outil de compression et de décompression de fichiers qui prend en charge différents algorithmes de compression tels que:
1. ```Huffman```
2. ```RLE (Run-Length Encoding)```
3. ```BWT (Burrows-Wheeler Transform)```

## Objectifs
1- Arriver à maitriser des algorithmes de compressions  
2- Documenter ses algorithmes  
3- Commenter son code afin de pouvoir le relire ou le faire reprendre
## Programmes

Pour réaliser le fichier de compression principale il nous faut tout d'abord réaliser les différents types de compressions.

Pour cela nous avons réalisé un fichier par algorithme de compression:

1. [RLE (Run-Length Encoding)](./empaktor/cmp_rle/rle.py)
2. [BWT(Burrows-Wheeler)](./empaktor/cmp_burrows/burrows_wheeler.py)
3. [Huffman](./empaktor/cmp_huffman/huffman.py)

Ces trois algorithmes seront appelés par le fichier principal [Empaktor](./empaktor/empaktor.py)

## Markdowns

Dans tous les exercices qui nous ont été donnés, il est imposé de créer en Markdown un fichier de documentation par algorithme/fonctionnalité.  
Pour cela nous avons donc créé un fichier de Markdown par algorithme pour faciliter une lecture de notre travail ainsi que de permettre une compréhension facile de nos algorithmes.

Retrouvez les fichiers de Markdown ci_dessous:

1. [RLE Markdown](./markdowns/rle.md)
2. [BWT Markdown](./markdowns/burrows.md)
3. [Huffman Markdown](./markdowns/huffman.md)
4. [Empaktor Markdown](./empaktor/README_empaktor.md)
