# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# without mode is read only or mode="r" (read)
# w mode will replace everything inside the file (write)
#   if the file doesn't exist, it will create the file for you
# a mode will add the text to the existing file (append)

with open("my_file2.txt", mode="w") as file:
    file.write("\nSecond line")
