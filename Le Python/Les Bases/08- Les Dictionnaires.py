############################################
############# les Dictionnaires ############
############################################

# Définition et fonctionnement :

"""
Un dictionnaire contient une collection d'objets Python auxquels on accède à l'aide d'une clé de correspondance plutôt qu'un indice. 
Ainsi, il ne s'agit pas d'objets séquentiels comme les listes, 
    mais plutôt d'objets dits de correspondance (mapping objects en anglais) ou tableaux associatifs.
"""

# Ceci étant défini, comment fonctionnent-ils exactement ? Regardons un exemple :

ville = {}                  # On defini un dictionnaire vide

    # On remplit le dictionnaire avec plusieurs clés ("nom", "population", "superficie") auxquelles on affecte des valeurs ("valence", 64483, 36.7).
ville["nom"] = "lyon"   
ville["population"] = 1702921
ville["superficie"] = 47.87

                            # Retourne : {'nom': 'lyon', 'population': 1702921, 'superficie': 47.87}
print("3  : ", ville)

"""
Une fois le dictionnaire créé, on récupère la valeur associée à une clé donnée avec une syntaxe du type dictionnaire["clé"].
"""

                            # Retourne : 'lyon'
print("4  : ", ville["nom"])

# On peut aussi initialiser toutes les clés et les valeurs d'un dictionnaire en une seule opération :

ville = {"nom": "valence", "population": 64483, "superficie": 36.7}

# Mais rien ne nous empêche d'ajouter une clé et une valeur supplémentaire :

ville["nombreDeDidierBarcelo"] = 1
print("5  : ", ville)       # Retourne : {'nom': 'valence', 'population': 64483, 'superficie': 36.7, 'nombreDeDidierBarcelo': 1}

"""
Les humains retiennent mieux les noms que les chiffres. 

Ainsi, les dictionnaires se révèlent très pratiques lorsque vous devez manipuler des structures complexes à décrire
    et que les listes présentent leurs limites. 
L'usage des dictionnaires rend en général le code plus lisible. Par exemple, si nous souhaitions stocker les coordonnées (x, y, z)
    d'un point dans l'espace, nous pourrions utiliser coors = [0, 1, 2] pour la version liste
    et coors = {"x": 0, "y": 1, "z": 2} pour la version dictionnaire. 
    
Quelqu'un qui lit le code comprendra tout de suite que coors["z"] contient la coordonnée z, ce sera moins intuitif avec coors[2].
"""

# La Fonction len()

"""
Comme pour les listes, 
    l'instruction len() renvoie la longueur du dictionnaire, 
    sauf qu'ici il s'agit du nombre de couples clé / valeur. 
    
Voici un exemple d'utilisation :
"""

ville = {"nom": "reykjavik", "population": 139875, "superficie": 274.5}
                            # Retournera : 3
print("6  : ", len( ville ) )

# Itération sur les clés pour obtenir les valeurs : 

"""
Si on souhaite voir toutes les associations clés / valeurs, on peut itérer sur un dictionnaire de la manière suivante :
"""

ville = {"nom": "reykjavik", "population": 139875, "superficie": 274.5}
for key in ville:
    print("7  : ", key, ":", ville[key])

"""
retournera :

nom : reykjavik
population : 139875
superficie : 274.5
"""

# Les méthodes .keys() et .values() :

"""
Les méthodes .keys() et .values() renvoient, comme vous vous en doutez, les clés et les valeurs d'un dictionnaire :
"""
ville = {"nom": "reykjavik", "population": 139875, "superficie": 274.5}

                            # Retourne : dict_keys(['poids', 'nom', 'taille'])
print("8  : ", ville.keys())
                            # Retourne : dict_values([70, 'singe', 1.75])
print("9  : ", ville.values())

"""
Les mentions dict_keys et dict_values indiquent que nous avons à faire à des objets un peu particuliers. 
Ils ne sont pas indexables (on ne peut pas retrouver un élément par indice, par exemple dico.keys()[0] renverra une erreur). 
Si besoin, nous pouvons les transformer en liste avec la fonction list() :
"""

ville = {"nom": "reykjavik", "population": 139875, "superficie": 274.5}

                            # Renvoi : ['reykjavik', 139875, 274.5]
print("10 : ", list(ville.values()))

"""
Toutefois, on peut itérer dessus dans une boucle for (on dit qu'ils sont itérables) :

for cle in animal2.keys():
    print(cle)

Retourne :

nom
poids
taille
"""

# La méthode .items() :

"""
La méthode .items() renvoie un nouvel objet dict_items :

dico = {0: "t", 1: "o", 2: "t", 3: "o"}
dico.items()

Renvoi :

dict_items([(0, 't'), (1, 'o'), (2, 't'), (3, 'o')])

On ne peut pas retrouver un élément par son indice dans un objet dict_items, toutefois on peut itérer dessus :

for key, val in dico.items():
    print(key, val)

Retourne :

0 t
1 o
2 t
3 o

Notez la syntaxe particulière qui ressemble à la fonction enumerate() vue au chapitre 5 Boucles et comparaisons. 
On itère à la fois sur key et sur val. 
Nous aurons l'explication de ce mécanisme dans la rubrique sur les tuples ci-après.
"""

# Existence d'une clé ou d'une valeur :

"""
Pour vérifier si une clé existe dans un dictionnaire, 
    on peut utiliser le test d'appartenance avec l'opérateur in qui renvoie un booléen :
"""

animal = {'nom': 'singe', 'poids': 70, 'taille': 1.75}
                            # Renvoie True, car "poids" est bien une clé dans le dictionnaire
print("11 : ", "poids" in animal)

"""
Si on souhaite tester si une valeur existe dans un dictionnaire,
    on peut utiliser l'opérateur in avec l'objet renvoyé par la méthode .values() :
"""

animal = {'nom': 'singe', 'poids': 70, 'taille': 1.75}
                            # Renvoie True, car "singe" est bien une valeur dans le dictionnaire
print("12 : ", "singe" in animal.values())

# La méthode .get() : 

"""
Par défaut, si on demande la valeur associée à une clé qui n'existe pas, Python renvoie une erreur :

animal2 = {'nom': 'singe', 'poids': 70, 'taille': 1.75}
print(animal2["age"])

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'age'

La méthode .get() s'affranchit de ce problème. 
Elle extrait la valeur associée à une clé mais ne renvoie pas d'erreur si la clé n'existe pas :
"""

print("13 : ", animal.get("age"))

"""
On peut également indiquer à .get() une valeur par défaut si la clé n'existe pas :
"""

print("14 : ", animal.get("age", 42))

# Les liste de dictionnaires :

"""
En créant une liste de dictionnaires qui possèdent les mêmes clés, on obtient une structure qui ressemble à une base de données :
"""

animal1 = {'nom': 'girafe', 'taille': 5.0, 'poids': 1100}
animal2 = {'nom': 'singe', 'taille': 1.75, 'poids': 70 }

animaux = [animal1, animal2]

    # Retourne : [{'nom': 'girafe', 'poids': 1100, 'taille': 5.0}, {'nom': 'singe','poids': 70, 'taille': 1.75}]
print("15 : ", animaux)

for animal in animaux:
                            # Retourne : girafe singe
    print("15 : ", animal["nom"])

"""
Vous constatez ainsi que les dictionnaires permettent de gérer des structures complexes de manière plus explicite que les listes.
"""
