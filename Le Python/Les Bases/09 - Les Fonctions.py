############################################
############## les Fonctions ###############
############################################

# Principe et généralités :

"""
En programmation, les fonctions sont très utiles pour réaliser plusieurs fois la même opération au sein d'un programme. 
Elles rendent également le code plus lisible et plus clair en le fractionnant en blocs logiques.

Vous connaissez déjà certaines fonctions Python. 
Par exemple math.cos(angle) du module math renvoie le cosinus de la variable angle exprimé en radian. 
Vous connaissez aussi des fonctions internes à Python comme range() ou len(). 
Pour l'instant, une fonction est à vos yeux une sorte de « boîte noire » :

1 - À laquelle vous passez aucune, une ou plusieurs variable(s) entre parenthèses. 
    Ces variables sont appelées arguments. 
    Il peut s'agir de n'importe quel type d'objet Python.

2 - Qui effectue une action.

3 - Qui renvoie un objet Python ou rien du tout.
"""

"""
Par exemple, si vous appelez la fonction len() de la manière suivante :
len([0, 1, 2])
>>> 3

voici ce qu'il se passe :

1 - vous appelez len() en lui passant une liste en argument (ici la liste [0, 1, 2]) ;
2 - la fonction calcule la longueur de cette liste ;
3 - elle vous renvoie un entier égal à cette longueur.
"""

"""
Aux yeux du developpeur, 
    une fonction est une portion de code effectuant une suite d'instructions bien particulière. 
Mais avant de vous présenter la syntaxe et la manière de construire une fonction, 
    revenons une dernière fois sur cette notion de « boîte noire » :

Une fonction effectue une tâche. Pour cela, elle reçoit éventuellement des arguments et renvoie éventuellement quelque chose. 
L'algorithme utilisé au sein de la fonction n'intéresse pas directement l'utilisateur. 
Par exemple, il est inutile de savoir comment la fonction math.cos() calcule un cosinus. 
On a juste besoin de savoir qu'il faut lui passer en argument un angle en radian, 
    et qu'elle renvoie le cosinus de cet angle. Ce qui se passe à l'intérieur de la fonction ne regarde que le developpeur.

Chaque fonction effectue en général une tâche unique et précise. 
Si cela se complique, il est plus judicieux d'écrire plusieurs fonctions (qui peuvent éventuellement s'appeler les unes les autres). 
Cette modularité améliore la qualité générale et la lisibilité du code. 
Vous verrez qu'en Python, les fonctions présentent une grande flexibilité.
"""

# Définition :

"""
Pour définir une fonction, Python utilise le mot-clé "def". 
Si on souhaite que la fonction renvoie quelque chose, il faut utiliser le mot-clé "return". 

Par exemple :
"""

def carre(x):
    return x**2

print("1  : ", carre(2) )

"""
Notez que la syntaxe de def utilise les deux-points comme les boucles for et while ainsi que les tests if : 
    un bloc d'instructions est donc attendu. 

De même que pour les boucles et les tests, 
    l'indentation de ce bloc d'instructions (qu'on appelle le corps de la fonction) est obligatoire.

Dans l'exemple précédent, 
    nous avons passé un argument à la fonction carre(), 
    qui nous a retourné une valeur que nous avons immédiatement affichée à l'écran avec l'instruction print(). 
    
Que veut dire valeur renvoyée ? Et bien cela signifie que cette dernière est récupérable dans une variable :
"""

resultat = carre(3)
print("2  : ", resultat )

"""
Ici, le résultat renvoyé par la fonction est stocké dans la variable resultat. 
Notez qu'une fonction ne prend pas forcément un argument et ne renvoie pas forcément une valeur, 
    par exemple :
"""

def hello():
    print("3  : ", "bonjour")

hello()

# Passage d'arguments

"""
Le nombre d'arguments que l'on peut passer à une fonction est variable. 
Nous avons vu ci-dessus des fonctions auxquelles on passait zero ou un argument. 
Dans les chapitres précédents, 
    vous avez rencontré des fonctions internes à Python qui prenaient au moins deux arguments. 
Souvenez-vous par exemple de range(1, 10) ou encore range(1, 10, 2). 
Le nombre d'arguments est donc laissé libre à l'initiative du programmeur qui développe une nouvelle fonction.
"""

"""
Une particularité des fonctions en Python est que vous n'êtes pas obligé de préciser le type des arguments, 
    dès lors que les opérations que vous effectuez avec ces arguments sont valides. 
Python est en effet connu comme étant un langage au « typage dynamique », 
    c'est-à-dire qu'il reconnaît pour vous le type des variables au moment de l'exécution. Par exemple :
"""

def fois(x, y):             # Cette fonction prend 2 arguments
    return x*y              # Cette fonction retourne le produit des deux parametres

print("4  : ", fois(2, 3))  # Ici une simple multiplication d'entiers

                            # Ici une multiplication d'un entier et d'une chaine de caractères
print("5  : ", fois("to", 2))

                            # Ici une multiplication d'un entier et d'une liste
print("6  : ", fois([1,3], 2))

# Renvoi de résultats

"""
Un énorme avantage en Python est que les fonctions sont capables de renvoyer plusieurs objets à la fois, 
    comme dans cette fraction de code :
"""

