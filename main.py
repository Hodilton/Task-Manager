from application.app_main import Application
from database.db_manager import DatabaseManager

if __name__ == '__main__':
    config = {
        'db_path': 'data/my_database2.db',

        'tables': {
            'staff_post': 'database.tables.staff_post_table.StaffPostTable',
            'staff': 'database.tables.staff_table.StaffTable'
        },

        'displays': {
            'display_1': {
                'name': 'Display 1',
                'module': 'application.displays.staff_post_display',
                'class_name': 'StaffPostDisplay'
            },
            'display_2': {
                'name': 'Display 2',
                'module': 'application.displays.staff_display',
                'class_name': 'StaffDisplay'
            }
        }
    }

    db_manager = DatabaseManager(config['db_path'], config['tables'])
    # db_manager.create_tables()

    try:
        app = Application(config['displays'], db_manager)
    finally:
        db_manager.close_connection()
