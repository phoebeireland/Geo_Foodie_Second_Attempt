import csv
import random

# Ask the user which meal type they want to pick from
meal_type = input("Enter the meal type (starter, main, side or dessert) you want to pick from: ")

# Ask the user which continent they want to pick from
continent = input("Enter the continent you want to pick from: ")

# Open the CSV file
with open('recipe.csv', 'r') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Filter rows based on the selected continent
    filtered_rows = [row for row in reader if row[2].lower() == continent.lower()]

    # Function to print text with underline
    def print_underline(text):
        print(f"\033[4m{text}\033[0m")

    if filtered_rows:
        # Randomly select a recipe from the filtered rows
        random_recipe = random.choice(filtered_rows)

        # Extract the first two parts of the randomly selected recipe
        recipe_name = random_recipe[0]
        recipe_description = random_recipe[1]

        # Display the randomly selected recipe
        print_underline(f"Random Recipe from {continent.capitalize()}")
        print("Country:", random_recipe[3])
        print("Type of meal:", random_recipe[4])
        print("Vegetation or Vegan:", random_recipe[5])
        print("Name:", recipe_name)
        print("Description:", recipe_description)
    else:
        print("No recipes found for the selected continent.")
