import tkinter as tk
from tkinter import messagebox, ttk

from .base_display import BaseDisplay

class WorkTaskDisplay(BaseDisplay):
    def __init__(self, parent, db_manager):
        self.db_table = db_manager.tables['work_task']['instance']
        super().__init__(parent, db_manager)

    def initialize_display(self):
        super().initialize_display()
        self.create_entries()

    def create_entries(self):
        # Title
        self.title_label = tk.Label(self.bottom_frame, text="Заголовок")
        self.title_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.title_entry = tk.Entry(self.bottom_frame, width=40)
        self.title_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # Start Time
        self.start_time_label = tk.Label(self.bottom_frame, text="Начальное время")
        self.start_time_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.start_time_entry = tk.Entry(self.bottom_frame, width=40)
        self.start_time_entry.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # End Time
        self.end_time_label = tk.Label(self.bottom_frame, text="Конечное время")
        self.end_time_label.grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.end_time_entry = tk.Entry(self.bottom_frame, width=40)
        self.end_time_entry.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # Form Combobox
        self.form_label = tk.Label(self.bottom_frame, text="Форма")
        self.form_label.grid(row=7, column=0, padx=5, pady=5, sticky='w')
        self.form_combobox = ttk.Combobox(self.bottom_frame, state="readonly", width=37)
        self.form_combobox.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.update_combobox()

    def update_combobox(self):
        # Update Form Combobox with formatted names (surname + name + patronymic)
        forms = self.db_manager.tables['form']['instance'].fetch_all_data()
        self.form_combobox['values'] = [f"{form[1]} {form[2]} {form[3]}" for form in forms]

    def add_item(self):
        title = self.title_entry.get().strip()
        start_time = self.start_time_entry.get().strip()
        end_time = self.end_time_entry.get().strip()
        form_name = self.form_combobox.get().strip()  # Получаем выбранный заголовок формы

        if title and start_time and end_time and form_name:
            forms = self.db_manager.tables['form']['instance'].fetch_all_data()
            form_id = next((form[0] for form in forms if f"{form[1]} {form[2]} {form[3]}" == form_name), None)

            if form_id is not None:  # Проверяем, что удалось найти ID формы
                try:
                    self.db_table.insert_data((title, start_time, end_time, form_id))
                    self.update_listbox()
                    messagebox.showinfo("Успешно", "Задача успешно добавлена")
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Ошибка при добавлении задачи: {str(e)}")
            else:
                messagebox.showerror("Ошибка", "Не удалось найти выбранную форму")
        else:
            messagebox.showerror("Ошибка", "Заполните все поля")

    def delete_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            id_to_delete = self.listbox.get(selected_index).split(':')[0].strip()
            self.db_table.delete_data(id_to_delete)
            self.update_listbox()
        else:
            messagebox.showerror("Ошибка", "Выберите запись для удаления")

    def update_listbox(self):
        super().update_listbox()

        data = self.db_table.fetch_all_data()

        if not data:
            return

        for row in data:
            display_string = f"{row[0]}: {row[1]} - {row[2]} - {row[3]} - {row[5]}- {row[6]}- {row[7]}- {row[8]}- {row[9]}- {row[10]}- {row[11]}"
            self.listbox.insert(tk.END, display_string)