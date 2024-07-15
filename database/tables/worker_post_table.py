from .base_table import BaseTable

class WorkerPostTable(BaseTable):
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS worker_post (
            Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            NamePost TEXT (30) UNIQUE NOT NULL,
            CHECK(LENGTH(NamePost) > 0)
        );
        '''
        self.connection.execute(query)

    def insert_data(self, data):
        query = '''
        INSERT INTO worker_post (NamePost)
        VALUES (?)
        '''
        self.connection.execute(query, data)
        self.connection.commit()

    def update_data(self, id, data):
        query = '''
        UPDATE worker_post
        SET NamePost = ?
        WHERE Id = ?
        '''
        self.connection.execute(query, (*data, id))
        self.connection.commit()

    def delete_data(self, id):
        query = '''
        DELETE FROM worker_post
        WHERE Id = ?
        '''
        self.connection.execute(query, (id,))
        self.connection.commit()

    def fetch_all_data(self):
        pass
