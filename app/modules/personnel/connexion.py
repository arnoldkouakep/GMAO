# Ensure the correct module is imported
from data.personnel_queries import get_personnel_by_email


def authenticate_user(connection, email, password):
    personnel = get_personnel_by_email(connection, email)
    print(
        f"Utilisateur trouvé : {dict(personnel)}"
    )  # Affiche les détails de l'utilisateur
    # if username == "admin" and password == "password":
    #     self.login_frame.destroy()
    #     self.on_login_success()
    # else:
    #     messagebox.showerror(
    #         "Erreur", "Nom d'utilisateur ou mot de passe incorrect"
    #     )
    print(
        f"{personnel["password"]} = Mot de passe = {password}"
    )  # Affiche les détails de l'utilisateur

    if personnel and personnel["password"] == password:  # Vérifie le mot de passe
        return personnel
    return None
