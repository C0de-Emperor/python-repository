############################################
############# les Boucles For ##############
############################################

"""
En programmation, on est souvent amené à répéter plusieurs fois une instruction. 
Incontournables à tout langage de programmation, 
    les boucles vont nous aider à réaliser cette tâche répétitive de manière compacte et efficace.
"""

"""
Imaginez par exemple que vous souhaitiez afficher les éléments d'une liste les uns après les autres. 
Dans l'état actuel de vos connaissances, 
    il faudrait taper quelque chose du style :
"""

animaux = ["girafe", "tigre", "singe", "souris"]
print("1-1  : ", animaux[0])
print("1-2  : ", animaux[1])
print("1-3  : ", animaux[2])
print("1-4  : ", animaux[3])

"""
Si votre liste ne contient que 4 éléments, 
    ceci est encore faisable mais imaginez qu'elle en contienne 100 voire 1 000 ! 
Pour remédier à cela, il faut utiliser les boucles . 

Regardez l'exemple suivant :
"""

animaux = ["girafe", "tigre", "singe", "souris"]
for animal in animaux:
                            # Va retourner : girafe tigre singe souris
    print("2    : ", animal)        

"""
Commentons en détails ce qu'il s'est passé dans cet exemple :

La variable animal est appelée variable d'itération , 
    elle prend successivement les différentes valeurs de la liste animaux à chaque itérations (ou tour) de boucle.

On verra un peu plus loin dans ce chapitre que l'on peut choisir le nom que l'on veut pour cette variable. 
Celle-ci est créée par Python la première fois que la ligne contenant le for est exécutée (si elle existait déjà son contenu serait écrasé). 
Une fois la boucle terminée, 
    cette variable d'itération animal n'est pas détruite et conserve la dernière valeur de la liste animaux (ici la chaîne de caractères "souris").

Notez bien les types des variables utilisées ici :

animaux est une liste sur laquelle on itère ;
animal est une chaîne de caractères car chaque élément de la liste animaux est une chaîne de caractères.

Nous verrons plus loin que la variable d'itération peut être de n'importe quel type selon la liste parcourue.
En Python, une boucle itère la plupart du temps sur un objet dit séquentiel (c'est-à-dire un objet constitué d'autres objets) tel qu'une liste. 
De tels objets sont dits itérables car on peut effectuer une boucle dessus. 
Nous verrons aussi plus tard d'autres objets séquentiels sur lesquels on peut itérer dans une boucle.

D'ores et déjà, prêtez attention au caractère deux-points « : » à la fin de la ligne débutant par for. 
Cela signifie que la boucle for attend un bloc d'instructions, 
    en l’occurrence toutes les instructions que Python répétera à chaque itération de la boucle. 
    
On appelle ce bloc d'instructions le corps de la boucle. 

Comment indique-t-on à Python où ce bloc commence et se termine ? Cela est signalé uniquement par l'indentation,
    c'est-à-dire le décalage vers la droite de la (ou des) ligne(s) du bloc d'instructions.
"""

"""
Dans les exemples ci-dessus, 
    nous avons exécuté une boucle en itérant directement sur une liste. 
    
Une tranche d'une liste étant elle même une liste, on peut également itérer dessus :
"""

animaux = ["girafe", "tigre", "singe", "souris"]
for animal in animaux[1:3]:
                            # Va retourner : tigre singe
    print("3    : ", animal)

"""
On a vu que les boucles for pouvaient utiliser une liste contenant des chaînes de caractères, 
    mais elles peuvent tout aussi bien utiliser des listes contenant des entiers (ou n'importe quel type de variable) :
"""

for i in [1, 2, 3]:
    print("4    : ", i)                # Va retourner : 1 2 3

# La fonction range()

"""
L'instruction range() est une fonction spéciale en Python qui génère des nombres entiers compris dans un intervalle.

Lorsqu'elle est utilisée en combinaison avec la fonction list(), on obtient une liste d'entiers. Par exemple :
"""
                            # Retournera [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("5    : ", list(range(10)))

"""
La commande list(range(10)) a généré une liste contenant tous les nombres entiers de 0 inclus à 10 exclu.
"""

    # Dans l'exemple ci-dessus, la fonction range() a pris un argument, mais elle peut également prendre deux ou trois arguments, voyez plutôt :

    # les argument sont : range(debut[inclu], fin[exclu], pas )

                            # Retournera [0, 1, 2, 3, 4]
print("6    : ", list(range(0, 5)))

                            # Retournera [15, 16, 17, 18, 19]
print("7    : ", list(range(15, 20)))

                            # Retournera [0, 200, 400, 600, 800]
print("8    : ", list(range(0, 1000, 200)))

                            # Retournera [2, 1, 0, -1]
print("9    : ", list(range(2, -2, -1)))

    # Associé aux boucles for :

for i in range(4):
    print("10   : ", i)     # Va retourner : 0 1 2 3 

"""
Contrairement à la création de liste avec list(range(4)), 
    la fonction range() peut être utilisée telle quelle dans une boucle. 
Il n'est pas nécessaire de taper for i in list(range(4)): même si cela fonctionnerait également.

Comment cela est possible ? 
    range() est une fonction qui a été spécialement conçue pour cela, 
    c'est-à-dire que l'on peut itérer directement dessus. Pour Python, 
    il s'agit d'un nouveau type : par exemple dans l'instruction x = range(3), 
    la variable x est de type range (tout comme on avait les types int, float, str ou list) à utiliser spécialement avec les boucles.
"""

# Nommage de la variable d'itération :

"""
Dans l'exemple précédent, nous avons choisi le nom i pour la variable d'itération. 
Ceci est une habitude en informatique et indique en général qu'il s'agit d'un entier (le nom i vient sans doute du mot indice ou index en anglais).

Si, par contre, 
    vous itérez sur une liste comportant des chaînes de caractères (ou tout autre type de variable), 
    utilisez un nom explicite pour la variable d'itération. Par exemple :

    for prenom in ["Joe", "Bill", "John"]:
        ...
"""

# Itération sur les indices : 

    # Revenons à notre liste animaux. Nous allons maintenant parcourir cette liste, mais cette fois par une itération sur ses indices :

animaux = ["girafe", "tigre", "singe", "souris"]
for i in range(4):
    print("11   : ", animaux[i])

"""
La variable i prendra les valeurs successives 0, 1, 2 et 3 
    et on accèdera à chaque élément de la liste animaux par son indice (i.e. animaux[i]). 
    
Notez à nouveau le nom i de la variable d'itération car on itère sur les indices.
"""

# Mais comment choisir entre Itération sur les indices ou sur les element comme à l'exemple 2 :

"""
La plus efficace est celle qui réalise les itérations directement sur les éléments

Toutefois, il se peut qu'au cours d'une boucle vous ayez besoin des indices, auquel cas vous devrez itérer sur les indices :
"""

animaux = ["girafe", "tigre", "singe", "souris"]
for i in range(len(animaux)):
    # Ici les {} servent à introduire des variables dans des chaines de caractères : !!! le f devant la chaine de caractère est très important
    print("12   : ", f"L'animal {i} est un(e) {animaux[i]}")

"""
Enfin, Python possède la fonction enumerate() qui vous permet d'itérer sur les indices et les éléments eux-mêmes :

L'objet énuméré génère des paires contenant un compteur (à partir d'une valeur, qui par défaut vaut zéro) et une valeur produite par l'argument iterable.
"""

animaux = ["girafe", "tigre", "singe", "souris"]
for i, animal in enumerate(animaux):
    print("13   : ",f"L'animal {i} est un(e) {animal}")
