import tkinter as tk
from tkinter import messagebox
from app.modules.personnel.login_form import LoginScreen
from app.modules.equipe.team_controller import TeamController
from data.database import connect_db, initialize_db


class MainApp:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection

        # Configuration de la fenêtre principale
        self.root.title("GMAO - Application Principale")
        self.root.geometry("800x600")

        # Création des zones
        self.create_top_menu()
        self.create_footer()
        self.create_left_menu()
        self.create_center_frame()

    def create_top_menu(self):
        """Créer la zone supérieure pour les menus des modules."""
        top_frame = tk.Frame(self.root, bg="lightblue", height=50)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(top_frame, text="Modules", font=("Arial", 14), bg="lightblue").pack(
            side=tk.LEFT, padx=10
        )

        # Boutons des modules
        tk.Button(
            top_frame, text="Personnel", command=self.show_personnel_submodules
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Équipe", command=self.show_team_submodules).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(top_frame, text="Quitter", command=self.root.quit).pack(
            side=tk.RIGHT, padx=10
        )

    def create_footer(self):
        """Créer la zone inférieure pour le pied de page."""
        footer_frame = tk.Frame(self.root, bg="lightgray", height=30)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        tk.Label(
            footer_frame, text="© 2025 GMAO - Tous droits réservés", bg="lightgray"
        ).pack()

    def create_left_menu(self):
        """Créer la zone gauche pour les sous-modules."""
        self.left_frame = tk.Frame(self.root, bg="lightyellow", width=200)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(
            self.left_frame, text="Sous-modules", font=("Arial", 12), bg="lightyellow"
        ).pack(pady=10)

    def create_center_frame(self):
        """Créer la zone centrale pour les interfaces des modules."""
        self.center_frame = tk.Frame(self.root, bg="white")
        self.center_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    def clear_center_frame(self):
        """Efface le contenu de la zone centrale."""
        for widget in self.center_frame.winfo_children():
            widget.destroy()

    def show_team_submodules(self):
        """Afficher les sous-modules pour le module Équipe."""
        # Effacer les sous-modules existants
        for widget in self.left_frame.winfo_children():
            widget.destroy()

        tk.Label(
            self.left_frame,
            text="Sous-modules Équipe",
            font=("Arial", 12),
            bg="lightyellow",
        ).pack(pady=10)

        # Ajouter les sous-modules
        tk.Button(
            self.left_frame, text="Ajouter une équipe", command=self.show_add_team_form
        ).pack(pady=5, fill=tk.X)
        tk.Button(
            self.left_frame, text="Liste des équipes", command=self.show_list_teams_form
        ).pack(pady=5, fill=tk.X)

    def show_personnel_submodules(self):
        """Afficher les sous-modules pour le module Personnel."""
        # Effacer les sous-modules existants
        for widget in self.left_frame.winfo_children():
            widget.destroy()

        tk.Label(
            self.left_frame,
            text="Sous-modules Personnel",
            font=("Arial", 12),
            bg="lightyellow",
        ).pack(pady=10)

        # Ajouter les sous-modules
        tk.Button(
            self.left_frame,
            text="Ajouter un personnel",
            command=self.show_add_personnel_form,
        ).pack(pady=5, fill=tk.X)
        tk.Button(
            self.left_frame,
            text="Liste du personnel",
            command=self.show_list_personnel_form,
        ).pack(pady=5, fill=tk.X)

    def show_add_team_form(self):
        """Afficher le formulaire pour ajouter une équipe."""
        self.clear_center_frame()
        from GMAO.app.modules.equipe.add_team_form import AddTeamForm

        AddTeamForm(self.center_frame, self.connection)

    def show_list_teams_form(self):
        """Afficher la liste des équipes."""
        self.clear_center_frame()
        from GMAO.app.modules.equipe.list_teams_form import ListTeamsForm

        ListTeamsForm(self.center_frame, self.connection)

    def show_add_personnel_form(self):
        """Afficher le formulaire pour ajouter un personnel."""
        self.clear_center_frame()
        from GMAO.app.modules.personnel.add_personnel_form import AddPersonnelForm

        AddPersonnelForm(self.center_frame, self.connection)

    def show_list_personnel_form(self):
        """Afficher la liste du personnel."""
        self.clear_center_frame()
        from GMAO.app.modules.personnel.list_personnel_form import ListPersonnelForm

        ListPersonnelForm(self.center_frame, self.connection)


def main():
    connection = connect_db("data/database.db")
    initialize_db(connection)

    root = tk.Tk()
    LoginScreen(root, connection, lambda: MainApp(root, connection))
    root.mainloop()


if __name__ == "__main__":
    main()
