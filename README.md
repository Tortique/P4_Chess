# P4_Chess

Ce projet permet de créer et gérer des tournois d'échecs.
</br> Il permet aussi de générer des rapports par tournoi, round et match ainsi que la liste des joueurs inscrits.

## Installation

Utilisez pip pour installer tinydb pour le stockage de données :

```bash
pip install tinydb
```

## Usage

Lancez le projet avec :

```python
python3 main.py
```

## Génération de rapports flake8:

Si besoin, vous pouvez installer flake8 : 

```bash
pip install flake8
pip install flake8-html
```

Et créer un rapport html avec flake8-html :


```bash
flake8 --format=html --htmldir=flake-report
```
