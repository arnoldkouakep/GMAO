def add_personnel(connection, name, position, email, password, role):
    """
    Ajoute un nouveau personnel dans la base de données.
    """
    with connection:
        connection.execute(
            "INSERT INTO personnel (name, position, email, password, role) VALUES (?, ?, ?, ?, ?)",
            (name, position, email, password, role),
        )


def get_all_personnel(connection):
    """
    Récupère la liste de tout le personnel.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, position, email, role FROM personnel")
    return cursor.fetchall()


def get_personnel_by_email(connection, email):
    """
    Récupère un personnel par son email.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM personnel WHERE email = ?", (email,))
    return cursor.fetchone()
