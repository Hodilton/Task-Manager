import tkinter as tk

from application.app_gui import ApplicationGUI
from utilities.error_handler import ErrorHandler

class Application:
    def __init__(self, config, db_manager):
        try:
            self.root = tk.Tk()
            self.root.title("Manager")
            self.db_manager = db_manager

            self.initialize_application(config)
            self.root.mainloop()

        except Exception as e:
            ErrorHandler.show_error(str(e))

    def initialize_application(self, config):
        self.gui = ApplicationGUI(self.root, config, self.db_manager)
