############################################
################ les Ints ##################
############################################

a = 2                       # peut être n'importe quel entier relatif
print("1  : ", type(a))

# il est possible de convertir des objets en Int

b = "2"                     # un string
b = int(b)                  # la fonction int() : Convertit un nombre ou une chaîne de caractères en un entier, ou retourne 0 si aucun argument n'est fourni.
print("2  : ", type(b))

b = 3.6                     # un relatif
b = int(b)                  # va arrondir a l'entier inferieur : 3.4 donnera 3 tout comme 3.9999...
print("3  : ", b)            

c = True                    # un boolean (peut prendre deux valeurs différentes seulement, True ou False)
c = int(c)
print("4  : ", c)           # 1 correspond a True et 0 à False


############################################
################ les String ################
############################################

a = "2"                     # peut être n'importe quel entier relatif
print("5  : ", type(a))

# il est possible de convertir des objets en Str

b = 2                       # un string
b = str(b)                  # la fonction str() : Crée un nouvel objet de type chaîne de caractères à partir de l'objet donné.
print("6  : ", type(b))

c = True                    # un boolean
c = str(c)
print("7  : ", c)           # va transformer True en "True" et False en "False"


############################################
############### les Booleans ###############
############################################

a = True                    # peut prendre 2 valeurs possibles : True / False
print("8  : ", type(a))

# il est possible de convertir des objets en Bool

b = 0                       # un entier
b = bool(b)                 # la fonction bool(x) : Renvoie True lorsque l'argument x est vrai, False sinon.
print("9  : ", b)           # va renvoyer False, car 0 est faux, en revanche tout autre entier, relatif ou str retournera True

# un bool peut aussi prendre comme valeur une condition :

x = int( 3 )
isPositive = (x > 0)        # ici, la variable isPositive prendra la valeur True si X (strictement) positif sinon false
print("10 : ", isPositive)

"""
voici les comparateurs possibles : 

a == b                      # lire a egal b
a != b                      # lire a different de b
a > b                       # lire a strictement superieur à b
a < b                       # lire a strictement inferieur à b
a >= b                      # lire a superieur ou egal à b
a <= b                      # lire a inferieur ou egal à b

"""


# le mot clé "not"

a = bool( True )
a = not a
print("11 : ", a)           # va retourner False si a = True et inversement


# les mots clés "and" et "or"

x = int( 3 )
isPositive = (x > 0) 

isGreaterThan5 = x > 5      # comme vous le voyez les parenthèses ne sont pas obligatoires mais ajoutent de la lisibilité

                            # ici, isPositiveAndGreaterThan5 prendra la valeur True si les deux conditions sont vraies
                            # sinon si au moins une, ou les deux sont fausses alors cela renverra False
isPositiveAndGreaterThan5 = isPositive and isGreaterThan5
print("12 : ", isPositiveAndGreaterThan5)

                            # ici, isPositiveAndGreaterThan5 prendra la valuer True si au moins une condition est vraie ou les deux,
                            # sinon si les deux sont fausses alors cela renverra False
isPositiveOrGreaterThan5 = isPositive or isGreaterThan5
print("13 : ", isPositiveOrGreaterThan5)


############################################
################ les Floats ################
############################################

a = 2.0                     # peut être n'importe quel entier relatif ou rationnel tant qu'il s'ecris avec un point, meme s'il n'y a que des 0 derriere.
print("14 : ", type(a))

# il est possible de convertir des objets en Float

b = "2"                     # un string
b = float(b)                # la fonction float() : Convertit une chaîne ou un nombre en un nombre à virgule flottante, si possible.
print("15 : ", b)           # renvoi 2.0

b = 3                       # un Int
b = float(b)        
print("16 : ", b)           # retourne 3.0            

c = False                   # un boolean
c = float(c)
print("17 : ", c)           # retourne 1.0 pour True et 0.0 pour Flase

d = 3.0000000000            # c'est un Float avec 10 chiffre après la virgule, il ne sera pourtant enregistré qu'en tant que : d = 3.0
print("18 : ", d)

e = 3.0000000001            # ici, c'est un Float avec neufs 0 après la virgule et un 1 , il sera enregistré en tant que tel : e = 3.0000000001  
print("19 : ", e)

f = 3.1415926535            # voici les 10 premières decimales de pi.
f = round(f)                # la fonction round : 
"""
Arrondit un nombre à une précision donnée en chiffres décimaux.

La valeur de retour est un entier si la precision est omise ou défini sur None. 
Sinon, la valeur de retour a le même type que le nombre. la precision peut être négative.
"""

print("20 : ", f)           # va retourner un Int : 3

f = 3.1415926535            # voici les 10 premières decimales de pi.
precision = int( 2 )        # ceci est la precision, c'est a dire le nombre de decimales que l'on souhaite conserver, ici 2
f = round(f, precision)     # la fonction round va donc retourner 3.14
print("21 : ", f)
