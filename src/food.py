import os
import random

def add_recipe():
    """
    Function to add a new recipe to the database.
    This function will prompt the user for recipe details and save them.
    """

    recipe_name = input("Enter the recipe name to add: ").lower()
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')
    ease_of_cooking = input("Enter the ease of cooking (easy, medium, hard): ").strip().lower()
    link = input("Enter the recipe link: ").strip()

    # create and write to a file with name recipe_name.txt in the recipes directory
    recipes_dir = '../recipes'
    if not os.path.exists(recipes_dir):
        os.makedirs(recipes_dir)
    recipe_file_path = os.path.join(recipes_dir, f"{recipe_name}.txt")

    with open(recipe_file_path, 'w') as recipe_file:
        recipe_file.write(f"Recipe Name: {recipe_name}\n")
        recipe_file.write(f"Ingredients: {', '.join(ingredients)}\n")
        recipe_file.write(f"Ease of Cooking: {ease_of_cooking}\n")
        recipe_file.write(f"Link: {link}\n")
    
    print(f"Recipe '{recipe_name}' added with ingredients {ingredients} and ease '{ease_of_cooking}'.")

def modify_recipe():
    """
    Function to modify an existing recipe in the database.
    This function will prompt the user for the recipe name and new details to update.
    """

    recipe_name = input("Enter the recipe name to modify: ").lower()
    recipes_dir = 'recipes'
    recipe_file_path = os.path.join(recipes_dir, f"{recipe_name}.txt")

    if not os.path.exists(recipe_file_path):
        print(f"Recipe '{recipe_name}' does not exist.")
        return

    # read old data to use later
    with open(recipe_file_path, 'r') as recipe_file:
        lines = recipe_file.readlines()
        existing_ingredients = ''
        existing_ease_of_cooking = ''
        existing_link = ''
        for line in lines:
            if line.startswith("Ingredients:"):
                existing_ingredients = line.strip().split(': ')[1]
            elif line.startswith("Ease of Cooking:"):
                existing_ease_of_cooking = line.strip().split(': ')[1]
            elif line.startswith("Link:"):
                existing_link = line.strip().split(': ')[1]

    new_ingredients = input("Enter the new ingredients (comma-separated), or enter if no changes: ").split(',')
    new_ease_of_cooking = input("Enter the new ease of cooking (easy, medium, hard) or enter if no changes: ").strip().lower()
    new_link = input("Enter the new recipe link or enter if no changes: ").strip()

    with open(recipe_file_path, 'w') as recipe_file:
        recipe_file.write(f"Recipe Name: {recipe_name}\n")
        if (new_ingredients and not new_ingredients == ['']):
            recipe_file.write(f"Ingredients: {', '.join(new_ingredients)}\n")
        else:
            recipe_file.write(f"Ingredients: {existing_ingredients}\n")
        if (new_ease_of_cooking and new_ease_of_cooking != ''):
            recipe_file.write(f"Ease of Cooking: {new_ease_of_cooking}\n")
        else:
            recipe_file.write(f"Ease of Cooking: {existing_ease_of_cooking}\n")

        if (new_link and new_link != ''):
            recipe_file.write(f"Link: {new_link}\n")
        else:
            recipe_file.write(f"Link: {existing_link}\n")
    
    print(f"Recipe '{recipe_name}' modified with new ingredients {new_ingredients} and ease '{new_ease_of_cooking}'.")

def delete_recipe():
    """
    Function to delete a recipe from the database.
    This function will prompt the user for the recipe name and delete the file if it exists.
    """
    recipe_name = input("Enter the recipe name to delete: ").lower()
    recipes_dir = 'recipes'
    recipe_file_path = os.path.join(recipes_dir, f"{recipe_name}.txt")

    if not os.path.exists(recipe_file_path):
        print(f"Recipe '{recipe_name}' does not exist.")
        return

    os.remove(recipe_file_path)
    print(f"Recipe '{recipe_name}' deleted successfully.")

def randomly_generate_recipe(ingredients_not_owned):
    """
    Function to randomly generate a recipe based on ingredients not owned.
    This function will read all recipes and filter out those that can be made with the given ingredients.
    """

    recipes_dir = '../recipes'
    if not os.path.exists(recipes_dir):
        print("No recipes available.")
        return

    available_recipes = []
    
    for filename in os.listdir(recipes_dir):
        if filename.endswith('.txt'):
            recipe_file_path = os.path.join(recipes_dir, filename)
            with open(recipe_file_path, 'r') as recipe_file:
                lines = recipe_file.readlines()
                for line in lines:
                    if line.startswith("Ingredients:"):
                        ingredients = line.strip().split(': ')[1].split(', ')
                        if not any(ingredient.strip() in ingredients_not_owned for ingredient in ingredients):
                            available_recipes.append(filename[:-4])  # remove .txt extension

    if not available_recipes:
        print("No recipes can be made with the given ingredients.")
        return

    print(f"Available recipes: {available_recipes}")
    selected_recipe = random.choice(available_recipes)
    print(f"Randomly selected recipe: {selected_recipe}")

randomly_generate_recipe(["1"])