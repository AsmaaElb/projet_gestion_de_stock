# Gestion de stock Desktop Application

Il s'agit d'une application de bureau construite à l'aide de Tkinter qui permet aux utilisateurs de
gérer l'inventaire d'un magasin ou d'un entrepôt. L'application dispose d'une interface conviviale 
qui permet aux utilisateurs de consulter les produits disponibles dans le stock ainsi que l'admin
ayant un but de modifier , ajouter et supprimer les produits de l'entrepot , n'oublions pas qu'il 
peut aussi consulter les produits.

## Caractéristiques 

L'application de bureau de gestion de stock comprend les éléments suivants:

- Ajouter de nouveaux produits à l'inventaire
- Modifier les informations produit existantes
- Supprimer des produits de l'inventaire
- Authentification des clients
- Authentification des admins

## Installation

Pour installer l'application de bureau de gestion de stock , suivez ces
pas:

1. Clonez le référentiel sur votre machine locale.
2. Assurez-vous que Python 3.6 ou version ultérieure est installée sur votre système.
3. Installez les bibliothèques requises en exécutant la commande :
    `pip installer tkinter`.
4. Exécutez l'application en exécutant la commande `python index.py`.

## Utilisation 

Une fois que vous avez installé et lancé le bureau de gestion de stock
Application, vous pouvez l'utiliser pour gérer votre inventaire en effectuant la
tâches suivantes :
1. S'inscrire à l'application de gestion de stock
2. Connectez-vous en utilisant votre nom d'utilisateur et votre mot de passe.Si il'est admin en se connectant par username="admin" et passwword="1234" sinon c'est un utilisatuer normal
3. Consulter de nouveaux produits à l'inventaire 
4. Rechercher les produits en cliquant sur \"rechercher\" pour la recherche par nom et \"recherche avancé"\ pour une recherche avancé et remplissez les informations requises. 
5. S'il s'agit d'un admin , il peut ajouter un produit en cliquant sur \"Insert\"
    bouton et remplissez les informations requises.
6. S'il s'agit d'un admin , il peut modifier un produit en cliquant sur \"Update\"
    bouton et remplissez les informations requises.
7. S'il s'agit d'un admin , il peut supprimer un produit en cliquant sur \"Delete \"
    bouton et remplissez les informations requises.


## Conception des classes et objets pour gérer les produits et les utilisateurs :
1.	Classe Database :

•	Méthodes :
     def __init__(self, db):pour la création de la table produit
     def insert(self, name, description, price, quantity, alert_quantity, last_entry_date, last_exit_date, image=None):pour insérer un nouveau produit.
     def fetch_records(self):pour séléctionner les produits.
	 def update_recordS(self, name, description, price, quantity, alert_quantity, last_entry_date, last_exit_date,image, pid):pour modifier un produit.
	 def remove_record(self, pid):pour supprimer un produit

•   Création d'un nouveau utilisateur
    les fonctions qu'on a utilisé :
    def insert_user(username, password,is_admin=False):pour insérer un nouvel utilisateur dans la base de données
    def login(username, password):pour vérifier les infos 
    def connect():pour se connecter 
    def register():pour enregistrer un utilisateur
## Planification de l'architecture de la base de données :
1.	Table "users":
•	id : clé primaire, entier, auto-incrémenté
•	username : texte, unique, non nul
•	password : texte, non nul
2.	Table "products" :
•	pid : clé primaire, entier, auto-incrémenté
•	name : texte, non nul
•	description : texte
•	price : décimal, non nul
•	quantity : entier, non nul
•	alert_quantity : entier, non nul
•	last_entry_date : texte, non nul
•	last_exit_date :  texte
•	image : varchar

## Crédits

L'application de bureau de gestion de stock a été crée par BENZALA Noutaila ,
ELBOUAZZAOUI  Asmaa , ABOU BICHARA Manal  pour leur  projet  de  fin  d'année.
Remerciements particuliers à Mr.AMEKSA Mohamed pour leurs conseils et leur soutien.

