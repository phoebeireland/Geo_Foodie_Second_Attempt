import csv
import random

# Ask the user which continent they want to pick from
continent = input("Enter the continent you want to pick from: ")

# Open the CSV file
with open('recipe.csv', 'r') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Filter rows based on the selected continent
    filtered_rows = [row for row in reader if row[2].lower() == continent.lower()]

    if filtered_rows:
        # Randomly select a recipe from the filtered rows
        random_recipe = random.choice(filtered_rows)

        # Extract the first two parts of the randomly selected recipe
        recipe_name = random_recipe[0]
        recipe_description = random_recipe[1]

        # Display the randomly selected recipe
        print(f"Random Recipe from {continent.capitalize()}:")
        print("Country:", random_recipe[3])
        print("Name:", recipe_name)
        print("Description:", recipe_description)
    else:
        print("No recipes found for the selected continent.")
