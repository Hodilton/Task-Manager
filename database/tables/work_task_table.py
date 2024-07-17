from .base_table import BaseTable

class WorkTaskTable(BaseTable):
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS work_task (
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
           INSERT INTO work_task (Title, StartTime, EndTime, id_form)
           VALUES (?, ?, ?, ?)
           '''
        self.connection.execute(query, data)
        self.connection.commit()

    def update_data(self, id, data):
        query = '''
           UPDATE work_task
           SET Title = ?, StartTime = ?, EndTime = ?, id_form = ?
           WHERE Id = ?
           '''
        self.connection.execute(query, (*data, id))
        self.connection.commit()

    def delete_data(self, id):
        query = '''
           DELETE FROM work_task
           WHERE Id = ?
           '''
        self.connection.execute(query, (id,))
        self.connection.commit()

    def fetch_all_data(self):
        query = '''
               SELECT work_task.Id,
                      work_task.Title,
                      work_task.StartTime,
                      work_task.EndTime,
                      form.Id AS FormId,
                      staff.LastName || ' ' || staff.FirstName || ' ' || staff.MiddleName AS StaffName,
                      worker.LastName || ' ' || worker.FirstName || ' ' || worker.MiddleName AS WorkerName,
                      room_class.Class AS RoomClass,
                      form.Place AS Place,
                      work_type.TypeName,
                      work_status.StatusName,
                      form.Notice
               FROM work_task
               JOIN form ON work_task.id_form = form.Id
               JOIN staff ON form.id_staff = staff.Id
               JOIN worker ON form.id_worker = worker.Id
               JOIN room_class ON form.id_class = room_class.Id
               JOIN work_type ON form.id_work_type = work_type.Id
               JOIN work_status ON form.id_work_status = work_status.Id
               '''
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
