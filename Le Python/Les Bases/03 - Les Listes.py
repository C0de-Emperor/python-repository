############################################
################ les Listes ################
############################################

"""
Les listes (ou list / array ) en python sont une variable dans laquelle on peut mettre plusieurs objets.

pour definir une liste il y a plusieurs moyen :
"""

# definition directe :

liste = []                  # definit une liste vide, sans elements de longueur 0

liste = [1, 2, 3, 4, 5]     # definit une liste de Ints de longueur 5, elle contien : 1, 2, 3 ... 5

                            # definit une liste de Strings de longueur 5, elle contien :  "1", "a" ... "True"
liste = ["1", "a", "Mattéo", "Python", "True"]   

                            # Une liste peut contenir plusieurs types d'objets differents :
                            # même des listes, on peut donc avoirs des listes dans des listes dans des listes ... etc   
liste = [1, "a", [], "Python", True]

# definition par la fonction list() :

liste = list("abcdef")
print("1  : ", liste)       # va retourner : ['a', 'b', 'c', 'd', 'e', 'f'], moins pratique mais plus rapide

# Utilisation : 

"""
Un des gros avantages d'une liste est que vous accédez à ses éléments par leur position. Ce numéro est appelé indice (ou index) de la liste.

liste  : ["girafe", "tigre", "singe", "souris"]
indice :     0         1        2         3

⚠⚠ SOYEZ TRES ATTENTIFS au fait que les indices d'une liste de n éléments commencent à 
0 et se terminent à n-1 .
"""

    # Acceder à un element :
liste = [0, 1, 2, 3, 4, 5]
elementN0 = liste[0]        # nom_de_la_liste [indice de l'element]
print("2  : ", elementN0)   # retourne 0

    # En revanche liste [6] va retourner l'erreur : IndexError: list index out of range, car l'element n°6 n'existe pas

# Opération sur les listes

    # Tout comme les chaînes de caractères, les listes supportent l'opérateur + de concaténation, ainsi que l'opérateur * pour la duplication :

liste1 = ["girafe", "tigre"]
liste2 = ["singe", "souris"]

liste1 + liste2             # Retourne : ['girafe', 'tigre', 'singe', 'souris']

liste1 * 3                  # Retourne : ['girafe', 'tigre', 'girafe', 'tigre', 'girafe', 'tigre']

    # Ajouter un element a une liste : 

liste = []                  # Une liste vide

liste1 = liste + [15]       # Ou liste += [15] (concatenation)
print("3  : ", liste)       # retournera : [15] 
liste = liste + [-5]        # Ou liste += [-5] 
print("4  : ", liste)       #retournera : [15, -5]
liste= ["debut"] + liste    # On ajout "debut" au debut de la liste
print("5 : ", liste)

    # Puis avec la méthode .append() :  (methode meilleure d'un point de vue structure de données)

liste = []
liste.append(15)            # retournera : [15]   (ajoute l'element passé en argument A LA FIN de la liste)
print("6 :", liste)

    # La méthode .insert()

liste=[0,1,2]
liste.insert(1, "coucou")  # insere a l'indice passé en PREMIER argument l'element passé en SECOND argument (et décale les éléments suivants)
print("7 : ", liste)

"""
Indiçage négatif :
Une liste peut également être indexée avec des nombres négatifs selon le modèle suivant :

liste          : ["girafe", "tigre", "singe", "souris"]
indice positif :        0        1        2         3
indice négatif :       -4       -3       -2        -1

ou encore :

liste          : ["A", "B", "C", "D", "E", "F"]
indice positif :   0    1    2    3    4    5
indice négatif :  -6   -5   -4   -3   -2   -1

Les indices négatifs reviennent à compter à partir de la fin. 
Leur principal avantage est que vous pouvez accéder au dernier élément d'une liste à l'aide de l'indice -1
    sans pour autant connaître la longueur de cette liste. 
L'avant-dernier élément a lui l'indice -2, l'avant-avant dernier l'indice -3, etc.
"""

# Les Tranches :

"""
Un autre avantage des listes,
    est la possibilité de sélectionner une partie d'une liste en utilisant un indiçage construit sur le modèle :
        
        tranche = nomDeLaListe[ m : n+1 ]

        ici, on a récupéré tous les éléments du m-ième au n-ième (de l'élément m inclu à l'élément n+1 exclu) grace au ":"
    
    On dit alors qu'on récupère une tranche de la liste.
"""

                            # definitune liste de Ints de longueur 6, elle contien : 1, 2, 3 ... 5
listeDeNombres = [0, 1, 2, 3, 4, 5]

                            # Va retourner une nouvelle liste contenant des elements de listeDeNombres du 0-ème au 2-ème exclu donc [0, 1]
print("8  : ", listeDeNombres[0:2])  

                            # Va retourner une nouvelle liste contenant des elements de listeDeNombres du 0-ème au 3-ème exclu donc [0, 1, 2]
print("9  : ", listeDeNombres[0:3])  

                            # Va retourner une nouvelle liste contenant des elements de listeDeNombres du 3-ème jusqu'à la fin de la liste donc [3, 4, 5]
print("10  : ", listeDeNombres[3:]) 

    # Va retourner une nouvelle liste contenant des elements de listeDeNombres du début jusqu'à la fin de la liste donc [0, 1, 2, 3, 4, 5]
