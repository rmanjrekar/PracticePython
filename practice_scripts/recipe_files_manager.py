'''
Recipe Manager using files. Handling files, directories with help of Path, os, sys, exception handling
Code will first welcome the user, tell them the path to the directory where the Recipes
folder is located, tell them how many recipes there are inside the folder, and then ask them
to choose one of these options:
1. Option 1 will ask the user for the categories to select and once the user chooses a category, it will ask them the recipe to be selected for read, then it will show the content of that recipe.
2. Option 2 is getting the user to create a new recipe in a specific category: it will also
ask the user to choose a category, but then it will ask the user to write the name and
content of a new recipe, and it will create that file in the correct place.
3. Option 3 will ask for the name of the category the user wants to create and will generate
a brand new folder, a new category with that name.
4. Option 4 will delete recipes: do the same as option one, but instead of reading the
recipe, it will delete it.
5. Option 5 will let the user delete a the input category provided by user.
6. Option 6 will end the execution of the code (just end the program). 
'''

import os
from pathlib import Path
import sys
import shutil

print("Welcome!!!")
guide = Path(Path.home(),'python','Recipes')

'''
	Gets the text files in the path mentioned using glob 
'''
def get_recipe_files():
	recipe_list=[]
	files_folder = {}
	recipe_complete_list=[]
	for txt_file in Path(guide).glob('**/*.txt'):     
		recipetext = []
		recipe_complete_list.append(str(txt_file))
		folderpath = str(txt_file.parent)
		name = txt_file.name
		recipetext.append(name)

		if folderpath in files_folder:
			val = files_folder[folderpath]
			val.append(name)
			files_folder[folderpath] = val
		else:
			files_folder[folderpath] = recipetext
		
		recipe_list.append(name)
	
	return recipe_list, files_folder, recipe_complete_list 

'''
	Reads the contents of selected recipe file
'''
def read_file(path_selected):
	print("File selected for read ", path_selected)
	my_file = open(path_selected,'r')
	print("Contents of file are : ", my_file.read())

'''
	Writes content to the new recipe file
'''
def write_file(path,content):
	print("Writing Contents at ", path)
	my_file = open(path,'w')
	my_file.write(content)

'''
	Returns Dictionary which contains folder name and path except hidden folders
'''
def get_visible_folders(directory_path):
    folders = {folder.name: str(folder) for folder in directory_path.iterdir() 
	            if folder.is_dir() and not folder.name.startswith('.')}
    return folders

'''
	Takes input from user for category and returns the path of it
'''
def get_category_path():
	count = 1
	cat_folder = get_visible_folders(guide)
	mylist = list(cat_folder.keys())
	print("Category Folders -> ", mylist)

	for fold in cat_folder :
		print(f"{count}. {fold}")
		count += 1	
	try:
		input_category = input("Select the category ")
		path_selected = cat_folder[mylist[int(input_category) - 1]]
		print("Path selected -> ", path_selected)
		return path_selected
	except IndexError as i:
		print(f"Index error occurred while removing the file: {i}")
	except Exception as e:
		print(f"Bad operation : {e}")

'''
	Clears the console
'''
def clear_console():
	clear_flag = input("Press 'C' to clear the console ") 
	if clear_flag == 'C':
		os.system('clear')
	else:
		print("Selected wrong flag")
		clear_console()

'''
	Operations to be performed
'''
def start():	
	print("1. Read Recipe")
	print("2. Create Recipe")
	print("3. Create Category")
	print("4. Delete Recipe")
	print("5. Delete Category")
	print("6. End Program")
	user_input = input("Select the operation from above ")
	return user_input

def main():
	recipe_list, files_folder, recipe_complete_list = get_recipe_files()
	for key,value in files_folder.items():
		print(f"Directory {key} : ", value)

	total_recipe = len(recipe_list)
	print(f"User have {total_recipe} recipes to select")

	while(1):
		user_input = start()
		print("Selected Operation -> ", user_input)
		if(user_input == "1"):
			path_selected = get_category_path()
			recipe_list, files_folder, recipe_complete_list = get_recipe_files() # to get updated data
			if path_selected in files_folder :
				frecipes = files_folder[path_selected] 
				count = 1
				for rec in frecipes:
					print(f"{count}.{rec}")
					count += 1
				try:
					user_in_recipe = input("Select the Recipe ")
					print("Selected Recipe -> " , frecipes[int(user_in_recipe) - 1])
					selected_path = Path(path_selected,frecipes[int(user_in_recipe) - 1])
					read_file(selected_path)
				except IndexError as i:
					print(f"Index error occurred while removing the file: {i}")
				except Exception as e:
					print(f"Bad operation : {e}")
			else :
				print("No recipe available here, Please select correct options")

		elif(user_input == "2"):
			path_selected = get_category_path()
			try:
				if os.path.exists(path_selected): 
					recipe_name = input("Provide the name for Recipe ")
					complete_path = Path(path_selected,recipe_name)
					if os.path.exists(complete_path):
						print("Recipe Name already exists, please select New Recipe name")
					else:
						recipe_content = input("Provide the content for Recipe ")
						recipe_content.strip()
						write_file(complete_path, recipe_content)
				else :
					print("Not a valid selection, Please select another option")
			except Exception as e:
				print(f"Bad operation : {e}")

		elif(user_input == "3"):
			cat_name = input("Provide the name for Category ")
			new_cat_path = Path(guide,cat_name)
			try:
				if os.path.exists(new_cat_path): 
					print("Category already exists, please select New Category name")
				else:
					# Create the directory
					os.mkdir(new_cat_path)	
					print("Directory '% s' created" % cat_name)
			except OSError as ose:
				print(f"An error occurred while creating the file: {ose}")
			except Exception as e:
				print(f"Bad operation : {e}")

		elif(user_input == "4"):
			count = 1
			for rec in recipe_complete_list:
				print(f"{count}.{rec}")
				count += 1
			delete_recipe = input("Select the Recipe to be deleted ")
			try:
				print("Recipe Selected for delete -> " , recipe_complete_list[int(delete_recipe) - 1])
				# Remove the file
				os.remove(recipe_complete_list[int(delete_recipe) - 1])
			except FileNotFoundError:
				print(f"File '{recipe_complete_list[int(delete_recipe) - 1]}' not found.")
			except OSError as ose:
				print(f"An error occurred while removing the file: {ose}")
			except IndexError as i:
				print(f"Index error occurred while removing the file: {i}")
			except Exception as e:
				print(f"Bad operation : {e}")

		elif(user_input == "5"):
			cat_deleted = get_category_path()
			try:
				print("Category to be deleted ", cat_deleted)
				# Remove the directory completely
				shutil.rmtree(cat_deleted)
				print(f"Directory '{cat_deleted}' removed successfully.")
			except FileNotFoundError:
				print(f"Directory '{cat_deleted}' not found.")
			except OSError as ose:
				print(f"An error occurred while removing the directory: {ose}")
			except Exception as e:
				print(f"Bad operation : {e}")
			
		elif(user_input == "6"):
			print("Exiting the script, Bye!!!")
			sys.exit()
		
		else:
			print("Wrong Option selected ")

		clear_console()

if __name__ == '__main__':
    main()