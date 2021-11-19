# full_stack_project
*Projet de l'unité Full Stack Data*

**Maxime Robillard**

L'objectif du projet est de créer un mini blog avec les fonctionnalités basique (création de compte, connexion, deconnexion, création d'article, modification des articles, pages de profil et accueil avec tous les articles ).
Le projet se décompose en une partie Backend et frontend pour avoir 2 logiques bien différentes.
Pour l'authentification, j'ai choisi d'utiliser les jetons JWT et de les stocker dans les cookies. La déconnexion peut se faire avant l'expiration du token.
La solution keycloak n'a pas été utilisée mais la logique de connexion est semblable.
***

**Pour démarrer l'application Flast api, la base de données, kong et keycloak**

A la racine du projet taper la commande : 'docker-compose up -d build'

***

**info partie backend**

La logique backend se décompose en plusieurs dossiers.


>Le dossier **apis**. Ce dossier comporte :
>- un dossier "version1" qui contient les fonctions necessaires  au backend réparties en 3 fichiers :
>  - route_articles.py contenant les fonctions CRUD nécessaire aux articles.
>  - route_login.py contenant les fonctions de connexion et de déconnexion pour les utilisateurs
>  - route_users.py contenant la création de l'utilisateur
>- et les fichiers :
>  - __init__.py pour indiquer que le dossier est un package
>  - base.py pour instancier les routers pour la logique backend
>  - utils.py contenant la classe utilisée pour l'authentification avec les cookies


>Le dossier **db**. Ce dossier comporte :
>- un dossier "models" qui contient les modèles pour la base de données. Ce dossier comporte les fichiers:
>  - articles.py
>  - users.py
>- un dossier "repositery" contenant requêtes à la base de donnée et décomposer comme ceci:
>  - articles.py
>  - login.py
>  - users.py
>- __init__.py pour indiquer que le dossier est un package
>- base.py pour importer toutes les fonctions
>- database.py pour la configuration de la base de donnée

>Le dossier **schemas** comprenant les schemas pour les articles, les utilisateurs et les tokens.
>Il est composé des fichiers :
>- __init__.py
>- articles.py
>- token.py
>- users.py

>Le dossier **test** comprenant quelques tests pour les fonctions implémentées. Il est composé:
>- du dossier "test_routes" qui permet de tester quelques routes pour les utilisateurs et les articles. Ce dossier se décompose en 3 fichiers:
>  - __init__.py
>  - articles.py
>  - test_users.py
>- le fichier __init__.py
>- le fichier conftest.py qui permet d'instancier sans erreur la base de données pour les tests.

>Le dossier **templates** comprenant les temlates html des différentes pages

>Le dossier **static** comprenant les fichiers css et scss et les ressources (images,...) nécessaires aux pages html.
---

**Info partie Frontend**

La logique Frontend se trouve dans le dossier webapps. Tout comme la partie backend c'est le framework fastapi qui est utilisé.
>Ce dossier est décomposé en 3 sous dossiers :
>- articles
>- auth
>- users
>Chacun de ces dossiers est composé des fichiers:
>- __init__.py
>- Forms.py
>- routes.py

>Et comporte deux fichiers à la racine (webapps):
>- __init__.py
>- base.py pour instancier les routers pour la logique frontend

---
Le fichier main.py permet de configurer l'API.

---
## Rest API
>Afin de vérifier l'API, vous pouvez naviguer sur la page suivante [localhost:8000/docs](http://localhost:8000/docs) et vous pouvez tester les requêtes **GET** et **POST** avec le button *Try it out*.

---

## Amélioration possible
### Keycloak

>L'implémentation de Keycloak est réalisé dans le docker et le service est opérationnel. Cependant, j'ai décidé de ne pas l'utiliser dans mon projet et gérer l'authentification avec des fonctions écrites dans le backend.
>Il est tout de même possible de relier keycloak à l'API en apportant de légère modification.

---

### Kong
>L'implémentation de Kong est réalisé dans le docker et le service est opérationnel. Konga a été instancié aussi à l'adresse http://localhost:1337/ pour permettre de visualiser les flux et les services créés.

