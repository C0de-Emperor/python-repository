############################################
########## La Gestion Des Erreurs ##########
############################################

"""
La base, en developpement informatique,
    c'est de considerer l'utilisateur comme un idiot ...

Imaginons la situation suivante :
"""

print("1  : ", int(input("entrez un nombre : ")))

"""
Qui vous dit que l'utilisateur va rentrer un nombre, et que se passera t'il s'il ne le fait pas ?

si l'utilisateur entre "bonjour" par exemple, voici l'erreur retounée :

print("1  : ", int(input("entrez un nombre : ")))
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'bonjour'

Donc il serait interressant d'avoir un moyen de gerer les erreurs :
"""

"""
Pour cela on utilise les mots clés "try" et "except", 
    voici un exemple :
"""

try :
    print("2  : ", int(input("entrez un nombre : ")))
except:
    print("2  : ", "une erreur est survenue")

"""
Ici, est executé uniquement ce qui est indenté avec le "try", 
    si une erreur survient alors l'execution s'interromp et repprend après le "except"

Comme on a pu le voir au dessus, il y a différent type d'erreurs,
    tel que : "ValueError", "TypeError", "NameError" ... etc

On peut donc specifier au except l'erreur qu'il doit capturer, je sous entend aussi, 
    que comme les conditions, un "try" peut admettre plusieurs "except".
"""

try :
    print("3  : ", int(input("entrez un nombre : ")))
except ValueError:
    print("3  : ", "une erreur de valeur est survenue")
except TypeError:
    print("3  : ", "une erreur de type est survenue")
except NameError:
    print("3  : ", "une erreur de nom est survenue")

"""
Enfin on peut aussi utiliser le mot clé "as" :
"""

try :
    print("4  : ", int(input("entrez un nombre : ")))
except ValueError as e:
        # Retournera : une erreur est survenue >>>  invalid literal for int() with base 10: 'E'
    print("4  : ", "une erreur est survenue >>> ", e )

"""
Voici un exmple concret de l'utilisation :
"""

def VerifiedInput (text : str):
    while True:
        try:
            return int(input(text))
        except:
            print("invalid input")

A = VerifiedInput("n  :  ")

"""
Ici, la boucle while ne s'arretera pas tant que le try n'aura pas capturé aucune erreur, 
    c'est à dire que l'utilisateur aura rentré une valeur que la fonction int() pourra transformer en int.

On peut remplacer int(), par str(), bool() ... etc en fonction de ce que l'on souhaite obtenir.
On peut aussi donner la fonction à appliquer en paramètre, car en effet, les fonctions sont aussi des objets. 
"""

def VerifiedInput (text : str, func):
    while True:
        try:
            return func(input(text))
        except:
            print("invalid input")

A = VerifiedInput("n  :  ", int)
