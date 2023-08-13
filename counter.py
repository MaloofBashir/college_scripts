with open("newfile.txt",'r') as file:
    contents=file.read()
    values=contents.split(",")
    for val in values:
        print(val)