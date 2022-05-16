# API LIVRE Full Stack

## DÉMARRAGE

### INSTALLATION DES DÉPENDANCES

#### Python 3.9.12

#### pip 22.1 from /usr/lib/python3/dist-packages/pip (python 3.9)

Suivez les instructions pour installer la dernière version de python pour votre système dans le [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### ENVIRONNEMENT VIRTUEL

Nous vous recommandons de travailler dans un environnement virtuel lorsque vous utilisez Python pour vos projets.Cela vous permet de séparer et d'organiser vos dépendances pour chaque projet. Vous pourez trouver toutes les instructions vous permettant de mettre en place un environnement virtuel pour votre système dans [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### DÉPENDANCES PIP

Maintenant que vous avez configurer et lancer votre environnement virtuel, Installez les dépendances en vous rendant sur le repectoire `Pr_flask`, ensuite exécutez les commandes suivantes :

```bash
pip install -r requirements.txt
ou
pip3 install -r requirements.txt
```

Ceci installera toutes les pacquets requis dans le fichier `requirements.txt`.

##### DÉPENDANCES CLÉS

- [Flask](http://flask.pocoo.org/) est un framework de microservices backend léger. Flask est nécessaire pour gérer les demandes et les réponses.

- [SQLAlchemy](https://www.sqlalchemy.org/) est la boîte à outils Python SQL et l'ORM que nous utiliserons pour gérer la base de données sqlite légère. Vous travaillerez principalement dans app.py et pourrez référencer models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) est l'extension que nous utiliserons pour gérer les demandes d'origine croisée de notre serveur frontend.



## DÉMARER LE SERVEUR

Depuis le répertoire `Pr_flask`, assurez-vous d'abord que vous travaillez dans l'environnement virtuel que vous avez créé.

Pour exécuter le serveur sur Linux ou Mac, exécutez :

```bash
export FLASK_APP=api.py
export FLASK_ENV=development
flask run
```

Pour exécuter le serveur sur Windows, exécutez :

```bash
set FLASK_APP=api.py
set FLASK_ENV=development
flask run
```

Mettre la variable `FLASK_ENV` à `development` va détecter les changements de fichiers et redémarrer le serveur automatiquement.

En mettant la variable `FLASK_APP` à `api.py`, flask utilisera le répertoire `api.py` et le fichier `__init__.py` pour trouver l'application.

Vous pouvez aussi exécutez

```
python api.py
```

## RÉFÉRENCE API

Démarrer

URL de base : Actuellement, cette application ne peut être exécutée que localement et n'est pas hébergée comme une URL de base. L'application backend est hébergée par défaut à l'adresse http://localhost:5000, qui est définie comme un proxy dans la configuration du frontend.

## GESTION D'ERREURS

Les erreurs sont retournées sous forme d'objets JSON au format suivant :

```
    {
    "success":False
    "error": 400
    "message":"Bad request
    }
```

L'API retournera trois types d'erreurs quand les requêtes échouent :

```
    . 400: Bad request
    . 404: Not found
    . 405: Method not allowed
    . 405: Method not allowed
```

## TERMINAISON

##### CATEGORIE

. ## GET/categories

GENERAL:
Cette terminaison retourne une liste d'objets Categorie, une valeur 'success', nombre total de categories.

    SAMPLE: curl http://localhost:5000/categorie
    {
        "categories": [
            {
                "id": 1,
                "libelle_categorie": "arr"
            },
            {
                "id": 3,
                "libelle_categorie": "Brainstorm"
            }
        ],
        "Nombre Catégories": 2,
        "Success": true 
    }

. ## GET/livres

GENERAL:
Cette terminaison retourne une liste d'objets livre, une valeur 'success', nombre total de livres.

    SAMPLE: curl http://localhost:5000/livre
    {
    "livre": [
         {
            "auteur": "Mhp",
            "categorie_id": 3,
            "date-publication": "Thu, 12 May 2022 00:00:00 GMT",
            "editeur": "Yves le curseur",
            "id": 1,
            "isbn": "34567",
            "titre": "Deception"
        },
        {
            "auteur": "Mhp",
            "categorie_id": 3,
            "date-publication": "Thu, 12 May 2022 00:00:00 GMT",
            "editeur": "Yves le curseur",
            "id": 5,
            "isbn": "34567",
            "titre": "Deception"
        },
        {
            "auteur": "Mhp",
            "categorie_id": 3,
            "date-publication": "Thu, 12 May 2022 00:00:00 GMT",
            "editeur": "Yves le curseur",
            "id": 6,
            "isbn": "34567",
            "titre": "Deception"
        },
        {
            "auteur": "Mhp",
            "categorie_id": 3,
            "date-publication": "Thu, 12 May 2022 00:00:00 GMT",
            "editeur": "Yves le curseur",
            "id": 7,
            "isbn": "34567",
            "titre": "Deception"
        },
        {
            "auteur": "Y-L-C",
            "categorie_id": 1,
            "date-publication": "Sat, 14 May 2022 00:00:00 GMT",
            "editeur": "ed 1956",
            "id": 8,
            "isbn": "534567",
            "titre": "Douleur"
        }
    ],
    "Nombre livres": 5,
    "Success": true

. ## DELETE/Categories/(categorie_id)

GENERAL:
Supprime la catégorie avec l'ID donneé s'il existe. Retourne l'ID de la catégorie suprimée, la valeur du success, et le nombre total de catégories

        SAMPLE: curl -X DELETE http://localhost:5000/categorie/6

    {
       "Categorie": 6,
        "Nombre Categorie": 3,
        "Success": true
    }

 ##PATCH/categories(categorie_id)

GENERAL:
Cette terminaison est utilisé pour modifier une catégorie
Nous retournons l'ID de la catégorie modifiée

    SAMPLE.....For Patch

    curl -X PATCH http://localhost:5000/categorie/1 -H "Content-Type:application/json" -d "

    {
         "Categories": {
               "id": 1,
               "libelle_categorie": "art"
            },
        "Success": true
    }

. ## POST/categories

GENERAL:
Cette terminaison est utilisé pour créer une nouvelle categorie.
Dans le cas de la création d'une categorie :
Nous retournons l'ID de la nouvelle categorie créée, la categorie créée, la liste des categories et le nombre de categories.

    SAMPLE.....For create

    curl -X POST http://localhost:5000/categories -H "Content-Type:application/json" -d 
    {
         "Liste ": [
                {
                  "id": 3,
                  "libelle_categorie": "Brainstorm"
                },
                {
                  "id": 1,
                  "libelle_categorie": "art"
                }
        ],
         "Nombre Catégories": 2,
         "Success": true

. ## POST/livres

GENERAL:
Cette terminaison est utilisé pour créer un nouveau livre.
Dans le cas de la création d'un livre :
Nous retournons l'ID du nouveau livre créé, le livre créé, la liste des livres et le nombre de livres.

    SAMPLE.....For create

    curl -X POST http://localhost:5000/livres -H "Content-Type:application/json" -d

    {
    "Livres": [
        {
            "auteur": "Mhp",
            "categorie_id": 3,
            "date-publication": "Thu, 12 May 2022 00:00:00 GMT",
            "editeur": "Yves le curseur",
            "id": 1,
            "isbn": "34567",
            "titre": "Deception"
        },
        {
            "auteur": "Mhp",
            "categorie_id": 3,
            "date-publication": "Thu, 12 May 2022 00:00:00 GMT",
            "editeur": "Yves le curseur",
            "id": 5,
            "isbn": "34567",
            "titre": "Deception"
        },
        {
            "auteur": "Mhp",
            "categorie_id": 3,
            "date-publication": "Thu, 12 May 2022 00:00:00 GMT",
            "editeur": "Yves le curseur",
            "id": 6,
            "isbn": "34567",
            "titre": "Deception"
        },
        {
            "auteur": "Mhp",
            "categorie_id": 3,
            "date-publication": "Thu, 12 May 2022 00:00:00 GMT",
            "editeur": "Yves le curseur",
            "id": 7,
            "isbn": "34567",
            "titre": "Deception"
        },
        {
            "auteur": "Y-L-C",
            "categorie_id": 1,
            "date-publication": "Sat, 14 May 2022 00:00:00 GMT",
            "editeur": "ed 1956",
            "id": 8,
            "isbn": "534567",
            "titre": "Douleur"
        }
    ],
    "Nombre livres": 5,
    "Success": true