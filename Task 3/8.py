# 8.	Create a new dictionary by concatenating the following two dictionaries:
#        a={1:10,2:20}
#        b={3:30,4:40}
#        Expected Result: {1:10,2:20,3:30,4:40}

a = {1:10,2:20}
b = {3:30,4:40}

print("a = ", a)
print("b = ", b)

def merge(a,b):
    result = {**a,**b}
    return result

res = merge(a,b)
print("Expected Result = ", res)

