from .base_table import BaseTable

class WorkStatusTable(BaseTable):
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS work_status (
            Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            StatusName TEXT (60) UNIQUE NOT NULL,
            CHECK(LENGTH(StatusName) > 0)
        );
        '''
        self.connection.execute(query)

    def insert_data(self, data):
        query = '''
           INSERT INTO work_status (StatusName)
           VALUES (?)
           '''
        self.connection.execute(query, data)
        self.connection.commit()

    def update_data(self, id, data):
        query = '''
           UPDATE work_status
           SET StatusName = ?
           WHERE Id = ?
           '''
        self.connection.execute(query, (*data, id))
        self.connection.commit()

    def delete_data(self, id):
        query = '''
           DELETE 
           FROM work_status
           WHERE Id = ?
           '''
        self.connection.execute(query, (id,))
        self.connection.commit()

    def fetch_all_data(self):
        query = '''
        SELECT Id, StatusName 
        FROM work_status
        '''
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
