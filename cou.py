with open("roolno.txt") as file:
    content=file.read()
    values=content.split(",")
    print(len(values))