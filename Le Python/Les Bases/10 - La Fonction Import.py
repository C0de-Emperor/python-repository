############################################
############ La Fonction import ############
############################################

# Définition : 

"""
Les modules sont des programmes Python qui contiennent des fonctions que l'on est amené à souvent réutiliser
    (on les appelle aussi bibliothèques, ou libraries en anglais). 
Ce sont des « boîtes à outils » qui vous seront très utiles.

Les développeurs de Python ont mis au point de nombreux modules qui effectuent différentes tâches. 
Pour cette raison, 
    prenez toujours le réflexe de vérifier si une partie du code que vous souhaitez écrire n'existe pas déjà sous forme de module.

La plupart de ces modules sont déjà installés dans les versions standards de Python. 
Vous pouvez accéder à une documentation exhaustive sur le site de Python. 

N'hésitez pas à explorer un peu ce site, 
    la quantité de modules disponibles est impressionnante (plus de 300 modules).
"""

# Importation de modules :

"""
la notion de module est importante, notamment lorsque l'on veux tirer un nombre aléatoire :
"""

import random
    # Ici on accède au module random, puis par le "." on accède à la fonction randint() de ce module.
print("1  : ", random.randint(0, 10))

"""
Regardons de plus près cet exemple :

Ligne 1. L'instruction import donne accès à toutes les fonctions du module random.

Ligne 2. Nous utilisons la fonction randint(0, 10) du module random. 
Cette fonction renvoie un nombre entier tiré aléatoirement entre 0 inclus et 10 inclus.
"""

"""
Nous pouvons également croiser le module math .
Ce module nous donne accès aux fonctions trigonométriques sinus et cosinus, et à la constante pi :
"""

import math
    # Ici on accède au module math, puis par le "." on accède à la fonction cos() de ce module.
    # Cela va retourner : 6.123233995736766e-17 ce qui est "presque" 0
print("2  : ", math.cos(math.pi / 2))

"""
En résumé, 
    l'utilisation de la syntaxe import nomDuModule permet d'importer tout une série de fonctions organisées par « thèmes ».
Par exemple, les fonctions gérant les nombres aléatoires avec random et les fonctions mathématiques avec math. 
Python possède de nombreux autres modules internes (c'est-à-dire présent de base lorsqu'on installe Python).
"""

# Il existe un autre moyen d'importer une ou plusieurs fonctions d'un module :

from random import randint
print("3  : ", randint(0,10))

"""
À l'aide du mot-clé from, on peut importer une fonction spécifique d'un module donné. 
Remarquez bien qu'il est inutile de répéter le nom du module dans ce cas : seul le nom de la fonction en question est requis.
"""

# On peut également importer toutes les fonctions d'un module :

from random import *
print("4  : ", randint(0,50))

"""
L'instruction from random import * importe toutes les fonctions du module random. 
On peut utiliser toutes ses fonctions directement, 
    comme par exemple randint() et uniform() qui renvoient des nombres aléatoires entiers et floats.
"""

# Dans la pratique, plutôt que de charger toutes les fonctions d'un module en une seule fois :

from random import *

# Nous vous conseillons de charger le module seul de la manière suivante :

import random

# Enfin, pour vider de la mémoire un module déjà chargé, on peut utiliser l'instruction del :

del random

"""
⚠⚠⚠ ATTENTION ⚠⚠⚠

la methode :
from nomDuModule import *

Est dangereuse, en effet, 
    si vous aves defini dans votre script un fonction qui possède le même nom que l'une de celle contenu dans le module importé,
    (parfois plus de 200)
    alors vous allez avoir des résultat étranges sans forcément avoir une erreur, 
    votre script preferant utiliser la fonction du module plutôt que la votre.
"""

# Le mot clé "as" :

"""
Des fois, les modules ont des noms compliqués à écrire et ré-écrire, mais si on fait un import * on aurait des problèmes à cause des noms de fonctions
du module qui coinciderait avec des fonctions définies par l'utilisateur dans le programme.

Dans ce cas, on peut utiliser le mot clé "as" afin de "renommer" le module dans notre programme.
Exemple: (import du module tkinter)
"""

import tkinter     # A chaque fois qu'on a besoin d'une fonction tkinter il faut retaper le nom en complet, c'est long et il est fort probable qu'on fasse des erreurs

import tkinter as tk     # Maintenant je peut écrire tk.button() au lieu de tkinter.button()
