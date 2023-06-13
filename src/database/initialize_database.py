import os
import sqlite3


def initialize_database() -> None:
    # If the database is already initialized, do not create a new one
    if os.path.exists("your_food_companion.db"):
        return

    # Connect to the SQLite database
    conn = sqlite3.connect("your_food_companion.db")
    cursor = conn.cursor()

    # Enable foreign key support
    conn.execute("PRAGMA foreign_keys = ON")

    # Create the food table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS food (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT
        )
        """)

    # Create the stored_food table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stored_food (
        id INTEGER PRIMARY KEY,
        quantity INTEGER,
        unit TEXT,
        price INTEGER,
        expiration_date TEXT,
        storing_location TEXT,
        notes TEXT,
        FOREIGN KEY (id) REFERENCES food(id)
        )
        """)

    # Create the eaten_food table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS eaten_food (
        id INTEGER PRIMARY KEY,
        quantity INTEGER,
        unit TEXT,
        eaten_date TEXT,
        FOREIGN KEY (id) REFERENCES food(id)
        )
        """)

    # Create the expired_food table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expired_food (
        id INTEGER PRIMARY KEY,
        quantity INTEGER,
        unit TEXT,
        price INTEGER,
        expiration_date TEXT,
        FOREIGN KEY (id) REFERENCES food(id)
        )
        """)

    # Create the grocery_food table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grocery_food (
        id INTEGER PRIMARY KEY,
        priority TEXT,
        FOREIGN KEY (id) REFERENCES food(id)
        )
        """)

    # Create the purchased_food table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchased_food (
        id INTEGER PRIMARY KEY,
        quantity INTEGER,
        unit TEXT,
        purchase_date TEXT,
        FOREIGN KEY (id) REFERENCES food(id)
        )
        """)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    initialize_database()
