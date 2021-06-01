# 3. Write a Python program to append text to a file and display the text.

from pathlib import Path

file_path = Path() / "files\\demos\\hello.txt"

# print(file_path.absolute())
with open(file_path , 'a') as file:
    try:
        file.write("\n I am studying pyhon")
    except Exception as e:
        print(e)
    else:
        print("File appended succesfully")
