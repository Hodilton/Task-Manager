class ErrorMessages:
    class Database:
        INVALID_EXTENSION = "Invalid database file extension.\nPlease provide a valid SQLite database file."
        CONNECTION = "Error connecting to SQLite database: {error}."
        TABLE_LOADING = "Error loading table {table_name}: {error}"
        DISPLAY_LOADING = "Error loading display {display_name}: {error}"

class CompleteMessages:
    class Database:
        CONNECTION = "Connected to SQLite database at {path}."