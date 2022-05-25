# Exercice Python

Le but de l'exercice est de compter le nombre d'occurrences de chaque mot dans un texte.

### Exemple:

```
input :
hello hello world

output :
[('hello', 2), ('world', 1)]
```

## Installation, tests et construction

```bash
docker build -t <image_name> .
```
Dans le Dockerfile je lance l'installation des dépendances, les tests unitaires et à la fin je crée une image de conteneur avec mon whl installé dedans

## Exécution

```bash
docker run -it <image_name> "Bonjour je m'appelle Franck"
```
En sorti vous devriez avoir :
```
[('bonjour', 1), ('je', 1), ('m', 1), ('appelle', 1), ('franck', 1)]
```

Dans mon code, j'ai pensé à remplacer la ponctuation et autres caractères spéciaux pour bien séparer les mots et à supprimer les majuscules pour pas avoir des mots similaires non comptabilisés.
