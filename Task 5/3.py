# Write a program to handle an error if the user entered the number more than four digits it should return “Please
# length is too short/long !!! Please provide only four digits”


x = str(input("Enter 4 numbers"))
if len(x) > 4:
    raise Exception("Please length is too short/long!!! Please provide only four digits")

