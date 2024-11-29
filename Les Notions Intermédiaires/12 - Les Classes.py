############################################
############### Les Classes ################
############################################

"""
La programmation orientée objet (POO) est un concept de programmation très puissant qui permet de structurer ses programmes d'une manière nouvelle. 
En POO, on définit un « objet » qui peut contenir des « attributs » ainsi que des « méthodes » qui agissent sur lui-même. 

Par exemple, on définit un objet « citron » qui contient les attributs « saveur » et « couleur », 
    ainsi qu'une méthode « presser » permettant d'en extraire le jus. En Python, on utilise une « classe » pour construire un objet. 
Dans notre exemple, la classe correspondrait au « moule » utilisé pour construire autant d'objets citrons que nécessaire.
"""

# La classe minimale

"""
En Python, le mot-clé class permet de créer sa propre classe, suivi du nom de cette classe. 
    
Par convention, un nom de classe commence toujours par une majuscule. 
Comme d'habitude, cette ligne attend un bloc d'instructions indenté définissant le corps de la classe.

Voyons un exemple simple dans l'interpréteur :
"""

class Citron:
    pass

print("1  : ", Citron)          # Va retourner : <class '__main__.Citron'>
print("2  : ", type(Citron))    # Va retourner : <class 'type'>

citron1 = Citron()
print("3  : ", citron1)         # Va retourner : <__main__.Citron object at 0x7ff2193a20f0>

"""
Ligne 1. La classe Citron est définie. 
    Pas besoin de parenthèses comme avec les fonctions dans un cas simple comme celui-là (nous verrons d'autres exemples plus loin où elles seront nécessaires).

Ligne 2. La classe ne contient rien, mais il faut mettre au moins une ligne, 
    on met donc ici le mot-clé Python pass qui ne fait rien (comme dans une fonction qui ne fait rien).

Lignes 4 et 5. Quand on tape le nom de notre classe Citron, 
    Python nous indique que cette classe est connue.

Lignes 6 et 7. Lorsqu'on regarde le type de notre classe Citron, 
    Python nous indique qu'il s'agit d'un type au même titre que type(int). Nous avons donc créé un nouveau type !

Ligne 8. On crée une instance de la classe Citron, 
    c'est-à-dire qu'on fabrique un représentant ou objet de la classe Citron, que nous nommons citron1.

Lignes 9 et 10. Lorsqu'on tape le nom de l'instance citron1, 
    l'interpréteur nous rappelle qu'il s'agit d'un objet de type Citron, ainsi que son adresse en mémoire.
"""

# Il est également possible de vérifier qu'une instance est bien issue d'une classe donnée avec la fonction isinstance() :

class Citron:
    pass
citron1 = Citron()
                                # retournera : True
print("4  : ", isinstance(citron1, Citron))

# Ajout d'un attribut d'instance :

    # Va retourner : ['__class__', '__delattr__', '__dict__', [...], '__weakref__']
print("5  : ", dir(citron1))

"""
L'objet possède de nombreuses méthodes ou attributs, 
    qui commencent et qui se terminent par deux caractères underscores. 
Je précise que les underscores indiquent qu'il s'agit de méthodes ou attributs destinés au fonctionnement interne de l'objet. 
Nous reviendrons sur certains d'entre-eux dans la suite.
"""

citron1.couleur = "jaune"
    # Va retourner : ['__class__', '__delattr__', '__dict__', [...], '__weakref__', 'couleur']
print("6  : ", dir(citron1))

    # Va retourner : "jaune"
print("7  : ", citron1.couleur)

"""
Ici on ajoute un attribut .couleur à l'instance citron1. Notez bien la syntaxe instance.attribut et le point qui lie les deux.
La fonction dir() nous montre que l'attribut .couleur a bien été ajouté à l'objet.

L'attribut nommé .__dict__ est particulièrement intéressant. 
Il s'agit d'un dictionnaire qui listera les attributs créés dynamiquement dans l'instance en cours :
"""

class Citron:
    pass
citron1 = Citron()

    # Va retourner : {} car aucun attribut n'a été ajouté dynamiquement.
print("8  : ", citron1.__dict__)

citron1.couleur = "jaune"

    # Va retourner : {'couleur': 'jaune'}
print("9  : ", citron1.__dict__)

"""
L'ajout d'un attribut depuis l'extérieur de la classe (on parle aussi du côté « client ») avec une syntaxe instance.nouvel_attribut = valeur, 
    créera ce nouvel attribut uniquement pour cette instance :
"""

class Citron:
    pass
citron1 = Citron()
citron1.couleur = "jaune"

    # Va retourner : {'couleur': 'jaune'}
print("9  : ", citron1.__dict__)

citron2 = Citron()

    # Va retourner : {}
print("10 : ", citron2.__dict__)

"""
Si on crée une nouvelle instance de Citron, ici citron2, elle n'aura pas l'attribut
couleur à sa création.

L'instruction del fonctionne bien sûr pour détruire un objet (par exemple : del citron1), 
    mais permet également de détruire un attribut d'instance. 
    
Si on reprend notre exemple citron1 ci-dessus :
"""

