import tkinter as tk
from tkinter import messagebox, ttk
from .base_display import BaseDisplay

class RoomClassDisplay(BaseDisplay):
    def __init__(self, parent, db_manager):
        self.db_table = db_manager.tables['room_class']['instance']
        self.inputs = {}

        super().__init__(parent, db_manager)

    def initialize_display(self):
        super().initialize_display()
        self.create_entries()

    def create_entries(self):
        self.inputs['class'] = self.create_label_entry("Аудитория", 1)
        self.inputs['place'] = self.create_label_entry("Кол-во мест", 3)

    def create_label_entry(self, label_text, row):
        label = tk.Label(self.bottom_frame, text=label_text)
        label.grid(row=row, column=0, padx=5, pady=5, sticky='w')

        entry = tk.Entry(self.bottom_frame, width=40)
        entry.grid(row=row+1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        return entry

    def add_item(self):
        room = self.inputs['class'].get().strip()
        place = self.inputs['place'].get().strip()

        if room and place:
            self.db_table.insert_data((room,place))
            self.inputs['class'].delete(0, tk.END)
            self.inputs['place'].delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showerror("Ошибка", "Введите название должности")

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
                display_string = f"{row[0]}: {row[1]} - {row[2]}"
                self.listbox.insert(tk.END, display_string)
