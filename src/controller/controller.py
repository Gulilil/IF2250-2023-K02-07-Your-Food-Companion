import os
import sqlite3


class Controller:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "../database/your_food_companion.db")
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    # Getter Element in Tables
    def get_food(self):
        temp = self.cursor.execute("""
        SELECT * 
        FROM food
        """)
        self.conn.commit()
        return temp

    def get_category(self):
        temp = self.cursor.execute("""
        SELECT DISTINCT category 
        FROM food""")
        self.conn.commit()
        return temp
        
    def get_good_food(self):
        temp = self.cursor.execute("""
        SELECT * 
        FROM stored_food NATURAL JOIN food
        WHERE JULIANDAY(stored_food.expiration_date) - JULIANDAY(DATE('now')) > 3
        """)
        self.conn.commit()
        return temp

    def get_stale_food(self):
        temp = self.cursor.execute("""
        SELECT * 
        FROM stored_food NATURAL JOIN food
        WHERE JULIANDAY(stored_food.expiration_date) - JULIANDAY(DATE('now')) <= 3
        """)
        self.conn.commit()
        return temp

    def get_eaten_food(self):
        temp = self.cursor.execute("""
        SELECT * 
        FROM eaten_food NATURAL JOIN food
        """)
        self.conn.commit()
        return temp

    def get_expired_food(self):
        temp = self.cursor.execute("""
        SELECT * 
        FROM expired_food NATURAL JOIN food
        """)
        self.conn.commit()
        return temp

    def get_grocery_food(self):
        temp = self.cursor.execute("""
        SELECT * 
        FROM grocery_food NATURAL JOIN food
        """)
        self.conn.commit()
        return temp

    def get_grocery_food_name(self, name):
        temp = self.cursor.execute("""
        SELECT * 
        FROM grocery_food NATURAL JOIN food
        WHERE name LIKE ?
        """, ("%" + name + "%",))
        self.conn.commit()
        return temp

    def get_grocery_food_prio(self, prio):
        temp = self.cursor.execute("""
        SELECT * 
        FROM grocery_food NATURAL JOIN food
        WHERE priority = ?
        """, (prio,))
        self.conn.commit()
        return temp

    def get_grocery_food_prio_name(self, prio, name):
        temp = self.cursor.execute("""
        SELECT * 
        FROM grocery_food NATURAL JOIN food
        WHERE priority = ? AND name LIKE ?
        """, (prio,"%" + name + "%",))
        self.conn.commit()
        return temp

    def get_grocery_food_cat(self, cat):
        temp = self.cursor.execute("""
        SELECT * 
        FROM grocery_food NATURAL JOIN food
        WHERE category = ?
        """, (cat,))
        self.conn.commit()
        return temp

    def get_grocery_food_cat_name(self, cat, name):
        temp = self.cursor.execute("""
        SELECT * 
        FROM grocery_food NATURAL JOIN food
        WHERE category = ? AND name LIKE ?
        """, (cat,"%" + name + "%",))
        self.conn.commit()
        return temp

    def get_grocery_food_prio_cat(self, prio, cat):
        temp = self.cursor.execute("""
        SELECT * 
        FROM grocery_food NATURAL JOIN food
        WHERE (category = ?) AND (priority = ?)
        """, (cat,prio))
        self.conn.commit()
        return temp

    def get_grocery_food_prio_cat_name(self, prio, cat, name):
        temp = self.cursor.execute("""
        SELECT * 
        FROM grocery_food NATURAL JOIN food
        WHERE (category = ?) AND (priority = ?) AND name LIKE ?
        """, (cat,prio,"%" + name + "%",))
        self.conn.commit()
        return temp

    def get_purchased_food(self):
        temp = self.cursor.execute("""
        SELECT * 
        FROM purchased_food NATURAL JOIN food
        """)
        self.conn.commit()
        return temp

    def get_purchased_food_with_category(self, category):
        temp = self.cursor.execute("""
        SELECT * 
        FROM purchased_food, food
        WHERE purchased_food.id = food.id AND food.category = ?
        """, (category,))
        self.conn.commit()
        return temp

    def get_stored_food(self):
        temp = self.cursor.execute("""
        SELECT * 
        FROM stored_food NATURAL JOIN food
        """)
        self.conn.commit()
        return temp

    # Getter Specific Type of Element
    def get_stored_food_with_category(self, category):
        temp = self.cursor.execute("""
        SELECT * 
        FROM stored_food, food
        WHERE stored_food.id = food.id AND food.category = ?
        """, (category,))
        self.conn.commit()
        return temp

    def get_good_food_with_category(self, category):
        temp = self.cursor.execute("""
        SELECT * 
        FROM stored_food, food
        WHERE stored_food.id = food.id 
        AND food.category = ? 
        AND JULIANDAY(stored_food.expiration_date) - JULIANDAY(DATE('now')) > 3
        """, (category,))
        self.conn.commit()
        return temp

    def get_stale_food_with_category(self, category):
        temp = self.cursor.execute("""
        SELECT * 
        FROM stored_food, food
        WHERE stored_food.id = food.id 
        AND food.category = ? 
        AND JULIANDAY(stored_food.expiration_date) - JULIANDAY(DATE('now')) <= 3
        """, (category,))
        self.conn.commit()
        return temp

    def get_expired_food_with_category(self, category):
        temp = self.cursor.execute("""
        SELECT * 
        FROM expired_food, food
        WHERE expired_food.id = food.id AND food.category = ?
        """, (category,))
        self.conn.commit()
        return temp

    def get_eaten_food_with_category(self, category):
        temp = self.cursor.execute("""
        SELECT * 
        FROM eaten_food, food
        WHERE eaten_food.id = food.id AND food.category = ?
        """, (category,))
        self.conn.commit()
        return temp
    
    def get_eaten_food_count_with_category_this_month(self, category):
        temp = self.cursor.execute(f"""
        SELECT SUM(quantity) AS total_quantity
        FROM eaten_food NATURAL JOIN food
        WHERE category = "{category}" AND
        strftime('%m', eaten_date) = strftime('%m', 'now') AND 
        strftime('%Y', eaten_date) = strftime('%Y', 'now')
        """)
        self.conn.commit()
        return temp

    def get_food_with_category(self, category):
        temp = self.cursor.execute("""
        SELECT * 
        FROM food
        WHERE category = ?
        """, (category,))
        self.conn.commit()
        return temp

    def get_distinct_category(self):
        temp = self.cursor.execute("""
        SELECT DISTINCT category
        FROM food
        """)
        self.conn.commit()
        return temp
    
    def get_category_summary(self, table, category, column, date_column):
        temp = self.cursor.execute(
            f"""
            SELECT 
            strftime('%Y', {date_column}) AS year, 
            strftime('%m', {date_column}) AS month, 
            SUM({column}) AS total
            FROM 
            {table} NATURAL JOIN food
            WHERE
            category = "{category}"
            GROUP BY 
            strftime('%Y-%m', {date_column})
            """
        )
        self.conn.commit()
        return temp

    # Insert
    def insert_food(self, i, name, category):
        self.cursor.execute("""
        INSERT INTO food (id, name, category)
        VALUES (?, ?, ?)
        """, (i, name, category))
        self.conn.commit()

    def insert_stored_food(self, i, quantity, unit, price, expiration_date, storing_location, notes):
        self.cursor.execute("""
        INSERT INTO stored_food (id, quantity, unit, price, expiration_date, storing_location, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (i, quantity, unit, price, expiration_date, storing_location, notes))
        self.conn.commit()

    def insert_grocery_food(self, i, priority):
        self.cursor.execute("""
        INSERT INTO grocery_food (id, priority) 
        VALUES (?, ?)
        """, (i, priority))
        self.conn.commit()

    def insert_expired_food(self, i, quantity, unit, price, expiration_date):
        self.cursor.execute("""
        INSERT INTO expired_food (id, quantity, unit, price, expiration_date)
        VALUES (?, ?, ?, ?, ?)
        """, (i, quantity, unit, price, expiration_date))
        self.conn.commit()

    def insert_eaten_food(self, i, quantity, unit, eaten_date):
        self.cursor.execute("""
        INSERT INTO eaten_food (id, quantity, unit, eaten_date)
        VALUES (?, ?, ?, ?)
        """, (i, quantity, unit, eaten_date))
        self.conn.commit()

    def insert_purchased_food(self, i, quantity, unit, purchase_date):
        self.cursor.execute("""
        INSERT INTO purchased_food (id, quantity, unit, purchase_date)
        VALUES (?, ?, ?, ?)
        """, (i, quantity, unit, purchase_date))
        self.conn.commit()

    # Delete
    def delete_food(self, i):
        self.cursor.execute("""
        DELETE FROM food
        WHERE id = ?
        """, (i,))
        self.conn.commit()

    def delete_stored_food(self, i):
        self.cursor.execute("""
        DELETE FROM stored_food
        WHERE id = ?
        """, (i,))
        self.conn.commit()

    def delete_grocery_food(self, i):
        self.cursor.execute("""
        DELETE FROM grocery_food
        WHERE id = ?
        """, (i,))
        self.conn.commit()

    def delete_purchased_food(self, i):
        self.cursor.execute("""
        DELETE FROM purchased_food
        WHERE id = ?
        """, (i,))
        self.conn.commit()
    
    # Update 
    def update_food(self, i, name, category):
        self.cursor.execute("""
        UPDATE food
        SET 
        name = ?,
        category = ?
        WHERE 
        id = ?
        """, (name, category, i))
        self.conn.commit()

    def update_stored_food(self, i, quantity, unit, price, expiration_date, storing_location, notes):
        self.cursor.execute("""
        UPDATE stored_food 
        SET
        quantity = ?,
        unit = ?,
        price = ?,
        expiration_date = ?,
        storing_location =?,
        notes = ?
        WHERE
        id = ?
        """, (quantity, unit, price, expiration_date, storing_location, notes, i))
        self.conn.commit()


    def move_from_stored_to_expired(self):
        pass

    def move_from_grocery_to_purchased(self):
        pass
