import sqlite3


def connect_db(db_file):
    connection = sqlite3.connect(db_file)
    return connection


def initialize_db(connection):
    with connection:
        # Création de la table des utilisateurs
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
            """
        )
        # Création de la table des permissions
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS permissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                module_name TEXT NOT NULL,
                role TEXT NOT NULL,
                can_access INTEGER NOT NULL
            )
            """
        )
        # Insertion des permissions par défaut
        connection.execute(
            """
            INSERT OR IGNORE INTO permissions (module_name, role, can_access) VALUES
            ('Gestion des utilisateurs', 'admin', 1),
            ('Gestion des utilisateurs', 'user', 0),
            ('Gestion de la maintenance', 'admin', 1),
            ('Gestion de la maintenance', 'user', 1),
            ('Gestion des équipements', 'admin', 1),
            ('Gestion des équipements', 'user', 1),
            ('Gestion des interventions', 'admin', 1),
            ('Gestion des interventions', 'user', 1),
            ('Gestion des rapports', 'admin', 1),
            ('Gestion des rapports', 'user', 1),
            ('Gestion des alertes', 'admin', 1),
            ('Gestion des alertes', 'user', 1),
            ('Gestion des historiques', 'admin', 1),
            ('Gestion des historiques', 'user', 1),
            ('Gestion des statistiques', 'admin', 1),
            ('Gestion des statistiques', 'user', 1),
            ('Gestion des sauvegardes', 'admin', 1),
            ('Gestion des sauvegardes', 'user', 0),
            ('Gestion des mises à jour', 'admin', 1),
            ('Gestion des mises à jour', 'user', 0),
            ('Gestion des configurations', 'admin', 1),
            ('Gestion des configurations', 'user', 0)
            """
        )
        # Insertion d'un utilisateur par défaut
        connection.execute(
            """
            INSERT OR IGNORE INTO users (username, password, role) VALUES
            ('admin', 'admin123', 'admin'),
            ('user', 'user123', 'user')
            """
        )
