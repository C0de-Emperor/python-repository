############################################
################ les Tuples ################
############################################

"""
Les tuples (« n-uplets » en français) sont des objets séquentiels correspondant aux listes, 
    mais ils sont toutefois non modifiables. On dit aussi qu'ils sont immuables. 
Vous verrez ci-dessous que nous les avons déjà croisés à plusieurs reprises !

Pratiquement, on utilise les parenthèses au lieu des crochets pour les créer :
"""

tuple_ = (1, 2, 3)

print("1  : ", tuple_)       # Va retourner : (1, 2, 3)

print("2  : ", type(tuple_)) # Va retourner : <class 'tuple'>

"""
Pour accedéder aux éléments d'un tuple, c'est exactement comme les listes :

tuple_[2] 
>>> 3

Les tranches fonctionne tout aussi bien : 

tuple_[0:2]
>>> (1, 2)

Voici l'erreur retournée si l'on essai de modifier un tuple :

tuple_[2] = 15
>>> Traceback (most recent call last):
>>>   File "<stdin>", line 1, in <module>
>>> TypeError: 'tuple' object does not support item assignment
"""

"""
L'affectation et l'indiçage fonctionnent comme avec les listes. Mais si on essaie de modifier un des éléments du tuple (en ligne 10),
    Python renvoie un message d'erreur car les tuples sont non modifiables. 
Si vous voulez ajouter un élément (ou le modifier), 
    vous devez créer un nouveau tuple :
"""

tuple_ = (1, 2, 3)
tuple_ = tuple_ + (2,)

print("3  : ", tuple_)       # Va retourner : (1, 2, 3, 2)

"""
Conseils :

Cet exemple montre que les tuples sont peu adaptés lorsqu'on a besoin :
    d'ajouter, retirer, modifier des éléments. 
    
La création d'un nouveau tuple à chaque étape s'avère lourde
    et il n'y a aucune méthode pour faire cela puisque les tuples sont non modifiables. 

Pour ce genre de tâche, les listes sont clairement mieux adaptées.

Remarque :
⚠⚠⚠
Pour créer un tuple d'un seul élément comme ci-dessus, 
    utilisez une syntaxe avec une virgule (element,), 
    pour éviter une ambiguïté avec une simple expression. 
    
Par exemple, (2) équivaut à l'entier 2, alors que l'expression (2,) est un tuple contenant l'élément 2.

⚠ Attention 

Autre particularité des tuples, 
    il est possible de les créer sans les parenthèses, 
    dès lors que ceci ne pose pas d'ambiguïté avec une autre expression :

tuple_ = 1, 2, 3

print(tuple_)
>>> (1, 2, 3)
"""

# Les opérateurs + et * fonctionnent comme pour les listes (concaténation et duplication)

"""
Enfin, on peut utiliser la fonction tuple(sequence) qui fonctionne exactement comme la fonction list(), 
    c'est-à-dire qu'elle prend en argument un objet et renvoie le tuple correspondant (opération de casting) :
"""

                            # Va retourner : (1, 2, 3)
print("4  : ", tuple([1,2,3]))       

                            # Va retourner : ('A', 'T', 'G', 'C', 'C', 'G', 'C', 'G', 'A', 'T')
print("5  : ", tuple("ATGCCGCGAT")) 

                            # Va retourner : (0, 1, 2, 3, 4)
print("6  : ", tuple(range(5))) 

# Affectation multiple : 

x, y, z = 1, 2, 3

print("7  : ", x)           # Va retourner : 1
print("8  : ", y)           # Va retourner : 2
print("9  : ", z)           # Va retourner : 3

"""
⚠⚠ Attention, le nombre de variables et de valeurs doit être cohérents à gauche et à droite de l'opérateur = :

x, y = 1, 2, 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)

Il est aussi possible de faire des affectations multiples avec des listes, par exemple :

[x, y, z] = [1, 2, 3].

Toutefois, cette syntaxe est alourdie par la présence des crochets. 
On préfèrera donc la syntaxe avec les tuples sans parenthèses.
"""

"""
Remarque :
Nous avons appelé l'opération x, y, z = 1, 2, 3 
    affectation multiple pour signifier que l'on affectait des valeurs à plusieurs variables en même temps.

Vous pourrez rencontrer aussi l'expression tuple unpacking
    que l'on pourrait traduire par « désempaquetage de tuple ». 
De même, il existe le list unpacking.

Ce terme tuple unpacking provient du fait que l'on peut décomposer un tuple initial de 
    N éléments en autant de variables différentes en une seule instruction.
"""

tuple_ = (1, 2, 3)
x, y, z = tuple_

print("10 : ", x)           # Va retourner : 1
print("11 : ", y)           # Va retourner : 2
print("12 : ", z)           # Va retourner : 3

# Itérations sur plusieurs valeurs à la fois :

"""
Nous reverons la fonction enumerate() et les tuple dans le chapitre 6 Les Boucles For. 
Cette dernière permet d'itérer en même temps sur les indices et les éléments d'une liste :
"""

for indice, element in enumerate([75, -75, 0]):
    print(13 + indice, ": ", element)

"""
Va retourner :
0 75
1 -75
2 0
"""

for bidule in enumerate([75, -75, 0]):
    print("14 : ", bidule, type(bidule))

"""
Va retourner : 
(0, 75) <class 'tuple'>
(1, -75) <class 'tuple'>
(2, 0) <class 'tuple'>

Lignes 7 à 12. La fonction enumerate() itère sur une série de tuples. 
Pouvoir séparer indice et element dans la boucle est possible avec l'affectation multiple, 
    par exemple : indice, element = 0, 75 (voir rubrique précédente).
"""

# La fonction divmod()

"""
Dans le chapitre 2 Variables, 
    on a vu les opérateurs // et % qui renvoient respectivement le quotient et le reste d'une division entière. 
    
La fonction divmod() prend en argument deux valeurs, le numérateur et le dénominateur d'une division, 
    et renvoie le quotient et le reste de la division entière correspondante :
"""

print("14 : ", 3 / 4)       # Retourne 0.75
print("15 : ", 3 // 4)      # Retourne 0
print("16 : ", 3 % 4)       # Retourne 3

                            # Retourne (0, 3)
print("17 : ", divmod(3, 4))
