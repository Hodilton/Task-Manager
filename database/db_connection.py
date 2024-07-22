import sqlite3

from utilities.error_handler import ErrorHandler
from utilities.messages import ErrorMessages, CompleteMessages

class DatabaseConnection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

        self.connect()

    def connect(self):
        if not self.db_path.endswith('.db'):
            ErrorHandler.show_error(ErrorMessages.Database.INVALID_EXTENSION)
            return

        try:
            self.connection = sqlite3.connect(self.db_path)
        except Exception as e:
            ErrorHandler.show_error(ErrorMessages.Database.CONNECTION.format(error=e))
            return

        print(CompleteMessages.Database.CONNECTION.format(path=self.db_path))

    def close(self):
        if self.connection:
            self.connection.close()