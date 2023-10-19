


class Meals:

    def __init__(self, name:str, type_of_meal:str, calories:int, soup:bool, quantity:int, ingredients:list, recipe:str):

        self.name = name
        self.type_of_meal = type_of_meal       
        self.calories = calories
        self.soup: soup
        self.quantity = quantity        
        self.ingredients = ingredients
        self.recipe = recipe



    def __str__(self):
        return f"Dish name {self.name}, Type: {self.type_of_meal}, calories: {self.calories}, for {self.quantity} people."
    

    def add_dish(self):
        meals_data = {
            self.name: {
                "Type of meal": self.type_of_meal,
                "Calories": self.calories,
                "Soup": self.soup,
                "Quantity": self.quantity,
                "Ingredients": self.ingredients,
                "Recipe": self.recipe
            }
        }
        return meals_data



    def get_all_dishes(self):
        pass