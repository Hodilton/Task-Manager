from .base_table import BaseTable

class StaffTable(BaseTable):
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS staff (
            Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            LastName TEXT (30) NOT NULL,
            FirstName TEXT (30) NOT NULL,
            MiddleName TEXT (30) NOT NULL,
            id_staff_post INTEGER NOT NULL REFERENCES staff_post (Id),
            CHECK(LENGTH(LastName) > 0),
            CHECK(LENGTH(FirstName) > 0),
            CHECK(LENGTH(MiddleName) > 0)
        );
        '''
        self.connection.execute(query)

    def insert_data(self, data):
        query = '''
        INSERT INTO staff (LastName, FirstName, MiddleName, id_staff_post)
        VALUES (?, ?, ?, ?)
        '''
        self.connection.execute(query, data)
        self.connection.commit()

    def update_data(self, id, data):
        query = '''
        UPDATE staff
        SET LastName = ?, FirstName = ?, MiddleName = ?, id_staff_post = ?
        WHERE Id = ?
        '''
        self.connection.execute(query, (*data, id))
        self.connection.commit()

    def delete_data(self, id):
        query = '''
        DELETE FROM staff
        WHERE Id = ?
        '''
        self.connection.execute(query, (id,))
        self.connection.commit()

    def fetch_all_data(self):
        query = '''
        SELECT staff.Id, LastName, FirstName, MiddleName, NamePost 
        FROM staff 
        JOIN staff_post ON staff.id_staff_post = staff_post.Id
        '''
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
