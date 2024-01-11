import json
import random

def pick_random_elements(source_file_path, destination_file_path):
    try:
        # Load the data from the source JSON file
        with open(source_file_path, 'r') as file:
            data = json.load(file)

        # Categories to pick from
        categories = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic']

        # Ensure all categories are present
        if all(category in data for category in categories):
            # Randomly pick one item from each category and store them
            selected_items = {category: random.choice(data[category]) for category in categories}
        else:
            missing_categories = [category for category in categories if category not in data]
            raise ValueError(f"JSON does not contain required categories: {missing_categories}")

        # Write the selected items to the destination JSON file
        with open(destination_file_path, 'w') as file:
            json.dump(selected_items, file, indent=4)

    except Exception as e:
        print(f"An error occurred: {e}")

# Path to your source and destination JSON files
source_file_path = ".github/workflows/Array.json"
destination_file_path = ".github/workflows/current_chances.json"
pick_random_elements(source_file_path, destination_file_path)
