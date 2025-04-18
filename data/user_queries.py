def get_user(connection, username):
    """
    Récupère un utilisateur par son nom d'utilisateur.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()


def insert_user(connection, username, password, role):
    """
    Insère un nouvel utilisateur dans la base de données.
    """
    with connection:
        connection.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, role),
        )


def create_user(connection, username, password, role):
    with connection:
        connection.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, role),
        )


def list_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT id, username, role FROM users")
    return cursor.fetchall()


def update_user(connection, user_id, username=None, password=None, role=None):
    with connection:
        if username:
            connection.execute(
                "UPDATE users SET username = ? WHERE id = ?", (username, user_id)
            )
        if password:
            connection.execute(
                "UPDATE users SET password = ? WHERE id = ?", (password, user_id)
            )
        if role:
            connection.execute(
                "UPDATE users SET role = ? WHERE id = ?", (role, user_id)
            )
