import tkinter as tk
from data.equipe_queries import get_all_teams


class ListTeamsForm:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH)

        tk.Label(self.frame, text="Liste des équipes", font=("Arial", 16)).pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=50, height=20)
        self.listbox.pack(pady=10)

        self.load_teams()

    def load_teams(self):
        self.listbox.delete(0, tk.END)
        teams = get_all_teams(self.connection)
        for team in teams:
            self.listbox.insert(tk.END, f"{team[1]} - {team[2]} - {team[3]}")
