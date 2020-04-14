# Write a program to Python find out the character in a string which is uppercase using list comprehension.

# Using list comprehension + isupper()

# initializing string
test_str = input("The sentence is: ")

# printing original string
print("The original string is : " + str(test_str))

# Extract Upper Case Characters
# Using list comprehension + isupper()
res = [char for char in test_str if char.isupper()]

# printing result
print("The uppercase characters in string are : " + str(res))
