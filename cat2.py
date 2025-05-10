class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.bowl = False

    def describe(self):
        print(f"{self.name} is a {self.age}-year-old {self.color} cat.")

    def feeding_cat(self):
        if not self.bowl:
            print(f"{self.name} is hungry. Please put food in the bowl!")
        else:
            print(f"{self.name} is eating happily.")

    def add_food_to_bowl(self):
        self.bowl = True
        print("Food has been added to the bowl.")

# Get user input
name = input("What's your cat's name? ")
age = int(input("How old is your cat? "))  # We convert it to an integer
color = input("What color is your cat? ")

# Create Cat object using user input
user_cat = Cat(name, age, color)

# Describe the cat and interact
user_cat.describe()
user_cat.feeding_cat()        # Will show the cat is hungry
user_cat.add_food_to_bowl()   # Add food
user_cat.feeding_cat()        # Now the cat is eating