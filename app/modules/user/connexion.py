# Ensure the correct module is imported
from data.user_queries import get_user


def authenticate_user(connection, username, password):
    user = get_user(connection, username)
    # if username == "admin" and password == "password":
    #     self.login_frame.destroy()
    #     self.on_login_success()
    # else:
    #     messagebox.showerror(
    #         "Erreur", "Nom d'utilisateur ou mot de passe incorrect"
    #     )
    if user and user[2] == password:  # Vérifie le mot de passe
        return user
    return None
