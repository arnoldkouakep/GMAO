import tkinter as tk
from tkinter import messagebox
from data.equipe_queries import add_team


class AddTeamForm:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH)

        tk.Label(
            self.frame, text="Ajouter une nouvelle équipe", font=("Arial", 16)
        ).pack(pady=10)

        tk.Label(self.frame, text="Nom de l'équipe:").pack()
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.pack()

        tk.Label(self.frame, text="Shift (Matin/Soir):").pack()
        self.shift_entry = tk.Entry(self.frame)
        self.shift_entry.pack()

        tk.Label(self.frame, text="Jour de la semaine:").pack()
        self.day_entry = tk.Entry(self.frame)
        self.day_entry.pack()

        tk.Button(self.frame, text="Ajouter", command=self.add_team).pack(pady=10)

    def add_team(self):
        name = self.name_entry.get()
        shift = self.shift_entry.get()
        day = self.day_entry.get()

        if not name or not shift or not day:
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
            return

        try:
            add_team(self.connection, name, shift, day)
            messagebox.showinfo("Succès", "Équipe ajoutée avec succès.")
            self.name_entry.delete(0, tk.END)
            self.shift_entry.delete(0, tk.END)
            self.day_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
