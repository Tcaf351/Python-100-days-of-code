# File System
# with  open("day 24/my_file.txt") as file: # writing this means you don't have to write file.close() to close file
#     contents = file.read()
#     print(contents)

with  open("day 24/new_file.txt", mode="w") as file: # writing this means you don't have to write file.close() to close file
    file.write("\nNew Text...")
