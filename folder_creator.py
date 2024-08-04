import os

folder = [] #for storing folders
n = int(input("How many folders do you want???"))

for folnames in range(n):
    folder_name = input("Please Enter your folder name: ")
    folder.append(folder_name)

for folder_name in folder:
    os.makedirs(folder_name)
