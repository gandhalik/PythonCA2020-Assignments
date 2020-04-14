#9.	Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
#       Sample data (n=5)
#       Expected Output: {1:1,2:4,3:9,4:16,5:25}

a=int(input("Input a number: "))
d = dict()

for x in range(1,a+1):
    d[x]=x*x

print(d) 
