from application.app_main import Application
from database.db_manager import DatabaseManager

if __name__ == '__main__':
    config = {
        'db_path': 'data/my_database1.db',

        'tables': {
            'staff_post': 'database.tables.staff_post_table.StaffPostTable',
            'staff': 'database.tables.staff_table.StaffTable',
            'worker_post': 'database.tables.worker_post_table.WorkerPostTable',
            'worker': 'database.tables.worker_table.WorkerTable'
        },

        'displays': {
            'display_1': {
                'name': 'Сотруднкики - Должности',
                'module': 'application.displays.staff_post_display',
                'class_name': 'StaffPostDisplay'
            },

            'display_2': {
                'name': 'Сотрудники',
                'module': 'application.displays.staff_display',
                'class_name': 'StaffDisplay'
            },

            'display_3': {
                'name': 'Работники - Должности',
                'module': 'application.displays.worker_post_display',
                'class_name': 'WorkerPostDisplay'
            },

            'display_4': {
                'name': 'Работники',
                'module': 'application.displays.worker_display',
                'class_name': 'WorkerDisplay'
            }
        }
    }

    db_manager = DatabaseManager(config['db_path'], config['tables'])
    # db_manager.create_tables()

    try:
        app = Application(config['displays'], db_manager)
    finally:
        db_manager.close_connection()
