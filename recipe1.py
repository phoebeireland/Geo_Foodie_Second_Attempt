import csv
import random

def get_random_recipe(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Skip header 1
        recipes = list(reader)
        # Choose a random recipe
        random_recipe = random.choice(recipes)
        return random_recipe[0]

if __name__ == "__main__":
    csv_file = "recipe.csv"  # Update with your CSV file name/path
    random_recipe = get_random_recipe(csv_file)
    print("Random Recipe: ", random_recipe)