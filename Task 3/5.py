#5. 	Create a new list which contains the specified numbers after removing the even numbers from a predefined list. 

list = [2, 7, 15, 30, 47, 80, 112, 165, 234, 753]

list = [x for x in list if x%2!=0]

print(list)