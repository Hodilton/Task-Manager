import tkinter as tk

from application.app_gui import ApplicationGUI


class Application:
    def __init__(self, config, db_manager):
        self.root = tk.Tk()
        self.root.title("Manager")
        self.db_manager = db_manager

        self.initialize_application(config)

    def initialize_application(self, config):
        self.gui = ApplicationGUI(self.root, config, self.db_manager)
        self.root.mainloop()