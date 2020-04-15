file = open("doc.txt", "r")

listOfLines = file.readlines()

for line in listOfLines:
    if len(line.strip()) % 2 == 0:
        print(line.strip())

file.close()
