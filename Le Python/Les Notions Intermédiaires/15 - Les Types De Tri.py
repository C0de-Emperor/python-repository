"""
En programmation on peut se retrouver confrontés à une situation où il nous est nécessaire de trier (par ordre croissant) les éléments d'une liste.
Nous allons voir les 3 types de tri les plus utilisés, à savoir le tri par insertion, le tri par sélection et le tri par bulles.
Cependant, il arrive d'avoir des liste ne contenant pas QUE des nombres à trier, nous verrons donc à la fin comment élargir les possibilités de tri.

Pour commencer, il est recommandé d'utiliser la fonction par défaut de python, sorted, dû à son coût machine des plus optimisés.

"""

listeATrier = [0, 89 , -7 , 18 , 52 , 3]
listeTriee = sorted(listeATrier)   # La méthode sorted() va retourner la liste qui lui est passée en argument triée par ordre croissant
print("1: ", listeTriee)     


listeATrier = [0, 89 , -7 , 18 , 52 , 3]
listeTriee = sorted(listeATrier, reverse=True)   # L'argument reverse détermine l'ordre de tri. Il est par défaut égal à False (=croissant), en le passant à True l'ordre devient décroissant
print("2: ", listeTriee)   


"""
            TRI PAR INSERTION

Principe général:

On considère notre liste à trier 'séparée' en deux parties, une triée et une non triée.
Par défaut, la liste triée correspond au premier élément, on a donc :

[0 , 89 , -7 , 18 , 52 , 3]
trié|         pas trié

Pour chaque élément non trié en partant de la gauche, on va le stocker puis décaler vers la droite l'élément le précédent tant que ce dernier n'est pas plus petit que celui sélectionné (ou qu'on atteigne le début de la liste).
Enfin, on placera l'élément sélectionné là où on s'arrete.
Ainsi on aura:

[0 , 89 , -7 , 18 , 52 , 3]     etat initial
trié|        pas trié


On sélectionne 89.

On pointe à l'indice 0.
0<89 donc on s'arrete la. On a donc:
[0 , 89 , -7 , 18 , 52 , 3]
trié   |       pas trié


On sélectionne -7.

On pointe à l'indice 1.
89>-7 donc on le décale. On a donc:
[0 , 89 , 89 , 18 , 52 , 3]

On pointe à l'indice 0.
0>-7 donc on le décale. On a donc:
[0 , 0 , 89 , 18 , 52 , 3]

On est arrivés à la fin de la liste donc on s'arrete la. On a donc:
[-7 , 0 , 89 , 18 , 52 , 3]
    trié     |  pas trié


On sélectionne 18.

On pointe à l'indice 2.
89>18 donc on le décale. On a donc:
[-7 , 0 , 89 , 89 , 52 , 3]

On pointe à l'indice 1.
0<18 donc on s'arrete la. On a donc:
[-7 , 0 , 18 , 89 , 52 , 3]
      trié        |pas trié


Et on continue ainsi jusqu'atteindre la fin de la liste.

En code, ça donne ceci:
"""

liste=[0, 89 , -7 , 18 , 52 , 3]

for k in range(1, len(liste)):                         # on boucle dans la liste (et commence à 1!)
    i=k                                                # i sera la variable déterminant l'indice actuel de où insérer l'élément sélectionné
    elementSelectionne=liste[k]                        # on stocke la valeur de l'élément sélectionné
    while i!=0 and elementSelectionne < liste[i-1]:    # littéralement: TANT QU'on est pas au début de la liste ET que l'élément sélectionné plus petit que l'élément à l'indice i-1
        liste[i] = liste[i-1]                          # on décale l'élément d'indice i-1
        i-=1                                           # on décrémente i
    liste[i]=elementSelectionne                        # on place à i l'élément sélectionné

print("3: ", liste)

"""
Il suffit d'inverser le sens du comparateur pour inverser le sens de tri.

!!!!!!! Dans la condition du WHILE, il faut ECRIRE LE i!=0 EN PREMIER
En effet, sinon, on cherche un indice négatif qui n'existera pas (en python si mais on ne le veut pas)
Par principe de fainéantise, si la première des deux clauses d'un AND est fausse, python ne lira pas la deuxième, évitant ainsi de potentielles erreurs d'indice.
"""



