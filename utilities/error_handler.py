import tkinter as tk
from tkinter import messagebox


class ErrorHandler:
    @staticmethod
    def show_error(message):
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", message)
        root.destroy()