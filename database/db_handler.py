from sqlite3 import connect, Error, Cursor


class Database:
    def __init__(self):
        self.connection = connect("schedule_bot.db")
        self.cursor = self.connection.cursor()
    
    def query(self, query: str):
        self.cursor.execute(query)

    def get_result(self):
        return self.cursor.fetchall()

    def get_user(self, user_id):
        self.query(f"Select * from User where user_id='{user_id}'")

    def add_user(self, user_id):
        self.query(f"""
                INSERT INTO User(user_id)
                VALUES("{user_id}");
        """)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()


# def get_user(database: Database() ,user_id: int) -> None:
#     with database as db:
#         db.query(f"Select * from User where user_id='{id}'")
#         print(db.get_result())


# def add_user(database: Database(), user_id, latest_search=None):
#     with database as db:
#         if latest_search == None:
#             db.query(f"""
#                     INSERT INTO User(user_id)
#                     VALUES("{user_id}");
#             """)
#         else:
#             db.query(f"""
#                     INSERT INTO User(user_id, latest_search)
#                     VALUES("{user_id}", "{latest_search}");
#             """)
    