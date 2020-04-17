# 6.Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 * C * D)/H]

# C is 50. H is 30.""

# D is the variable whose values s


import math

C = 50
H = 30
Ds = []
result = []
Dv = input("enter the value of D\n")
Ds = Dv.split(",")
Ds = [int(i) for i in Ds]
i = 0
l = len(Ds)
while i < l:
    Q = round(math.sqrt((2 * C * Ds[i]) / H))
    result.append(Q)
    i += 1
print("output=", result)
