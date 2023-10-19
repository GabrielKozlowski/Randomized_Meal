import sqlite3


class Database:

    def __init__(self, meal_data):
        # Create Database
        self.connect = sqlite3.connect('randomize_meals.db')

        # Create Cursor
        self.cursor = self.connect.cursor()

        # Create Table
        self.cursor.execute(
        """CREATE TABLE meals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(120) NOT NULL,
        type_of_meal VARCHAR(20) NOT NULL,
        calories INTEGER,
        soup BOOLEAN NOT NULL,
        quantity INTEGER DEFAULT 1,
        ingredients JSON DEFAULT('[]'),
        recipe VARCHAR(500)
        )""")



        self.meal_data = meal_data
        

    def add_to_database(self):
        self.cursor.execute(
        f"""INSERT INTO meals(id, name, type_of_meal, calories, soup, quantity, ingredients, recipe) VALUES(
        None,{self.meal_data},
        )
        """
        )



Database('sds')