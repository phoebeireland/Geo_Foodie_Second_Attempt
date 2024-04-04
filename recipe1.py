import csv
import random

# Function to get user input for meal type
def get_meal_type():
    print("Meal Types:")
    print("1. Starter")
    print("2. Main")
    print("3. Side")
    print("4. Dessert")
    meal_type_choice = input("Enter the number of the meal type you want to pick: ")
    return meal_type_choice

# Function to get user input for continent
def get_continent():
    print("Continents:")
    print("1. Asia")
    print("2. Europe")
    print("3. North America")
    print("4. South America")
    print("5. Africa")
    print("6. Australia")
    continent = input("Enter the continent you want to pick from: ")
    return continent

# Ask the user to pick meal type
meal_type_choice = get_meal_type()

# Determine the meal type based on user input
if meal_type_choice == "1":
    meal_type = "Starter"
elif meal_type_choice == "2":
    meal_type = "Main"
elif meal_type_choice == "3":
    meal_type = "Side"
elif meal_type_choice == "4":
    meal_type = "Dessert"
else:
    print("Invalid choice. Please enter a valid number (1, 2, 3 or 4).")
    exit()

# Ask the user to pick continent
continent_choice = get_continent()

# Determine the continent based on user input
if continent_choice == "1":
    continent = "Asia"
elif continent_choice == "2":
    continent = "Europe"
elif continent_choice == "3":    
    continent = "North America"
elif continent_choice == "4":
    continent = "South America"
elif continent_choice == "5":
    continent = "Africa"
elif continent_choice == "6":
    continent = "Australia"
else:
    print("Invalid choice. Please enter a valid number (1, 2, 3, 4, 5 or 6).")
    exit()

# Open the CSV file
with open('recipe.csv', 'r') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Filter rows based on the selected continent and meal type
    filtered_rows = [row for row in reader if row[2].strip().lower() == continent.strip().lower() and row[4].strip().lower() == meal_type.strip().lower()]

    # Function to print text with underline
    def print_underline(text):
        print(f"\033[4m{text}\033[0m")

    if filtered_rows:
        # Randomly select a recipe from the filtered rows
        random_recipe = random.choice(filtered_rows)

        # Extract the first two parts of the randomly selected recipe
        recipe_name = random_recipe[0]
        recipe_description = random_recipe[1]
        recipe_origin = random_recipe[3]
        recipe_vegornot = random_recipe[5]

        # Display the randomly selected recipe
        print_underline(f"Random {meal_type} Recipe from {continent.capitalize()}:")
        print("Country of Origin:", recipe_origin)
        print("Name:", recipe_name)
        print("Veg/Non-Veg:", recipe_vegornot)
        print("Description:", recipe_description)
    else:
        print("No recipes found for the selected continent and meal type.")