def carre_cube(x):
        # On pourrait aussi l'écrire : return (x**2, x**3) c'est donc l'autre manière d'écrire les tuples.
    return x**2, x**3       

                            # Ici on remarque que cela va retourner (4, 8) c'est bien un tuple.
print("7  : ", carre_cube(2))

"""
En réalité Python ne renvoie qu'un seul objet, mais celui-ci peut être séquentiel, 
    c'est-à-dire contenir lui-même d'autres objets. 
    
Dans notre exemple, 
    Python renvoie un objet de type tuple, 
    type que nous avons vu dans le chapitre 8 Dictionnaires et tuples 
    (souvenez-vous, il s'agit d'une sorte de liste avec des propriétés différentes). 
    
Notre fonction pourrait tout autant renvoyer une liste :
"""

def carre_cube2(x):
    return [x**2, x**3]

                            # Ici on remarque que cela va retourner [9, 27] c'est bien une liste.
print("8  : ", carre_cube2(3))

"""
Renvoyer un tuple ou une liste de deux éléments (ou plus) 
    est très pratique en conjonction avec l'affectation multiple, 
    par exemple :
"""

z1, z2 = carre_cube2(3)

print("9  : ", z1)          # Va retourner : 9
print("10 : ", z2)          # Va retourner : 27

# Une fonction peut renvoyer tout type de variable

# Arguments positionnels et arguments par mot-clé

"""
Lorsqu'on définit une fonction def fct(x, y): 
    les arguments x et y sont appelés arguments positionnels (en anglais, positional arguments). 
    
Il est strictement obligatoire de les préciser lors de l'appel de la fonction. 

De plus, il est nécessaire de respecter le même ordre lors de l'appel que dans la définition de la fonction. 

Dans l'exemple ci-dessus, 2 correspondra à x et 3 correspondra à y. 
Finalement, tout dépendra de leur position, d'où leur qualification de positionnel.
"""
"""
Mais il est aussi possible de passer un ou plusieurs argument(s) de manière facultative
    et de leur attribuer une valeur par défaut :
"""

def fct(x=1):
    return x

print("11 : ", fct())       # Va retourner : 1
print("12 : ", fct(10))     # Va retourner : 10

"""
Un argument défini avec une syntaxe def fct(arg=val): 
    est appelé argument par mot-clé (en anglais, keyword argument). 
    
Le passage d'un tel argument lors de l'appel de la fonction est facultatif. 
Ce type d'argument ne doit pas être confondu avec les arguments positionnels présentés ci-dessus, 
    dont la syntaxe est def fct(arg):
"""

def fct(x=0, y=0, z=0):
    return x, y, z

print("13 : ", fct())       # Va retourner : (0, 0, 0)
print("14 : ", fct(10))     # Va retourner : (10, 0, 0)
print("15 : ", fct(10, 8))  # Va retourner : (10, 8, 0)

                            # Va retourner : (10, 8, 9)
print("16 : ", fct(10, 8, 9)) 

"""
On observe que pour l'instant, 
    les arguments par mot-clé sont pris dans l'ordre dans lesquels on les passe lors de l'appel. 
    
Comment faire si l'on souhaitait préciser l'argument par mot-clé z et garder les valeurs de x et y par défaut ? 

Simplement en précisant le nom de l'argument lors de l'appel :
"""

print("17 : ", fct(z = 10))  # Va retourner : (0, 0, 10)

# Variables locales et variables globales :

"""
Lorsqu'on manipule des fonctions, 
    il est essentiel de bien comprendre comment se comportent les variables. 

Une variable est dite locale lorsqu'elle est créée dans une fonction. 
Elle n'existera et ne sera visible que lors de l'exécution de ladite fonction.

Une variable est dite globale lorsqu'elle est créée dans le programme principal. 
Elle sera visible partout dans le programme.

Ceci ne vous paraît pas clair ? 
Nous allons prendre un exemple simple qui vous aidera à mieux saisir ces concepts. 

Observez le code suivant :
"""

    # Définition d'une fonction.
def fct():
    y = 3
    print("18 : ", var)  


    # Programme principal.
var = 5
y = 7

fct()
print("19 : ", y) 

"""
Dans cet exemple, il sera retourné :
5
7

Alors même que l'on reassigne la valeur 3 à la variable y dans la fonction.
On voit donc bien que ce qui se passe dans une fonction n'as pas d'impact sur les variables exterieures
"""

# Pour changer cela, on utilise le mot clé "global" :

    # Définition d'une fonction.
def fct():
    global y                # Ici on annonce que la fonction y est la même à l'interieur qu'à l'exterieur de la fonction
    y = 3
    print("20 : ", var)  


    # Programme principal.
var = 5
y = 7

fct()
print("21 : ", y)

"""
Il sera retourné :
5
3

Donc ce qu'il s'est passé à l'interieur de la fonction à eu un impact sur la variable y,
    pourtant à l'exterieur de la fonction.

On peut mettre plusieurs variables derrière le global : global a, b, c, d, ..., z
"""

# Le principe DRY :

"""
⚠⚠ Vous vous demandez surement à quoi servent vraiment les fonctions :

L'acronyme DRY signifie Don't Repeat Yourself. 
Les fonctions permettent de satisfaire ce principe en évitant la duplication de code. 
En effet, plus un code est dupliqué plusieurs fois dans un programme, 
    plus il sera source d'erreurs, 
    notamment lorsqu'il faudra le faire évoluer.
"""
