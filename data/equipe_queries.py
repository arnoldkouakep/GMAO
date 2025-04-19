def add_team(connection, name, shift, day):
    """
    Ajoute une nouvelle équipe dans la base de données.
    """
    with connection:
        connection.execute(
            "INSERT INTO equipes (name, shift, day) VALUES (?, ?, ?)",
            (name, shift, day),
        )


def get_all_teams(connection):
    """
    Récupère la liste de toutes les équipes.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, shift, day FROM equipes")
    return cursor.fetchall()
