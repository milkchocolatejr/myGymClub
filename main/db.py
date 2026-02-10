import sqlite3
from pathlib import Path

conn = None

# This is where we begin our sql database

def init_db():

    print("Initializing database . . .")

    with sqlite3.connect('myGymClub.db') as conn:
        cur = conn.cursor()
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS User_Record (
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            isAdmin INTEGER NOT NULL DEFAULT 0
            );
        """)

        cur.execute("DELETE FROM User_Record;") # Resets the User_Record table each time the app is run for testing purposes
        cur.execute("INSERT INTO User_Record (username, password, isAdmin) VALUES ('admin', 'admin', 1);")
        conn.commit()
        conn.close()

    print("Database initialized successfully!")

def add_user_record(username, password, isAdmin):
    with sqlite3.connect('myGymClub.db') as conn:
        cur = conn.cursor()
        cur.execute(f"INSERT INTO User_Record (username, password, isAdmin) VALUES ('{username}', '{password}', '{isAdmin}');")
        conn.commit()
        conn.close()

