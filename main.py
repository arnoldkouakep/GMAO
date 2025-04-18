import tkinter as tk
from tkinter import messagebox
from app.modules.user.login import LoginScreen
from data.database import connect_db, initialize_db


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GMAO - Gestion de Maintenance")
        self.root.geometry("600x400")

        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Nouvelle tâche")
        file_menu.add_command(label="Ouvrir")
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.root.quit)
        menubar.add_cascade(label="Fichier", menu=file_menu)

        options_menu = tk.Menu(menubar, tearoff=0)
        options_menu.add_command(label="Paramètres")
        menubar.add_cascade(label="Options", menu=options_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="À propos", command=self.show_about)
        menubar.add_cascade(label="Aide", menu=help_menu)

        self.root.config(menu=menubar)

        welcome_label = tk.Label(
            self.root, text="Bienvenue dans votre logiciel GMAO", font=("Arial", 16)
        )
        welcome_label.pack(expand=True)

    def show_about(self):
        messagebox.showinfo(
            "À propos", "Logiciel GMAO v1.0 - Développé en Python avec Tkinter"
        )


if __name__ == "__main__":
    connection = connect_db("data/database.db")
    initialize_db(connection)

    root = tk.Tk()
    LoginScreen(root, connection, lambda: MainApp(root))
    root.mainloop()