print("11  : ", listeDeNombres[:]) 

                            # Va retourner une nouvelle liste contenant des elements de listeDeNombres : [1, 2, 3, 4]
print("12  : ", listeDeNombres[1:-1]) 

"""
On peut aussi préciser le pas en ajoutant un symbole deux-points supplémentaire et en indiquant le pas par un entier
"""

                            # definitune liste de Ints de longueur 6, elle contien : 1, 2, 3 ... 5
listeDeNombres = [0, 1, 2, 3, 4, 5]

                            # Va retourner une nouvelle liste contenant des elements de listeDeNombres du 0-ème au 3-ème exclu de 2 en 2 donc [0, 2]
print("13 : ", listeDeNombres[0:3:2]) 

    # Va retourner une nouvelle liste contenant des elements de listeDeNombres du début jusqu'à la fin de la liste de 1 en 1 donc [0, 1, 2, 3, 4, 5]
print("14 : ", listeDeNombres[::1]) 

    # Va retourner une nouvelle liste contenant des elements de listeDeNombres du début jusqu'à la fin de la liste de 2 en 2 donc [0, 2, 4,]
print("15 : ", listeDeNombres[::2]) 

    # Va retourner une nouvelle liste contenant des elements de listeDeNombres du 1er au 6ème exclu de 3 en 3 donc [1, 4]
print("16 : ", listeDeNombres[1:6:3]) 

# La Fonction len() :

"""
L'instruction len() vous permet de connaître la longueur d'une liste, c'est-à-dire le nombre d'éléments que contient la liste.
"""

                            # definitune liste de Ints de longueur 6, elle contien : 1, 2, 3 ... 5
listeDeNombres = [0, 1, 2, 3, 4, 5]

                            # Va retourner 6
print("17 : ", len(listeDeNombres) )

# Les listes de listes :

"""
Sachez qu'il est tout à fait possible de construire des listes de listes. Cette fonctionnalité peut parfois être très pratique.
"""

prairie1 = ["girafe", 4]
prairie2 = ["tigre", 2]
prairie3 = ["singe", 5]
savane = [prairie1, prairie2, prairie3]
             
print("18 : ", savane)      # Va retourner [['girafe', 4], ['tigre', 2], ['singe', 5]]

print("19 : ", savane[0])   # Va retourner ['girafe', 4]

                            # Va retourner 'girafe'
print("20 : ", savane[0][0])

# Le minimum, maximum et somme d'une liste :

"""
Les fonctions min(), max() et sum() renvoient respectivement le minimum, le maximum et la somme d'une liste passée en argument :
"""

                            # definitune liste de Ints de longueur 6, elle contien : 1, 2, 3 ... 5
listeDeNombres = [0, 1, 2, 3, 4, 5]

                            # Va renvoyer la somme des termes de la liste : 1 + 2 + 3 + 4 + 5 = 15
print("21 : ", sum(listeDeNombres) )

                            # Va renvoyer le plus petit élément de la liste : 0
print("22 : ", min(listeDeNombres) )

                            # Va renvoyer le plus grand élément de la liste : 5
print("23 : ", max(listeDeNombres) )

"""
Même si en théorie ces fonctions peuvent prendre en argument une liste de strings, 
    on les utilisera la plupart du temps avec des types numériques (liste d'entiers et / ou de floats).
"""

x = int( 1 )
y = int( 2 )
z = int( 3 )

    # on peut aussi utiliser la fonction max et min comme ceci :
print("24 : ", max(x, y, z) )

"""
⚠ Attention toutefois à ne pas mélanger entiers et floats d'une part avec une liste d'autre part, car cela renvoie une erreur.
"""

# Problème avec les copies de listes :

"""
⚠⚠⚠ TRES IMPORTANT
J'attire votre attention sur un comportement de Python qui peut paraitre étrange lorsqu'on copie une liste :
"""

liste1 = [0, 1, 2, 3, 4]

liste2 = liste1

print("25 : ", liste2 )     # Va renvoyer la liste2 donc la liste1 car elles sont égales : [0, 1, 2, 3, 4]

    # Mantenant ajoutons un élément à la liste2
liste2.append( 5 )

print("26 : ", liste2 )     # Va renvoyer : [0, 1, 2, 3, 4, 5]

"""
Jusque ici, tout va bien

Mais regardez ce qu'il se passe si j'affiche ce que vaut la lste1
"""

print("27 : ", liste1 )

"""
Va renvoyer : [0, 1, 2, 3, 4, 5]

Alors qu'on a jamais ajouté 5 a la liste1

Voici le problème :
    liste2 = liste1
cette operation met en relation les deux listes, tout ce qui arrive à l'une arrive aussi à l'autre

pour eviter cela, on utilise la fonction .copy()
"""

liste1 = [0, 1, 2, 3, 4]

liste2 = liste1.copy()      # On dis que la liste2 deviens une liste à part entière qui possède les mêmes elements que la liste1

print("28 : ", liste2 )     # Va renvoyer la liste2 : [0, 1, 2, 3, 4]

    # Mantenant ajoutons un élément à la liste2
liste2.append( 5 )

print("29 : ", liste2 )     # Va renvoyer : [0, 1, 2, 3, 4, 5]

print("30 : ", liste1 )     # Va renvoyer : [0, 1, 2, 3, 4]
