import os
from shutil import copyfile
from pathlib import Path

# Lets save the path to the documents directory
dev_directory = str(Path.home()) + "\documents\dev\\"
documents_directory = str(Path.home()) + "\documents\\"

# Does the dev folder exist? 
# print(os.getcwd())


if os.path.isdir(dev_directory):
    # Lets create the student directory
    # os.chdir(dev_directory)
    student_name = input("Whats your name:  ").lower().replace(" ", "")
    print(student_name)
    
    if os.path.isdir(dev_directory + student_name):
        print(student_name + " directory already exists!")
        
        # Lets copy the file from this directory to 
        copyfile("./quarter-1-project.py", dev_directory + student_name + "/quarter-1-project.py")
        print("Copied file to: " + dev_directory + student_name)


    else:
        print("Creating new folder called: " + student_name)
        os.mkdir(dev_directory + student_name)
        print(dev_directory + student_name + " folder Created!")

        # Lets move the quarter 1 file over
        copyfile("./quarter-1-project.py", dev_directory + student_name + "/quarter-1-project.py")
        print("Copied file to: " + dev_directory + student_name)

# Dev folder doesn't exist
else:
    # Lets create the dev folder
    # os.chdir(documents_directory)
    os.mkdir(dev_directory)

    # Lets get the student's name
    student_name = input("Whats your name:  ").lower().replace(" ", "")

    if os.path.isdir(dev_directory + student_name):
        print("directory already exists!")
        
        # Lets copy the file from this directory to 
        copyfile("./quarter-1-project.py", dev_directory + student_name + "/quarter-1-project.py")
        print("Copied file to: " + dev_directory + student_name)

    else:
        print("Creating new folder called: " + student_name)
        os.mkdir(dev_directory + student_name)
        print("Dev folder and student folder created" + dev_directory + student_name)

        
        copyfile("./quarter-1-project.py", dev_directory + student_name + "/quarter-1-project.py")
        print("Copied file to: " + dev_directory + student_name)

        # Lets move the quarter 1 file over



    # print(os.getcwd())


os.system('pause')