"""
            TRI PAR SELECTION

Principe général:

On considère notre liste à trier 'séparée' en deux parties, une triée et une non triée.
Par défaut, la liste triée est vide, on a donc :

[0 , 89 , -7 , 18 , 52 , 3]
|         pas trié

Tant que la liste non triée n'est pas vide, on va chercher son élément le plus petit puis l'échanger avec le 1er élément de la liste non triée.
Ainsi, on aura:

[0 , 89 , -7 , 18 , 52 , 3]    état initial
|         pas trié


1er tour de liste:
on trouve que -7 est le minimum, on a donc:
[-7 , 89, 0 , 18 , 52 , 3]
trié|       pas trié


2e tour de liste:
on trouve que 0 est le minimum, on a donc:
[-7 , 0 , 89 , 18 , 52 , 3]
  trié  |     pas trié


3e tour de liste:
on trouve que 3 est le minimum, on a donc:
[-7 , 0 , 3 , 18 , 52 , 89]
     trié   |     pas trié

Et on continue jusqu'à la fin de la liste.

En code, on a ça:
"""

liste=[0, 89 , -7 , 18 , 52 , 3]

for k in range(len(liste)):                           # on boucle dans la liste
    indiceDuMinimum=k                                 # on initialise l'indice du minimum comme étant celui du 1er élément de la liste non triée
    for n in range(indiceDuMinimum, len(liste)):      # on parcourt la liste non triée
        if liste[n] < liste[indiceDuMinimum]:         # on compare la valeur du minimum actuellement trouvé et de l'élément à l'indice n
            indiceDuMinimum=n                         # on remplace la valeur de l'indice du minimum
    
    liste[indiceDuMinimum], liste[k] = liste[k], liste[indiceDuMinimum]  # on permute le minimum et le premier élément de la liste non triée


print("4:", liste)


"""
            TRI PAR BULLES

Principe général:

On compare les deux premiers éléments: si le 1er élément est plus grand que le deuxième, on les inverse. Sinon, on compare le 2e et 3e élément.
Chaque fois qu'on en invertit deux, on recommence depuis LE DEBUT. (C'est pourquoi cet algorithme de tri est terriblement inefficace)
Ainsi, on a:

[0 , 89 , -7 , 18 , 52 , 3]

On pointe à l'indice 0.
0<89 donc tout va bien.

On pointe à l'indice 1.
89>-7 donc on les intervertit. On a donc:
[0 , -7 , 89 , 18 , 52 , 3]

On pointe à l'indice 0.
0>-7 donc on les intervertit. On a donc:
[-7 , 0 , 89 , 18 , 52 , 3]

On pointe à l'indice 0.
-7<0 donc tout va bien.

On pointe à l'indice 1.
0<89 donc tout va bien.

On pointe à l'indice 2.
89>18 donc on les intervertit. On a donc:
[-7 , 0 , 18 , 89 , 52 , 3]

On pointe à l'indice 1.  ((❁´◡`❁))
......

Et on continue jusqu'on n'ait aucune interversion dans un tour de boucle.

En code, ça donne:
"""

liste=[0 , 89 , -7 , 18 , 52 , 3]

i=0                                                     # on initialise notre variable pointeur
intervertit=True                                        # intervertit sera True si il y a eu interversion et False sinon
while intervertit==True:                                # littéralement: TANT QU'il y a eu interversion
    intervertit=False                                   # on part du principe qu'il n'y aura pas d'interversion
    while i<len(liste)-1 and intervertit==False:        # littéralement: TANT QU'on n'est pas arrivés à la fin de la liste ET qu'il n'y a pas eu d'interversion
        if liste[i]>liste[i+1]:                         # si l'élément pointé par i est plus grand que le suivant
            liste[i],liste[i+1] = liste[i+1],liste[i]   # on inverse les éléments d'indices i et i+1
            intervertit=True                            # il y a eu interversion
            i=-1                                        # on repart du début (!!!! i=-1 car la ligne i+=1 suivante sera lue après la fin du if)
        i+=1                                            # on incrémente i de 1

print("5:", liste)



#-By Mimile
