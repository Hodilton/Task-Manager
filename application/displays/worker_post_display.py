import tkinter as tk
from tkinter import messagebox

from .base_display import BaseDisplay

class WorkerPostDisplay(BaseDisplay):
    def __init__(self, parent, db_manager):
        self.db_table = db_manager.tables['worker_post']['instance']
        super().__init__(parent, db_manager)

    def initialize_display(self):
        super().initialize_display()
        self.create_entry()

    def create_entry(self):
        self.entry_label = tk.Label(self.bottom_frame, text="Должность")
        self.entry_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.entry = tk.Entry(self.bottom_frame, width=40)
        self.entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def add_item(self):
        name = self.entry.get().strip()
        if name:
            self.db_table.insert_data((name,))
            self.entry.delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showerror("Ошибка", "Введите название должности")

    def delete_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            id_to_delete = self.listbox.get(selected_index).split(':')[0].strip()
            self.db_table.delete_data(id_to_delete)
            self.update_listbox()
        else:
            messagebox.showerror("Ошибка", "Выберите должность для удаления")

    def update_listbox(self):
        super().update_listbox()

        data = self.db_table.fetch_all_data()

        if not data:
            return

        for row in data:
            display_string = f"{row[0]}: {row[1]}"
            self.listbox.insert(tk.END, display_string)

