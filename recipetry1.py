import csv
import random

def get_random_recipe(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        recipes = list(reader)
        # Exclude header if present
        if recipes[0][0].lower() == 'recipe':
            recipes = recipes[1:]
        # Choose a random recipe
        random_recipe = random.choice(recipes)
        return random_recipe[0]

if __name__ == "__main__":
    csv_file = "recipe.csv"  # Update with your CSV file name/path
    random_recipe = get_random_recipe(csv_file)
    print("Random Recipe: ", random_recipe)
