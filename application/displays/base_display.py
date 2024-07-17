import tkinter as tk

class BaseDisplay:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db_manager = db_manager

        self.frame = tk.Frame(self.parent)
        self.initialize_display()
        self.update_listbox()

    def initialize_display(self):
        self.create_top_frame()
        self.create_bottom_frame()
        self.create_buttons()

    def create_top_frame(self):
        self.top_frame = tk.Frame(self.frame)
        self.top_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.listbox = tk.Listbox(self.top_frame, height=15, width=150)
        self.scrollbar = tk.Scrollbar(self.top_frame, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def create_bottom_frame(self):
        self.bottom_frame = tk.Frame(self.frame)
        self.bottom_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def create_buttons(self):
        self.add_button = tk.Button(self.bottom_frame, text="Добавить", command=self.add_item)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(self.bottom_frame, text="Удалить", command=self.delete_item)
        self.delete_button.grid(row=0, column=1, padx=5, pady=5)

    def add_item(self):
        pass

    def delete_item(self):
        pass

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()

    def update_data(self):
        self.update_listbox()
        self.update_combobox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)

    def update_combobox(self):
        pass