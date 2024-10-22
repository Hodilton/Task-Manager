import tkinter as tk
from tkinter import messagebox, ttk

from .base_display import BaseDisplay


class StaffDisplay(BaseDisplay):
    def __init__(self, parent, db_manager):
        self.db_table = db_manager.tables['staff']['instance']
        self.db_manager = db_manager
        super().__init__(parent, db_manager)

    def initialize_display(self):
        super().initialize_display()
        self.create_entries()

    def create_entries(self):
        # Last Name
        self.lastname_label = tk.Label(self.bottom_frame, text="Фамилия")
        self.lastname_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.lastname_entry = tk.Entry(self.bottom_frame, width=40)
        self.lastname_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # First Name
        self.firstname_label = tk.Label(self.bottom_frame, text="Имя")
        self.firstname_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.firstname_entry = tk.Entry(self.bottom_frame, width=40)
        self.firstname_entry.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # Middle Name
        self.middlename_label = tk.Label(self.bottom_frame, text="Отчество")
        self.middlename_label.grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.middlename_entry = tk.Entry(self.bottom_frame, width=40)
        self.middlename_entry.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # Staff Post (Dropdown)
        self.staffpost_label = tk.Label(self.bottom_frame, text="Должность")
        self.staffpost_label.grid(row=7, column=0, padx=5, pady=5, sticky='w')
        self.staffpost_combobox = ttk.Combobox(self.bottom_frame, state="readonly", width=37)
        self.staffpost_combobox.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.update_combobox()

    def update_combobox(self):
        staff_posts = self.db_manager.tables['staff_post']['instance'].fetch_all_data()
        self.staffpost_combobox['values'] = [post[1] for post in staff_posts]

    def add_item(self):
        lastname = self.lastname_entry.get().strip()
        firstname = self.firstname_entry.get().strip()
        middlename = self.middlename_entry.get().strip()
        staff_post_name = self.staffpost_combobox.get().strip()

        if lastname and firstname and middlename and staff_post_name:
            staff_posts = self.db_manager.tables['staff_post']['instance'].fetch_all_data()
            staff_post_id = next((post[0] for post in staff_posts if post[1] == staff_post_name), None)

            if staff_post_id:
                self.db_table.insert_data((lastname, firstname, middlename, staff_post_id))
                self.lastname_entry.delete(0, tk.END)
                self.firstname_entry.delete(0, tk.END)
                self.middlename_entry.delete(0, tk.END)
                self.staffpost_combobox.set('')
                self.update_listbox()
            else:
                messagebox.showerror("Ошибка", "Выбранная должность не найдена")
        else:
            messagebox.showerror("Ошибка", "Заполните все поля")

    def delete_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            id_to_delete = self.listbox.get(selected_index).split(':')[0].strip()
            self.db_table.delete_data(id_to_delete)
            self.update_listbox()
        else:
            messagebox.showerror("Ошибка", "Выберите сотрудника для удаления")

    def update_listbox(self):
        super().update_listbox()

        data = self.db_table.fetch_all_data()

        if not data:
            return

        for row in data:
            display_string = f"{row[0]}: {row[1]} {row[2]} {row[3]} - {row[4]}"
            self.listbox.insert(tk.END, display_string)