class Citron:
    pass
citron1 = Citron()
citron1.couleur = "jaune"

del citron1.couleur

    # Va retourner : {}
print("11 : ", citron1.__dict__)

# Les attributs de classe :

"""
Si on ajoute une variable dans une classe comme on créait une variable locale dans une fonction, 
    on crée ce qu'on appelle un attribut de classe :
"""

class Citron:
    couleur = "jaune"

"""
Définition
Une variable de classe ou attribut de classe est un attribut qui sera identique pour chaque instance. 
On verra plus bas que de tels attributs suivent des règles différentes par rapport aux attributs d'instance.

À l'extérieur ou à l’intérieur d'une classe, un attribut de classe peut se retrouver avec une syntaxe NomClasse.attribut :
"""


print("12 : ", Citron.couleur)  # Va retourner : "jaune"

"""
⚠⚠⚠ Attention ⚠⚠⚠
Même si on peut retrouver un attribut de classe avec la syntaxe instance.attribut, 
    un tel attribut ne peut pas être modifié avec une instruction de cette forme :

instance.attribut = nouvelle_valeur
"""

# Les méthodes :

"""
Une fonction définie au sein d'une classe est appelée méthode. 
Pour exécuter une méthode à l'extérieur de la classe, 
    la syntaxe générale est instance.méthode(). En général, on distingue attributs et méthodes (comme nous le ferons systématiquement dans ce chapitre). 
    
Toutefois, il faut garder à l'esprit qu'une méthode est finalement un objet de type fonction. 
Ainsi, elle peut être vue comme un attribut également, 
    concept que vous croiserez peut-être en consultant de la documentation externe.

Voici un exemple d'ajout d'une fonction, ou plus exactement d'une méthode, au sein d'une classe (attention à l'indentation !) :
"""

class Citron:
    def coucou(self):
        print("13 : ", "Coucou, je suis la mth .coucou() dans la classe Citron !")

if __name__ == "__main__":
    citron1 = Citron()
    citron1.coucou()

"""
Lignes 2 et 3. On définit une méthode nommée .coucou(), qui va afficher un petit message. 

    ⚠⚠⚠ Attention, cette méthode prend obligatoirement un argument que nous avons nommé ici self. 
    Nous verrons dans les deux prochaines rubriques la signification de ce self.
    Si on a plusieurs méthodes dans une classe, on saute toujours une ligne entre elles afin de faciliter la lecture (comme pour les fonctions).

Ligne 7 et 8. On crée l'instance citron1 de la classe Citron, puis on exécute la méthode .coucou() avec une syntaxe instance.méthode().

Une méthode étant une fonction, elle peut bien sûr retourner une valeur 
"""

# Le constructeur :

"""
Lors de l'instanciation d'un objet à partir d'une classe, 
    il peut être intéressant de lancer des instructions, comme, d'initialiser certaines variables. 

Pour cela, on ajoute une méthode spéciale nommée .__init__() : cette méthode s'appelle le « constructeur » de la classe. 
Il s'agit d'une méthode spéciale dont le nom est entouré de doubles underscores : en effet, elle sert au fonctionnement interne de notre classe et, 
    sauf cas extrêmement rare, elle n'est pas supposée être lancée comme une fonction classique par l'utilisateur de la classe. 

Ce constructeur est exécuté à chaque instanciation de notre classe, et ne renvoie pas de valeur, il ne possède donc pas de return.
"""

class Citron:
    def __init__(self):
        self.couleur = "jaune"

if __name__ == "__main__":
    citron1 = Citron()
        # Va retourner : "jaune"
    print("14 : ", citron1.couleur)

# Passage d'argument(s) à l'instanciation :

"""
Lors de l'instanciation, il est possible de passer des arguments au constructeur. 
Comme pour les fonctions, on peut passer des arguments positionnels ou par mot-clé, et en créer autant que l'on veut.

Voici un exemple :
"""

class Citron:
    def __init__(self, masse, couleur="jaune"):
        self.masse = masse
        self.couleur = couleur

if __name__ == "__main__":
    citron1 = Citron(100)
    print("15 : ", "citron1:", citron1.__dict__)
    citron2 = Citron(150, couleur="blanc")
    print("16 : ", "citron2:", citron2.__dict__)

"""
On a ici un argument positionnel (masse) et un autre par mot-clé (couleur). Le code donnera la sortie suivante :

citron1: {'masse': 100, 'couleur': 'jaune'}
citron2: {'masse': 150, 'couleur': 'blanc'}
"""

# Mieux comprendre le rôle du self :

"""
Cette rubrique va nous aider à mieux comprendre le rôle du self à travers quelques exemples simples. 
Regardons le code suivant dans lequel nous créons une nouvelle méthode .affiche_attributs():
"""

