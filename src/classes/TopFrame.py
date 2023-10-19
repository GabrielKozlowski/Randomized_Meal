from tkinter import *
from PIL import ImageTk, Image

from .RandomMealInfo import RandomMealInfo

class TopFrame:

    def __init__(self):
        print('Helo from init')


    def create_top_label(self):
        """Create Label With Meal Name On Top Frame

        """
        self.random_meal_info = RandomMealInfo().get_random_meal_info()
        self.meal_name = self.random_meal_info[0]

        self.top_label = Label(self, text=self.meal_name.capitalize(), bg='#e6dcdc', font="Arial 18")
        self.top_label.pack(expand=False, fill="both")


    def create_top_meal_photo(self):
        """Create Meal Image On Top Frame
        """
        self.meal_image = self.random_meal_info[1]
        max_height = 400

        self.image = Image.open(self.meal_image)
        pixels_x, pixels_y = tuple([int(max_height/self.image.size[1] * x)  for x in self.image.size])
        self.image.resize((pixels_x, pixels_y))

        self.photo = ImageTk.PhotoImage(self.image.resize((pixels_x, pixels_y)))
        self.top_photo = Label(self, image=self.photo, bg='#e6dcdc')
        self.top_photo.pack(expand=True, fill="both")
