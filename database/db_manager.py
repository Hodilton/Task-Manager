import importlib

from utilities.messages import ErrorMessages

class DatabaseManager:
    def __init__(self, connection, tables_config):
        self.db_connection = connection
        self.tables = {}

        self.setup_tables(tables_config)
        self.init_tables()

    def setup_tables(self, tables_config):
        for table_name, module_class_name in tables_config.items():
            try:
                module_name, class_name = module_class_name.rsplit('.', 1)
                module = importlib.import_module(module_name)

                table_class = getattr(module, class_name)
                self.tables[table_name] = {'class': table_class}

            except Exception as e:
                print(ErrorMessages.Database.TABLE_LOADING.format(table_name=table_name, error=e))

    def init_tables(self):
        for table_name, table_data in self.tables.items():

            table_class = table_data['class']
            table_data['instance'] = table_class(self.db_connection.connection)

    def create_tables(self):
        for table_name, table_data in self.tables.items():

            table_instance = table_data['instance']
            table_instance.create_table()
