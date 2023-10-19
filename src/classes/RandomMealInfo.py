from random import choice
from os import listdir

class RandomMealInfo:

    def __init__(self):

        self.path = "./static/images/meals/"
        self.files = listdir(self.path)
        self.photos_info = dict()

        for file in self.files:
            self.photos = self.path + file
            self.photo_name = file.split('.')
            self.photos_info[self.photo_name[0]] = self.photos


    def get_random_meal_info(self):
        """Randomly choice meal info from meals list

        Returns:
            dict: return name of meal and path to meal photo
        """
        self.meal_name = choice(list(self.photos_info.keys()))
        return [self.meal_name, self.photos_info[self.meal_name]]

