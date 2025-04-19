import tkinter as tk
from tkinter import messagebox
from app.modules.personnel.connexion import authenticate_user
from PIL import (
    Image,
    ImageTk,
)  # Nécessite l'installation de Pillow (pip install pillow)


class LoginScreen:
    def __init__(self, root, connection, on_login_success):
        self.root = root
        self.root.title("GMAO - Connexion")
        self.root.geometry("600x400")
        self.connection = connection
        self.on_login_success = on_login_success

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(fill=tk.BOTH, expand=True)

        welcome_label = tk.Label(
            self.login_frame, text="Bienvenue sur GMAO", font=("Arial", 16, "bold")
        )
        welcome_label.pack(pady=10)

        main_container = tk.Frame(self.login_frame)
        main_container.pack(expand=True, fill=tk.BOTH)

        left_frame = tk.Frame(main_container)
        left_frame.pack(side=tk.LEFT, padx=20, pady=20, expand=True)

        logo = Image.open("assets/logo.png").resize((100, 100))
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(left_frame, image=logo)
        self.logo_image = logo
        logo_label.pack()

        right_frame = tk.Frame(main_container)
        right_frame.pack(side=tk.RIGHT, padx=20, pady=20, expand=True)

        tk.Label(right_frame, text="Email:").pack()
        self.email_entry = tk.Entry(right_frame)
        self.email_entry.pack()

        tk.Label(right_frame, text="Mot de passe:").pack()
        self.password_entry = tk.Entry(right_frame, show="*")
        self.password_entry.pack()

        login_button = tk.Button(right_frame, text="Connexion", command=self.login)
        login_button.pack(pady=10)

        # Footer container
        footer_container = tk.Frame(self.root)
        footer_container.pack(side=tk.BOTTOM, fill=tk.X)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        user = authenticate_user(self.connection, email, password)
        if user:
            self.login_frame.destroy()
            self.on_login_success()
        else:
            messagebox.showerror(
                "Erreur", "Nom d'utilisateur ou mot de passe incorrect"
            )
