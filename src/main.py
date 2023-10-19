from tkinter import *
from classes.TopFrame import TopFrame
from classes.LeftFrame import LeftFrame



class RandomizeMeals:

    def __init__(self):
        # Create App Window
        self.app = Tk()
        
        # Set App Icon, title, max and min width/height
        self.app.iconbitmap("./static/images/icon.ico")
        self.app.title('Randomize Meals')
        self.app.maxsize(700, 900)
        self.app.minsize(700, 900)


        # Frames Initialize 
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        self.bottom_left_frame = self.create_bottom_left_frame()

        # App Run Function
        self.run_app()


    # Create Top Frame
    def create_top_frame(self):
        self.top_frame = Frame(self.app, bg="#cf6f0e")
        self.top_frame.pack(side=TOP, fill='both')

        # Create Label and Image For Top Frame With TopFrame Class
        TopFrame.create_top_label(self.top_frame)
        TopFrame.create_top_meal_photo(self.top_frame)
        return self.top_frame


    # Create Bottom Frame
    def create_bottom_frame(self):
        self.bottom_frame = Frame(self.app, bg="#e6dcdc")
        self.bottom_frame.pack(fill='both', expand=True, side=BOTTOM)
        return self.bottom_frame


    # Create Left Site Of Bottom Frame
    def create_bottom_left_frame(self):


        self.bottom_left = LeftFrame.create_left_label(self.bottom_frame)
        self.bottom_left = Frame(self.bottom_frame, bg="#cf6f0e")
        self.bottom_left.grid()


        self.bottom_left.columnconfigure(0, minsize=350, weight=1)
    

        random_meal_button = Button(self.bottom_left, width=16, text='Random Meal',font="Arial 11", command=self.refresh)
        random_meal_button.grid(column=0, row=0, pady=14)

        meals_list_button = Button(self.bottom_left, width=16, text='Meals List',font="Arial 11", command=self.show_meals_list)
        meals_list_button.grid(column=0, row=1, pady=14)
        
        add_meal_to_list_button = Button(self.bottom_left, width=16, text='Add Meal To List',font="Arial 11", command=self.add_meal_to_list)
        add_meal_to_list_button.grid(column=0, row=2, pady=14)

        delete_meal_from_list_button = Button(self.bottom_left, width=16, text='Delete Meal In List',font="Arial 11", command=self.delete_meal_from_list)
        delete_meal_from_list_button.grid(column=0, row=3, pady=14)    

        edit_meal_button = Button(self.bottom_left, width=16, text='Edit Meal',font="Arial 11", command=self.edit_meal)
        edit_meal_button.grid(column=0, row=4, pady=14)

        show_shopping_list_button = Button(self.bottom_left, width=16, text='Shopping List',font="Arial 11", command=self.show_shopping_list_button)
        show_shopping_list_button.grid(column=0, row=5, pady=14)

        exit_button = Button(self.bottom_left, width=16, text='Exit',font="Arial 11", command=self.exit_button)
        exit_button.grid(column=0, row=6, pady=14)





    def refresh(self):
        self.top_frame.pack_forget()
        self.top_frame = self.create_top_frame()



    def show_meals_list(self):
        pass



    def add_meal_to_list(self):
        pass


    def delete_meal_from_list(self):
        pass


    def edit_meal(self):
        pass


    def show_shopping_list_button(self):
        pass


    def exit_button(self):
        self.app.destroy()









    def run_app(self):
        self.app.mainloop()












if __name__ == "__main__":
    RandomizeMeals()