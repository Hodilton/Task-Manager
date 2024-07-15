import tkinter as tk
from tkinter import messagebox, ttk

from .base_display import BaseDisplay

class FormDisplay(BaseDisplay):
    def __init__(self, parent, db_manager):
        self.db_table = db_manager.tables['form']['instance']
        self.db_manager = db_manager
        super().__init__(parent, db_manager)

    def initialize_display(self):
        super().initialize_display()
        self.create_entries()

    def create_entries(self):
        # Staff
        self.staff_label = tk.Label(self.bottom_frame, text="Сотрудник")
        self.staff_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.staff_combobox = ttk.Combobox(self.bottom_frame, state="readonly", width=37)
        self.staff_combobox.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # Worker
        self.worker_label = tk.Label(self.bottom_frame, text="Рабочий")
        self.worker_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.worker_combobox = ttk.Combobox(self.bottom_frame, state="readonly", width=37)
        self.worker_combobox.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # Room Class
        self.class_label = tk.Label(self.bottom_frame, text="Класс")
        self.class_label.grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.class_combobox = ttk.Combobox(self.bottom_frame, state="readonly", width=37)
        self.class_combobox.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        self.class_combobox.bind("<<ComboboxSelected>>", self.update_places_combobox)

        # Place
        self.place_label = tk.Label(self.bottom_frame, text="Место")
        self.place_label.grid(row=7, column=0, padx=5, pady=5, sticky='w')
        self.place_combobox = ttk.Combobox(self.bottom_frame, state="readonly", width=37)
        self.place_combobox.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # Work Type
        self.work_type_label = tk.Label(self.bottom_frame, text="Тип работы")
        self.work_type_label.grid(row=9, column=0, padx=5, pady=5, sticky='w')
        self.work_type_combobox = ttk.Combobox(self.bottom_frame, state="readonly", width=37)
        self.work_type_combobox.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # Work Status
        self.work_status_label = tk.Label(self.bottom_frame, text="Статус работы")
        self.work_status_label.grid(row=11, column=0, padx=5, pady=5, sticky='w')
        self.work_status_combobox = ttk.Combobox(self.bottom_frame, state="readonly", width=37)
        self.work_status_combobox.grid(row=12, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # Notice
        self.notice_label = tk.Label(self.bottom_frame, text="Примечание")
        self.notice_label.grid(row=13, column=0, padx=5, pady=5, sticky='w')
        self.notice_entry = tk.Entry(self.bottom_frame, width=40)
        self.notice_entry.grid(row=14, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.update_combobox()

    def update_combobox(self):
        # Update Staff Combobox
        staffs = self.db_manager.tables['staff']['instance'].fetch_all_data()
        self.staff_combobox['values'] = [f"{staff[1]} {staff[2]} {staff[3]}" for staff in staffs]

        # Update Worker Combobox
        workers = self.db_manager.tables['worker']['instance'].fetch_all_data()
        self.worker_combobox['values'] = [f"{worker[1]} {worker[2]} {worker[3]}" for worker in workers]

        # Update Room Class Combobox
        room_classes = self.db_manager.tables['room_class']['instance'].fetch_all_data()
        self.class_combobox['values'] = [room_class[1] for room_class in room_classes]

        # Update Work Type Combobox
        work_types = self.db_manager.tables['work_type']['instance'].fetch_all_data()
        self.work_type_combobox['values'] = [work_type[1] for work_type in work_types]

        # Update Work Status Combobox
        work_statuses = self.db_manager.tables['work_status']['instance'].fetch_all_data()
        self.work_status_combobox['values'] = [work_status[1] for work_status in work_statuses]

    def update_places_combobox(self, event):
        selected_class = self.class_combobox.get()
        room_classes = self.db_manager.tables['room_class']['instance'].fetch_all_data()
        selected_class_data = next((cls for cls in room_classes if cls[1] == int(selected_class)), None)

        if selected_class_data:
            places = list(range(1, selected_class_data[2] + 1))
            self.place_combobox['values'] = places

    def add_item(self):
        staff_name = self.staff_combobox.get().strip()
        worker_name = self.worker_combobox.get().strip()
        room_class = self.class_combobox.get().strip()
        place = self.place_combobox.get().strip()
        work_type_name = self.work_type_combobox.get().strip()
        work_status_name = self.work_status_combobox.get().strip()
        notice = self.notice_entry.get().strip()

        if staff_name and worker_name and room_class and place and work_type_name and work_status_name:
            staffs = self.db_manager.tables['staff']['instance'].fetch_all_data()
            staff_id = next((staff[0] for staff in staffs if f"{staff[1]} {staff[2]} {staff[3]}" == staff_name), None)

            workers = self.db_manager.tables['worker']['instance'].fetch_all_data()
            worker_id = next((worker[0] for worker in workers if f"{worker[1]} {worker[2]} {worker[3]}" == worker_name), None)

            room_classes = self.db_manager.tables['room_class']['instance'].fetch_all_data()
            class_id = next((cls[0] for cls in room_classes if cls[1] == int(room_class)), None)

            work_types = self.db_manager.tables['work_type']['instance'].fetch_all_data()
            work_type_id = next((wt[0] for wt in work_types if wt[1] == work_type_name), None)

            work_statuses = self.db_manager.tables['work_status']['instance'].fetch_all_data()
            work_status_id = next((ws[0] for ws in work_statuses if ws[1] == work_status_name), None)

            if all([staff_id, worker_id, class_id, place, work_type_id, work_status_id]):
                self.db_table.insert_data((staff_id, worker_id, class_id, place, work_type_id, work_status_id, notice))
                self.update_listbox()
            else:
                messagebox.showerror("Ошибка", "Не удалось найти одну из выбранных сущностей")
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
            display_string = f"{row[0]}: {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]} - {row[6]} - {row[7]}"
            self.listbox.insert(tk.END, display_string)

