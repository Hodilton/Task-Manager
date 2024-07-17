from .base_table import BaseTable

class WorkTypeTable(BaseTable):
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS work_type (
            Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            TypeName TEXT (60) UNIQUE NOT NULL,
            CHECK(LENGTH(TypeName) > 0)
        );
        '''
        self.connection.execute(query)

    def insert_data(self, data):
        query = '''
           INSERT INTO work_type (TypeName)
           VALUES (?)
           '''
        self.connection.execute(query, data)
        self.connection.commit()

    def update_data(self, id, data):
        query = '''
           UPDATE work_type
           SET TypeName = ?
           WHERE Id = ?
           '''
        self.connection.execute(query, (*data, id))
        self.connection.commit()

    def delete_data(self, id):
        query = '''
           DELETE FROM work_type
           WHERE Id = ?
           '''
        self.connection.execute(query, (id,))
        self.connection.commit()

    def fetch_all_data(self):
        query = '''
        SELECT Id, TypeName 
        FROM work_type
        '''
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