class Citron:
    def __init__(self, couleur="jaune"):
        self.couleur = couleur
        var = 2

    def affiche_attributs(self):
        print("17 : ", self)
        print("18 : ", self.couleur)
        print("19 : ", variable)


if __name__ == "__main__":
    citron1 = Citron()
    citron1.affiche_attributs()

"""
Ligne 3. On crée l'attribut couleur que l'on accroche à l'instance avec self.

Ligne 4. Nous créons cette fois-ci une variable var sans l'accrocher à self.

Ligne 6. Nous créons une nouvelle méthode dans la classe Citron qui se nomme .affiche_attributs(). 
Comme pour le constructeur, cette méthode prend comme premier argument une variable obligatoire, 
    que nous avons à nouveau nommée self. 
    
Il s'agit encore une fois d'une référence vers l'objet ou instance créé(e).

⚠⚠⚠ Attention
On peut appeler cette référence comme on veut, 
    toutefois nous vous conseillons vivement de l'appeler self, car c'est une convention en Python. 
Ainsi, quelqu'un qui lira votre code comprendra immédiatement de quoi il s'agit.

Ligne 7. Cette ligne va afficher le contenu de la variable self.

Lignes 8 et 9. On souhaite que notre méthode .affiche_attributs() 
    affiche ensuite l'attribut de classe .couleur ainsi que la variable var créée dans le constructeur .__init__().

L'exécution de ce code donnera :

Traceback (most recent call last):
  File "c:\Users\mttma\Documents\Projets Python\Explication Python.py", line n, in <module>
    citron1.affiche_attributs()
  File "c:\Users\mttma\Documents\Projets Python\Explication Python.py", line n, in affiche_attributs
    print("19 : ", variable)
                   ^^^^^^^^
NameError: name 'variable' is not defined. Did you mean: 'callable'?

Ligne 2. La méthode .affiche_attributs() montre que le self est bien une référence vers l'instance (ou objet)
    citron1 (ou vers n'importe quelle autre instance : par exemple, si on crée citron2 = Citron(), le self sera une référence vers citron2).

Ligne 3. La méthode .affiche_attributs() affiche l'attribut .couleur, 
    qui avait été créé précédemment dans le constructeur. 
    Vous voyez ici l'intérêt principal de l'argument self passé en premier à chaque méthode d'une classe : 
        il « accroche » n'importe quel attribut qui sera visible partout dans la classe, y compris dans une méthode où il n'a pas été défini.

Lignes 4 à 9. La création de la variable var dans la méthode .__init__() 
    sans l'accrocher à l'objet self fait qu'elle n'est plus accessible en dehors de .__init__(). 
    C'est exactement comme pour les fonctions classiques, 
        var est finalement une variable locale au sein de la méthode .__init__() et n'est plus visible lorsque l'exécution de cette dernière est terminée. 
    Ainsi, Python renvoie une erreur, car var n'existe pas lorsque .affiche_attributs() est en exécution.

En résumé, le self est nécessaire lorsqu'on a besoin d'accéder à différents attributs dans les différentes méthodes d'une classe. 
Le self est également nécessaire pour appeler une méthode de la classe depuis une autre méthode :
"""

class Citron:
    def __init__(self, couleur="jaune"):
        self.couleur = couleur
        self.affiche_message()

    def affiche_message(self):
        print("20 : ", "Le citron c'est trop bon !")


if __name__ == "__main__":
    citron1 = Citron("jaune pâle")

"""
Ligne 4. Nous appelons ici la méthode .affiche_message() depuis le constructeur. 
    Pour appeler cette méthode interne à la classe Citron, on doit utiliser une syntaxe self.methode(). 
    Le self sert donc pour accéder aux attributs, mais aussi aux méthodes, ou plus généralement à tout ce qui est accroché à la classe.

Lignes 6 et 7. La méthode .affiche_message() est exécutée. 
    On peut se poser la question « Pourquoi passer l'argument self à cette méthode alors qu'on ne s'en sert pas dans celle-ci ? »

Ligne 11. On crée l'instance citron1 en lui passant l'argument "jaune pâle". 
    La variable d'instance couleur prendra ainsi cette valeur au lieu de celle par défaut ("jaune"). 
    À noter, l'instanciation affichera le message Le citron c'est trop bon ! puisque la méthode .affiche_attributs()
        est appelée dans le constructeur .__init__()
"""

"""
⚠⚠⚠ Attention ⚠⚠⚠
Même si on ne se sert d'aucun attribut dans une méthode, 
    l'argument self (ou quel que soit son nom) est strictement obligatoire. 

En fait, la notation citron1.affiche_message() est équivalente à Citron.affiche_message(citron1). 
Testez les deux pour voir ! Dans cette dernière instruction, 
    on appelle la méthode accrochée à la classe Citron et on lui passe explicitement l'instance citron1 en tant qu'argument. 

La notation citron1.affiche_message() contient donc en filigrane un argument, 
    à savoir la référence vers l'instance citron1 que l'on appelle self au sein de la méthode.
"""
