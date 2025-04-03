############################################
############# les Boucles While ############
############################################

"""
Une alternative à l'instruction for couramment utilisée en informatique est la boucle while. 
Avec ce type de boucle, 
    une série d'instructions est exécutée tant qu'une condition est vraie. 
"""

# Par exemple :

i = 1
while i <= 4:
    print("1  : ", i)
    i = i + 1

"""
Remarquez qu'il est encore une fois nécessaire d'indenter le bloc d'instructions correspondant au corps de la boucle (ici, les instructions lignes 3 et 4).

Une boucle while nécessite généralement trois éléments pour fonctionner correctement :

>>> Initialisation de la variable d'itération avant la boucle (ligne 1).

>>> Test de la variable d'itération associée à l'instruction while (ligne 2).

>>> Mise à jour de la variable d'itération dans le corps de la boucle (ligne 4).

!! A noter qu'il n'est pas obligatoire d'avoir un aspect itératoire à la boucle, il faut juste que le code en son sein lui permette de s'arrêter

Faites bien attention aux tests et à l'incrémentation que vous utilisez, 
    car une erreur mène souvent à des « boucles infinies » qui ne s'arrêtent jamais. 
Vous pouvez néanmoins toujours stopper l'exécution d'un script Python à l'aide de la combinaison de touches Ctrl-C
    (c'est-à-dire en pressant simultanément les touches Ctrl et C).
"""

# La fonction input() :

"""
La fonction input() en Python permet de lire une entrée utilisateur depuis l'entrée standard (généralement le clavier).

Elle prend en argument un message (sous la forme d'une chaîne de caractères) (qui sera affiché dans la console), 
    demande à l'utilisateur d'entrer une valeur (ET STOPPE L'EXECUTION du programme tant que entrée n'est pas pressée) et renvoie celle-ci sous forme d'une chaîne de caractères, 
    qu'il faut ensuite convertir si besoin.
"""

entreeUtilisateur = input("saisir une lettre : ")

print("2  : ", entreeUtilisateur )

"""
La boucle while combinée à la fonction input() peut s'avérer commode lorsqu'on souhaite demander à l'utilisateur une valeur numérique. 
"""

i = 0
while i < 10:
                            # Ici, le programme ne s'arretera pas tant que l'utilisateur n'aura pas saisi une valeur superieur a 10
    reponse = input("Entrez un entier supérieur à 10 : ")
    i = int(reponse)
