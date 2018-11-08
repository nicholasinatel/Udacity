# Program to Rename all Image Files in Folder, Removing Numbers but not letters
# Step: Get All The File Names
# Step: For Each File - Rename it

# Step:0 Count how many Image Files
# Step:1 Check if it is Image File - IF True Go to Step:1 | If False Go to Step:4
# Step:2 Check if it has numbers on name - IF True Go to Step:2 | If False Go to Step:4
# Step:3  Remove Numbers
# Step:4 Go to next file

import glob
import os

def rename_files():
    # (1) get file names from a folder

    # print(glob.glob("C:\Users\Nicholas Fernandes\Desktop\*.pdf"))

    file_list = os.listdir(r"C:\Users\Nicholas Fernandes\Desktop\alphabet\CodedMessage1") 
    # the r before the address of the folder just says, Python Take the String as it is and dont interpret it
    print(file_list)
    # getcwd - Current Working Directory
    saved_path = os.getcwd()
    print(saved_path)

    # Changing CWD - Current Working Directory
    os.chdir(r"C:\Users\Nicholas Fernandes\Desktop\alphabet\CodedMessage1")
    
    # (2) for each file, rename filename
    # http://www.tutorialspoint.com/python/python_for_loop.htm
    # http://www.tutorialspoint.com/python/string_translate.htm
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    
    os.chdir(r"C:\Users\Nicholas Fernandes\Source\Udacity")
    print(os.getcwd())


rename_files()
