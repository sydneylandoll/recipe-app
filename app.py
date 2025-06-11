print("Here are your recipes:")

import os

recipe_folder = "recipes"

files = os.listdir(recipe_folder)

md_files = [f for f in files if f.endswith(".md")]

for i, file_name in enumerate(md_files, 1):
    print(f"{i}. {file_name}")
