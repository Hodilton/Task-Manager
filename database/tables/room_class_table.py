from .base_table import BaseTable

class RoomClassTable(BaseTable):
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS room_class (
            Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            Class INTEGER UNIQUE NOT NULL,
            Place INTEGER NOT NULL,
            CHECK(Class > 0),
            CHECK(Place > 0)
        );
        '''
        self.connection.execute(query)

    def insert_data(self, data):
        query = '''
        INSERT INTO room_class (Class, Place)
        VALUES (?, ?)
        '''
        self.connection.execute(query, data)
        self.connection.commit()

    def update_data(self, id, data):
        query = '''
        UPDATE room_class
        SET Class = ?, Place = ?
        WHERE Id = ?
        '''
        self.connection.execute(query, (*data, id))
        self.connection.commit()

    def delete_data(self, id):
        query = '''
        DELETE FROM room_class
        WHERE Id = ?
        '''
        self.connection.execute(query, (id,))
        self.connection.commit()

    def fetch_all_data(self):
        pass
