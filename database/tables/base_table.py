class BaseTable:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        raise NotImplementedError("Subclasses should implement this method!")

    def insert_data(self, data):
        raise NotImplementedError("Subclasses should implement this method!")

    def update_data(self, id, data):
        raise NotImplementedError("Subclasses should implement this method!")

    def delete_data(self, id):
        raise NotImplementedError("Subclasses should implement this method!")

    def fetch_all_data(self):
        raise NotImplementedError("Subclasses should implement this method!")
