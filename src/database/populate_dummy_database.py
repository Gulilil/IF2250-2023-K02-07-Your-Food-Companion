import os
import sqlite3
import sys

from faker import Faker


def populate_food(cursor: sqlite3.Cursor) -> None:
    # Generate dummy entries using Faker
    fake = Faker()
    categories = ['Junk Food', 'Vegetables', 'Meat', 'Snacks', 'Spices']  # Example categories
    for _ in range(50):  # Generate 50 entries
        name = fake.word()
        category = fake.random_element(elements=categories)
        cursor.execute("INSERT INTO food (name, category) VALUES (?, ?)", (name, category))


def populate_stored_food(cursor: sqlite3.Cursor) -> None:
    # Generate dummy entries using Faker
    fake = Faker()
    unit_choices = ['kg', 'g', 'piece', 'bags', 'ml']  # Example unit choices
    storing_locations = ['Refrigerator', 'Freezer', 'Kitchen Cabinets', 'Shelf']
    for i in range(1, 11):  # Generate 10 entries
        quantity = fake.random_int(min=1, max=20)
        unit = fake.random_element(elements=unit_choices)
        price = fake.random_int(min=5000, max=100000)
        expiration_date = fake.date_between(start_date='+1y', end_date='+2y')
        storing_location = fake.random_element(elements=storing_locations)
        notes = fake.sentence()
        cursor.execute("INSERT INTO stored_food (id, quantity, unit, price, expiration_date, storing_location, "
                       "notes) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (i, quantity, unit, price, expiration_date, storing_location, notes))


def populate_eaten_food(cursor: sqlite3.Cursor) -> None:
    # Generate dummy entries using Faker
    fake = Faker()
    unit_choices = ['kg', 'g', 'piece', 'bags', 'ml']  # Example unit choices
    for i in range(11, 21):  # Generate 10 entries
        quantity = fake.random_int(min=1, max=20)
        unit = fake.random_element(elements=unit_choices)
        eaten_date = fake.date_between(start_date='-2m', end_date='-1m')
        cursor.execute("INSERT INTO eaten_food (id, quantity, unit, eaten_date) VALUES (?, ?, ?, ?)",
                       (i, quantity, unit, eaten_date))


def populate_expired_food(cursor: sqlite3.Cursor) -> None:
    # Generate dummy entries using Faker
    fake = Faker()
    unit_choices = ['kg', 'g', 'piece', 'bags', 'ml']  # Example unit choices
    for i in range(21, 31):  # Generate 10 entries
        quantity = fake.random_int(min=1, max=100)
        unit = fake.random_element(elements=unit_choices)
        price = fake.random_int(min=5000, max=100000)
        expiration_date = fake.date_between(start_date='-1y', end_date='-1m')
        cursor.execute("INSERT INTO expired_food (id, quantity, unit, price, expiration_date) VALUES (?, ?, ?, ?, ?)",
                       (i, quantity, unit, price, expiration_date))


def populate_grocery_food(cursor: sqlite3.Cursor) -> None:
    # Generate dummy entries using Faker
    fake = Faker()
    priority_choices = ['Low', 'Medium', 'High']
    for i in range(31, 41):  # Generate 10 entries
        priority = fake.random_element(elements=priority_choices)
        cursor.execute("INSERT INTO grocery_food (id, priority) VALUES (?, ?)", (i, priority))


def populate_purchased_food(cursor: sqlite3.Cursor) -> None:
    # Generate dummy entries using Faker
    fake = Faker()
    unit_choices = ['kg', 'g', 'piece', 'bags', 'ml']  # Example unit choices
    for i in range(41, 51):  # Generate 10 entries
        quantity = fake.random_int(min=1, max=100)
        unit = fake.random_element(elements=unit_choices)
        purchase_date = fake.date_between(start_date='-3m', end_date='-1m')
        cursor.execute("INSERT INTO purchased_food (id, quantity, unit, purchase_date) VALUES (?, ?, ?, ?)",
                       (i, quantity, unit, purchase_date))


if __name__ == "__main__":
    # If the database doesn't exist, exit the script
    if not os.path.exists("your_food_companion.db"):
        print("Database doesn't exist.")
        sys.exit(1)

    # Connect to the SQLite database
    conn = sqlite3.connect("your_food_companion.db")
    cur = conn.cursor()

    # Enable foreign key support
    conn.execute("PRAGMA foreign_keys = ON")

    # Populate the tables
    populate_food(cur)
    populate_stored_food(cur)
    populate_eaten_food(cur)
    populate_expired_food(cur)
    populate_grocery_food(cur)
    populate_purchased_food(cur)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
