import sqlite3
from pathlib import Path


conn = None

# This is where we begin our sql database

def init_db():

    print("Initializing database . . .")

    with sqlite3.connect('myGymClub.db') as conn: # closes the connection automatically when done
        cur = conn.cursor()
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS User_Records (
            username TEXT NOT NULL UNIQUE PRIMARY KEY,
            password TEXT NOT NULL,
            isAdmin INTEGER NOT NULL DEFAULT 0,
            experience INTEGER NOT NULL DEFAULT 0
            );
                          
            CREATE TABLE IF NOT EXISTS Goals (
            username TEXT NOT NULL PRIMARY KEY,
            exercise_name TEXT NOT NULL,
            style TEXT NOT NULL CHECK (style IN ('progress', 'habitual')),
            reps INTEGER,
            rep_type TEXT CHECK (rep_type IN ('miles', 'minutes')),
            sets INTEGER,
            frequency INTEGER NOT NULL,
            freq_type TEXT NOT NULL CHECK (freq_type IN ('day', 'week', 'month')),
            memo TEXT
            );                          
        """)

        cur.execute("DELETE FROM User_Records") # Resets the User_Records table each time the app is run for testing purposes
        cur.execute("DELETE FROM Goals") # Resets the Goals table each time the app is run for testing purposes
        add_user_record(conn, "admin", "admin", 1,0) # Adds a default admin user for testing purposes
        add_goal(conn, "admin", "Endurance Run", "habitual", None, "miles", None, 4, "week", "Do not stop, keep going !!!!") # Adds a default goal for testing purposes

    print("Database initialized successfully!")

def add_user_record(conn, username, password, isAdmin, experience):
        cur = conn.cursor()
        cur.execute(f"INSERT INTO User_Records (username, password, isAdmin, experience) VALUES ('{username}', '{password}', '{isAdmin}', '{experience}');")
        conn.commit()

def add_goal(conn, username, exercise_name, style, reps, rep_type, sets, frequency, freq_type, memo):
        cur = conn.cursor()
        cur.execute(f"INSERT INTO Goals (username, exercise_name, style, reps, rep_type, sets, frequency, freq_type, memo) VALUES ('{username}', '{exercise_name}', '{style}', '{reps}', '{rep_type}', '{sets}', '{frequency}', '{freq_type}', '{memo}');")
        conn.commit()

