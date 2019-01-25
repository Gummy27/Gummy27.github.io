with open("text.txt", "w", encoding = "utf-8") as f:
    f.write("This is my first file\n")
    f.write("This file\n\n")
    f.write("Has three lines")
with open("text.txt", "r", encoding = "utf-8") as f:
    f.read()
