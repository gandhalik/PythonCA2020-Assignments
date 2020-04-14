# Write a program to construct a dictionary from the two lists containing the names of students and their
# corresponding subjects. The dictionary should maps the students with their respective subjects. Let’s see how to do
# this using for loops and dictionary comprehension.
# HINT-Use Zip function also Student = ['Smit', 'Jaya', 'Rayyan']
# capital = ['CSE', 'Networking', 'Operating System']


Student = ['Smit', 'Jaya', 'Rayyan']
Capital = ['CSE', 'Networking', 'Operating System']

# Printing original keys-value lists
print("Original student list is : " + str(Student))
print("Original subject list is : " + str(Capital))


# to convert lists to dictionary
res = dict(zip(Student, Capital))

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))