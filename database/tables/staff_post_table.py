from .base_table import BaseTable

class StaffPostTable(BaseTable):
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS staff_post (
            Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            NamePost TEXT (30) UNIQUE NOT NULL,
            CHECK(LENGTH(NamePost) > 0)
        );
        '''
        self.connection.execute(query)

    def insert_data(self, data):
        query = '''
        INSERT INTO staff_post (NamePost)
        VALUES (?)
        '''
        self.connection.execute(query, data)
        self.connection.commit()

    def update_data(self, id, data):
        query = '''
        UPDATE staff_post
        SET NamePost = ?
        WHERE Id = ?
        '''
        self.connection.execute(query, (*data, id))
        self.connection.commit()

    def delete_data(self, id):
        query = '''
        DELETE FROM staff_post
        WHERE Id = ?
        '''
        self.connection.execute(query, (id,))
        self.connection.commit()

    def fetch_all_data(self):
        query = '''
           SELECT Id, NamePost FROM staff_post
           '''
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
