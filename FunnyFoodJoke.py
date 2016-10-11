#Download the folder "Why is the mushroom always invited to parties?"
#Save folder to desktop
#Run program to unscramble pictures and reveal the answer to a funny food joke
import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:/Users/user/Desktop/Why is the mushroom always invited to parties?")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:/Users/user/Desktop/Why is the mushroom always invited to parties?")

    #this code has a bug in the part to rename files or print file list. I haven't found the bug yet but it's not working!

    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789") )
    os.chdir(saved_path)

rename_files()
    
