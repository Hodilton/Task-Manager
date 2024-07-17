from .base_table import BaseTable

class FormTable(BaseTable):
    def create_table(self):
        query = '''
                CREATE TABLE IF NOT EXISTS form (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    id_staff INTEGER NOT NULL REFERENCES staff (Id),
                    id_worker INTEGER NOT NULL REFERENCES worker (Id),
                    id_class INTEGER NOT NULL REFERENCES room_class (Id),
                    Place INTEGER NOT NULL,
                    id_work_type INTEGER NOT NULL REFERENCES work_type (Id),
                    id_work_status INTEGER NOT NULL REFERENCES work_status (Id),
                    Notice TEXT (500),
                    CHECK(id_staff > 0),
                    CHECK(id_worker > 0),
                    CHECK(id_class > 0),
                    CHECK(Place > 0),
                    CHECK(id_work_type > 0),
                    CHECK(id_work_status > 0)
                );
                '''
        self.connection.execute(query)

    def insert_data(self, data):
        query = '''
                INSERT INTO form (id_staff, id_worker, id_class, Place, id_work_type, id_work_status, Notice)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                '''
        self.connection.execute(query, data)
        self.connection.commit()

    def update_data(self, id, data):
        query = '''
                UPDATE form
                SET id_staff = ?, id_worker = ?, id_class = ?, Place = ?, id_work_type = ?, id_work_status = ?, Notice = ?
                WHERE Id = ?
                '''
        self.connection.execute(query, (*data, id))
        self.connection.commit()

    def delete_data(self, id):
        query = '''
               DELETE FROM form
               WHERE Id = ?
               '''
        self.connection.execute(query, (id,))
        self.connection.commit()

    def fetch_all_data(self):
        query = '''
               SELECT form.Id,
                      staff.LastName || ' ' || staff.FirstName || ' ' || staff.MiddleName AS StaffName,
                      worker.LastName || ' ' || worker.FirstName || ' ' || worker.MiddleName AS WorkerName,
                      room_class.Class AS RoomClass,
                      form.Place AS Place,
                      work_type.TypeName,
                      work_status.StatusName,
                      form.Notice
               FROM form
               JOIN staff ON form.id_staff = staff.Id
               JOIN worker ON form.id_worker = worker.Id
               JOIN room_class ON form.id_class = room_class.Id
               JOIN work_type ON form.id_work_type = work_type.Id
               JOIN work_status ON form.id_work_status = work_status.Id
               '''
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
