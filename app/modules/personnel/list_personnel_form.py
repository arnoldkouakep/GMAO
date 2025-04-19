import tkinter as tk
from data.personnel_queries import get_all_personnel


class ListPersonnelForm:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH)

        tk.Label(self.frame, text="Liste du personnel", font=("Arial", 16)).pack(
            pady=10
        )

        self.listbox = tk.Listbox(self.frame, width=70, height=20)
        self.listbox.pack(pady=10)

        self.load_personnel()

    def load_personnel(self):
        self.listbox.delete(0, tk.END)
        personnel_list = get_all_personnel(self.connection)
        for personnel in personnel_list:
            self.listbox.insert(
                tk.END,
                f"{personnel[1]} - {personnel[2]} - {personnel[3]} - {personnel[4]}",
            )
