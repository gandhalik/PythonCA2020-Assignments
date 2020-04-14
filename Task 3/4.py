# 4. Find the largest and smallest number from a given list.

#creating empty list
list = []

#user defined input - length of the list
num = int(input("Enter number of elements in the list: "))

for i in range(1, num + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    list.append(value)

print("The Smallest Element in this List is : ", min(list))
print("The Largest Element in this List is : ", max(list))

