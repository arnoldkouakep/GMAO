import tkinter as tk
from tkinter import messagebox
from data.personnel_queries import add_personnel


class AddPersonnelForm:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH)

        tk.Label(
            self.frame, text="Ajouter un nouveau personnel", font=("Arial", 16)
        ).pack(pady=10)

        tk.Label(self.frame, text="Nom:").pack()
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.pack()

        tk.Label(self.frame, text="Poste:").pack()
        self.position_entry = tk.Entry(self.frame)
        self.position_entry.pack()

        tk.Label(self.frame, text="Email:").pack()
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.pack()

        tk.Label(self.frame, text="Mot de passe:").pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()

        tk.Label(self.frame, text="Rôle:").pack()
        self.role_entry = tk.Entry(self.frame)
        self.role_entry.pack()

        tk.Button(self.frame, text="Ajouter", command=self.add_personnel).pack(pady=10)

    def add_personnel(self):
        name = self.name_entry.get()
        position = self.position_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        role = self.role_entry.get()

        if not name or not position or not email or not password or not role:
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
            return

        try:
            add_personnel(self.connection, name, position, email, password, role)
            messagebox.showinfo("Succès", "Personnel ajouté avec succès.")
            self.name_entry.delete(0, tk.END)
            self.position_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.role_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
