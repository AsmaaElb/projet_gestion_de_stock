import sqlite3
import tkinter as tk
from tkinter import ttk
import sys
import tkinter as tk


   
# créer une connexion à la base de données
conn = sqlite3.connect('stock2.db')
# créer une table pour les products
"""conn.execute('''CREATE TABLE IF NOT EXISTS products (
                pid INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                alert_quantity INTEGER NOT NULL,
                last_entry_date TEXT NOT NULL,
                last_exit_date TEXT NOT NULL,
                image VARCHAR)''')"""
conn.commit()

# définir une fonction pour afficher la liste des products
def afficher_liste_products(name=None):
    # effacer la liste de products précédente
    for row in treeview.get_children():
        treeview.delete(row)
    
    # sélectionner tous les products si aucun nom de produit n'est spécifié
    if name is None:
        products = conn.execute("SELECT * FROM products")
    # sinon sélectionner les products correspondant au nom de produit spécifié
    else:
        products = conn.execute("SELECT * FROM products WHERE name LIKE ?", ('%'+name+'%',))
    
    # ajouter les products à la liste sous forme de tableau
    for produit in products:
        treeview.insert("", "end", values=produit)

# définir une fonction pour afficher la liste des products avancée
def afficher_liste_products_avancee(name=None, description_produit_produit=None, prix_produit=None):
    # effacer la liste de products précédente
    for row in treeview.get_children():
        treeview.delete(row)
    
    # construire la requête SQL pour la recherche avancée
    query = "SELECT * FROM products WHERE 1=1"
    params = []
    if name:
        query += " AND name LIKE ?"
        params.append('%'+name+'%')
    if description_produit_produit:
        query += " AND description LIKE ?"
        params.append('%'+description_produit_produit+'%')
    if prix_produit:
        query += " AND price <= ?"
        params.append(prix_produit)
    
    # exécuter la requête SQL et ajouter les products à la liste sous forme de tableau
    products = conn.execute(query, params)
    for produit in products:
        treeview.insert("", "end", values=produit)

# définir une fonction pour gérer la recherche
def rechercher():
    name = name_entree.get()
    if name:
        afficher_liste_products(name)
    else:
        afficher_liste_products()

# définir une fonction pour gérer la recherche avancée
def rechercher_avancee():
    name = name_entree.get()
    description_produit_produit = description_produit_produit_entree.get()
    prix_produit = prix_produit_entree.get()
    afficher_liste_products_avancee(name, description_produit_produit, prix_produit)

# créer une fenêtre tkinter
fenetre = tk.Tk()
fenetre.title("Liste des products")

# créer une boîte pour la recherche de base
boite_recherche_base = ttk.Frame(fenetre)
boite_recherche_base.pack(padx=10, pady=10, fill=tk.X)

ttk.Label(boite_recherche_base, text="Rechercher par nom de produit :").pack(side=tk.LEFT)
name_entree = ttk.Entry(boite_recherche_base, width=30)
name_entree.pack(side=tk.LEFT, padx=10)
#créer un bouton pour effectuer la recherche de base
ttk.Button(boite_recherche_base, text="Rechercher", command=rechercher).pack(side=tk.LEFT)
#créer une boîte pour la recherche avancée
boite_recherche_avancee = ttk.Frame(fenetre)
boite_recherche_avancee.pack(padx=10, pady=10, fill=tk.X)

ttk.Label(boite_recherche_avancee, text="Recherche avancée :").pack(side=tk.LEFT)

ttk.Label(boite_recherche_avancee, text="Nom de produit :").pack(side=tk.LEFT)
name_entree_avancee = ttk.Entry(boite_recherche_avancee, width=30)
name_entree_avancee.pack(side=tk.LEFT, padx=10)

ttk.Label(boite_recherche_avancee, text="Description_produit de produit :").pack(side=tk.LEFT)
description_produit_produit_entree = ttk.Entry(boite_recherche_avancee, width=30)
description_produit_produit_entree.pack(side=tk.LEFT, padx=10)

ttk.Label(boite_recherche_avancee, text="Prix de produit maximum :").pack(side=tk.LEFT)
prix_produit_entree = ttk.Entry(boite_recherche_avancee, width=10)
prix_produit_entree.pack(side=tk.LEFT, padx=10)

ttk.Button(boite_recherche_avancee, text="Rechercher", command=rechercher_avancee).pack(side=tk.LEFT)
#créer une boîte pour afficher la liste des products
boite_liste_products = ttk.Frame(fenetre)
boite_liste_products.pack(padx=10, pady=10)
#créer un arbre pour afficher la liste des products
treeview = ttk.Treeview(boite_liste_products, columns=("name", "description_produit", "prix_unitaire", "quantite_en_stock", "seuil_alerte_stock", "date_derniere_entree_stock", "date_derniere_sortie_stock", "image"))
treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#ajouter des en-têtes de colonnes à l'arbre
treeview.heading("name", text="Name")
treeview.heading("description_produit", text="Description_produit")
treeview.heading("prix_unitaire", text="Prix unitaire")
treeview.heading("quantite_en_stock", text="Quantité en stock")
treeview.heading("seuil_alerte_stock", text="Seuil d'alerte de stock")
treeview.heading("date_derniere_entree_stock", text="Date de dernière entrée en stock")
treeview.heading("date_derniere_sortie_stock", text="Date de dernière sortie de stock")
treeview.heading("image", text="Image")
#remplir l'arbre avec la liste des products
afficher_liste_products()
#exécuter la boucle principale de tkinter
fenetre.mainloop()
#fermer la connexion à la base de données
conn.close()