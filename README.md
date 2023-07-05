# Application de bureau pour la gestion des stocks

Il s'agit d'une application de bureau construite à l'aide de Tkinter qui permet aux utilisateurs de gérer l'inventaire d'un magasin ou d'un entrepôt. L'application dispose d'une interface conviviale qui permet aux utilisateurs de consulter les produits disponibles dans le stock. L'administrateur peut modifier, ajouter et supprimer les produits de l'entrepôt et consulter également les produits.

## Fonctionnalités 

L'application de bureau de gestion des stocks comprend les éléments suivants:

- Ajout de nouveaux produits à l'inventaire
- Modification des informations produit existantes
- Suppression des produits de l'inventaire
- Authentification des clients
- Authentification des administrateurs

## Installation

Pour installer l'application de bureau de gestion des stocks, suivez ces étapes:

1. Clonez le référentiel sur votre machine locale.
2. Assurez-vous que Python 3.6 ou une version ultérieure est installée sur votre système.
3. Installez les bibliothèques requises en exécutant la commande :
    `pip install tkinter`.
4. Exécutez l'application en exécutant la commande `python index.py`.

## Utilisation 

Une fois que vous avez installé et lancé l'application de bureau de gestion des stocks, vous pouvez l'utiliser pour gérer votre inventaire en effectuant les tâches suivantes :
1. Inscrivez-vous à l'application de gestion des stocks.
2. Connectez-vous en utilisant votre nom d'utilisateur et votre mot de passe. Si vous êtes administrateur, connectez-vous avec username="admin" et password="1234", sinon vous êtes un utilisateur normal.
3. Consultez les nouveaux produits dans l'inventaire.
4. Recherchez les produits en cliquant sur \"Rechercher\" pour effectuer une recherche par nom, ou sur \"Recherche avancée\" pour une recherche avancée et remplissez les informations requises. 
5. Si vous êtes administrateur, vous pouvez ajouter un produit en cliquant sur le bouton \"Insert\" et en remplissant les informations requises.
6. Si vous êtes administrateur, vous pouvez modifier un produit en cliquant sur le bouton \"Update\" et en remplissant les informations requises.
7. Si vous êtes administrateur, vous pouvez supprimer un produit en cliquant sur le bouton \"Delete\" et en remplissant les informations requises.




## Conception des classes et objets pour gérer les produits et les utilisateurs :
1. Classe Database :

• Méthodes :
     - `__init__(self, db)`: pour la création de la table produit.
     - `insert(self, name, description, price, quantity, alert_quantity, last_entry_date, last_exit_date, image=None)`: pour insérer un nouveau produit.
     - `fetch_records(self)`: pour sélectionner les produits.
     - `update_records(self, name, description, price, quantity, alert_quantity, last_entry_date, last_exit_date, image, pid)`: pour modifier un produit.
     - `remove_record(self, pid)`: pour supprimer un produit.

• Création d'un nouvel utilisateur :
    Les fonctions utilisées :
    - `insert_user(username, password, is_admin=False)`: pour insérer un nouvel utilisateur dans la base de données.
    - `login(username, password)`: pour vérifier les informations.
    - `connect()`: pour se connecter.
    - `register()`: pour enregistrer un utilisateur

## Planification de l'architecture de la base de données :
1. Table "users":
    - id : clé primaire, entier, auto-incrémenté
    - username : texte, unique, non nul
    - password : texte, non nul
2. Table "products" :
    - pid : clé primaire, entier, auto-incrémenté
    - name : texte, non nul
    - description : texte
    - price : décimal, non nul
    - quantity : entier, non nul
    - alert_quantity : entier, non nul
    - last_entry_date : texte, non nul
    - last_exit_date : texte
    - image : varchar

## Crédits

L'application de bureau de gestion de stock a été créée par ELBOUAZZAOUI Asmaa, BENZALA Noutaila et ABOU BICHARA Manal pour leur projet de fin d'année. Remerciements particuliers à M. AMEKSA Mohamed pour ses conseils et son soutien.


