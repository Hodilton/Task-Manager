import tkinter as tk
from tkinter import messagebox, ttk
from .base_display import BaseDisplay

class WorkerDisplay(BaseDisplay):
    def __init__(self, parent, db_manager):
        self.db_table = db_manager.tables['worker']['instance']
        self.inputs = {}

        super().__init__(parent, db_manager)

    def initialize_display(self):
        super().initialize_display()
        self.create_entries()

    def create_entries(self):
        self.inputs['lastname'] = self.create_label_entry("Фамилия", 1)
        self.inputs['firstname'] = self.create_label_entry("Имя", 3)
        self.inputs['middlename'] = self.create_label_entry("Отчество", 5)
        self.inputs['workerpost'] = self.create_combobox("Должность", 7)

    def create_label_entry(self, label_text, row):
        label = tk.Label(self.bottom_frame, text=label_text)
        label.grid(row=row, column=0, padx=5, pady=5, sticky='w')

        entry = tk.Entry(self.bottom_frame, width=40)
        entry.grid(row=row+1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        return entry

    def create_combobox(self, label_text, row):
        label = tk.Label(self.bottom_frame, text=label_text)
        label.grid(row=row, column=0, padx=5, pady=5, sticky='w')

        combobox = ttk.Combobox(self.bottom_frame, state="readonly", width=37)
        combobox.grid(row=row+1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.update_combobox(combobox)
        return combobox

    def update_combobox(self, combobox):
        worker_posts = self.db_manager.tables['worker_post']['instance'].fetch_all_data()
        combobox['values'] = [post[1] for post in worker_posts]

    def add_item(self):
        lastname = self.inputs['lastname'].get().strip()
        firstname = self.inputs['firstname'].get().strip()
        middlename = self.inputs['middlename'].get().strip()
        worker_post_name = self.inputs['workerpost'].get().strip()

        if lastname and firstname and middlename and worker_post_name:
            worker_posts = self.db_manager.tables['worker_post']['instance'].fetch_all_data()
            worker_post_id = next((post[0] for post in worker_posts if post[1] == worker_post_name), None)

            if worker_post_id:
                self.db_table.insert_data((lastname, firstname, middlename, worker_post_id))
                self.clear_entries()
                self.update_listbox()
            else:
                messagebox.showerror("Ошибка", "Выбранная должность не найдена")
        else:
            messagebox.showerror("Ошибка", "Заполните все поля")

    def clear_entries(self):
        for input_widget in self.inputs.values():
            if isinstance(input_widget, tk.Entry):
                input_widget.delete(0, tk.END)
            elif isinstance(input_widget, ttk.Combobox):
                input_widget.set('')

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

        if data:
            for row in data:
                display_string = f"{row[0]}: {row[1]} {row[2]} {row[3]} - {row[4]}"
                self.listbox.insert(tk.END, display_string)
