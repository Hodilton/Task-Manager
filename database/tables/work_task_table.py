# database/task_table.py
from .base_table import BaseTable

class TaskTable(BaseTable):
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS task (
            Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            Title TEXT (100) NOT NULL,
            StartTime TEXT NOT NULL,
            EndTime TEXT NOT NULL,
            id_form INTEGER NOT NULL REFERENCES form (Id),
            CHECK(LENGTH(Title) > 0),
            CHECK(StartTime <= EndTime)
        );
        '''
        self.connection.execute(query)

    def insert_data(self, data):
        query = '''
           INSERT INTO task (Title, StartTime, EndTime, id_form)
           VALUES (?, ?, ?, ?)
           '''
        self.connection.execute(query, data)
        self.connection.commit()

    def update_data(self, id, data):
        query = '''
           UPDATE task
           SET Title = ?, StartTime = ?, EndTime = ?, id_form = ?
           WHERE Id = ?
           '''
        self.connection.execute(query, (*data, id))
        self.connection.commit()

    def delete_data(self, id):
        query = '''
           DELETE FROM task
           WHERE Id = ?
           '''
        self.connection.execute(query, (id,))
        self.connection.commit()

    def fetch_all_data(self):
        pass
