import sqlite3
import importlib

class DatabaseManager:
    def __init__(self, db_path, tables_config):
        self.db_path = db_path
        self.tables = {}
        self.connection = sqlite3.connect(self.db_path)

        self.setup_connection()
        self.setup_tables(tables_config)
        self.init_tables()

    def setup_connection(self):
        if not self.db_path.endswith('.db'):
            print("Invalid database file extension. Please provide a valid SQLite database file.")
            return

        if not sqlite3.sqlite_version:
            print("SQLite is not installed.")
            return

        try:
            self.connection = sqlite3.connect(self.db_path)
            print(f"Connected to SQLite database at {self.db_path}")
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite database: {e}")

    def setup_tables(self, tables_config):
        for table_name, module_class_name in tables_config.items():
            try:
                module_name, class_name = module_class_name.rsplit('.', 1)
                module = importlib.import_module(module_name)
                table_class = getattr(module, class_name)
                self.tables[table_name] = {'class': table_class}

            except (ValueError, ImportError, AttributeError) as e:
                print(f"Error loading table {table_name}: {e}")

    def init_tables(self):
        for table_name, table_data in self.tables.items():
            table_class = table_data['class']
            table_data['instance'] = table_class(self.connection)

    def create_tables(self):
        for table_name, table_data in self.tables.items():
            table_instance = table_data['instance']
            table_instance.create_table()

    def close_connection(self):
        self.connection.close()


    def create_indexes(self):
        indexes = [
            "CREATE INDEX IF NOT EXISTS idx_form_id_staff ON form(id_staff);",
            "CREATE INDEX IF NOT EXISTS idx_form_id_worker ON form(id_worker);",
            "CREATE INDEX IF NOT EXISTS idx_form_id_class ON form(id_class);",
            "CREATE INDEX IF NOT EXISTS idx_form_id_work_type ON form(id_work_type);",
            "CREATE INDEX IF NOT EXISTS idx_form_id_work_status ON form(id_work_status);"
        ]

        for index in indexes:
            self.connection.execute(index)
        self.connection.commit()