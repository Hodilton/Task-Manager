# database/task_table.py
from .base_table import BaseTable

class WorkTaskTable(BaseTable):
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
        query = '''
               SELECT task.Id,
                      task.Title,
                      task.StartTime,
                      task.EndTime,
                      form.Id AS FormId,
                      staff.LastName || ' ' || staff.FirstName || ' ' || staff.MiddleName AS StaffName,
                      worker.LastName || ' ' || worker.FirstName || ' ' || worker.MiddleName AS WorkerName,
                      room_class.Class AS RoomClass,
                      form.Place AS Place,
                      work_type.Name_work,
                      work_status.Name_status,
                      form.Notice
               FROM task
               JOIN form ON task.id_form = form.Id
               JOIN staff ON form.id_staff = staff.Id
               JOIN worker ON form.id_worker = worker.Id
               JOIN room_class ON form.id_class = room_class.Id
               JOIN work_type ON form.id_work_type = work_type.Id
               JOIN work_status ON form.id_work_status = work_status.Id
               '''
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
